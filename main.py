__author__ = "pwcz"
import bs4
from urllib.request import Request, urlopen
import re
import json
import signal
import sys
import base64
from time import sleep
import numpy as np
import datetime
from collections import defaultdict
import logging as logger
from telegram_sender import TelegramSender
logger.basicConfig(format='%(name)s:%(levelname)s:%(message)s', level=logger.DEBUG)


class CascadaNotifier:
    def __init__(self):
        self.url_link = base64.b64decode(b'aHR0cDovL3d3dy5jYXNjYWRhLmNvbS5wbC9wbC5zcXVhc2hfYzA2Lmh0bWw=')\
            .decode("utf-8")
        self.bs4_data = None
        self.raw_data = []
        self.f_name = "http_dump.txt"
        self.json_file = 'data.json'
        self.json_obj = None
        self.config = None
        self.telegram = TelegramSender()

    @staticmethod
    def _load_json(json_file):
        with open(json_file, "r") as file:
            return json.loads(file.read())

    def _download_data(self):
        logger.info("download data")
        req = Request(self.url_link)
        code_html = urlopen(req).read().decode()
        self.bs4_data = bs4.BeautifulSoup(code_html, "lxml")

    def _decode(self):
        self._download_data()
        data = bs4.BeautifulStoneSoup.select(self.bs4_data, "script")[18].text
        regex = re.compile(r"events: \[([^]]+)\]")
        m = str(regex.search(data).groups()[0])
        replace_t = (("id", "\"id\""), ("title", "\"title\""), ("start", "\"start\""), ("end", "\"end\""),
                     ("'", "\""), (" ", ""))
        for a1, a2 in replace_t:
            m = m.replace(a1, a2)
        regex = r"\{(.*?)\}"
        matches = re.finditer(regex, m, re.MULTILINE | re.DOTALL)
        self.raw_data = [json.loads(x.group(0)) for x in matches]

    def _get_empty_slots(self, data, minimum=17, maximum=21):
        hours = np.arange(1, 24, dtype=np.uint8)
        for reserv in self.raw_data:
            if data in reserv['start']:
                start_date = int(reserv['start'].replace(data + "T", "").split(":")[0])
                stop_date = int(reserv['end'].replace(data + "T", "").split(":")[0])
                hours[start_date:stop_date] = 0
        return np.where((hours >= minimum) & (hours <= maximum))[0].tolist()

    def _seach_week_for_empty_reservation(self):
        now = datetime.datetime.now()
        reserv_dict = {}
        for _ in range(0, 7):
            if now.weekday() > 3:
                now += datetime.timedelta(days=1)
                continue
            check_date = now.strftime("%Y-%m-%d")
            available_hours = self._get_empty_slots(check_date)
            reserv_dict[check_date] = available_hours
            now += datetime.timedelta(days=1)
        data2send = self._update_json(reserv_dict)
        if len(data2send) > 0:
            self._send_notification(data2send)

    def _update_json(self, reserv):
        message = defaultdict(list)
        if self.json_obj is None:
            self.json_obj = CascadaNotifier._load_json(self.json_file)
            self.json_obj = defaultdict(list, self.json_obj)
        for key, items in reserv.items():
            for day in items:
                if day not in self.json_obj[key]:
                    message[key].append(day)
                    self.json_obj[key].append(day)
        with open(self.json_file, "w+") as file:
            json.dump(self.json_obj, file)
        return message

    def _send_notification(self, message):
        data = "\n".join([key + ": " + " ".join([str(x) for x in items]) for key, items in message.items()])
        logger.info("message = %s", data)
        self.telegram.send_messages(data)

    def run(self):
        self.telegram.start()
        while True:
            if 6 < datetime.datetime.now().hour < 22:
                self._decode()
                self._seach_week_for_empty_reservation()
            sleep(60*10)


def signal_handler(_, __):
    logger.info("NOTIFIER STOP")
    notifier_obj.telegram.stop()
    sys.exit(0)


if __name__ == "__main__":
    logger.info("Start cascada-notifier")
    notifier_obj = CascadaNotifier()
    signal.signal(signal.SIGINT, signal_handler)
    notifier_obj.run()
