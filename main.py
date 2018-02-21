import bs4
from urllib.request import Request, urlopen
import re
import json
import base64
import os.path
import numpy as np
import datetime


class CascadaNotifier:
    def __init__(self):
        self.url_link = base64.b64decode(b'aHR0cDovL3d3dy5jYXNjYWRhLmNvbS5wbC9wbC5zcXVhc2hfYzA2Lmh0bWw=') \
            .decode("utf-8")
        self.bs4_data = None
        self.raw_data = []
        self.f_name = "http_dump.txt"

    def _download_data(self):
        print("download data")
        req = Request(self.url_link)
        code_html = urlopen(req).read().decode()
        self.bs4_data = bs4.BeautifulSoup(code_html, "lxml")

    def _decode(self):
        if not os.path.isfile(self.f_name):
            self._download_data()
            data = bs4.BeautifulStoneSoup.select(self.bs4_data, "script")[18].text
            regex = re.compile(r"events: \[([^]]+)\]")
            m = str(regex.search(data).groups()[0])
            replace_t = (("id", "\"id\""), ("title", "\"title\""), ("start", "\"start\""), ("end", "\"end\""),
                         ("'", "\""), (" ", ""))
            for a1, a2 in replace_t:
                m = m.replace(a1, a2)
            with open(self.f_name, "w+") as file:
                file.write(m)
        else:
            m = open(self.f_name, 'r').read()
        regex = r"\{(.*?)\}"
        matches = re.finditer(regex, m, re.MULTILINE | re.DOTALL)
        for x in matches:
            self.raw_data.append(json.loads(x.group(0)))

    def _get_empty_slots(self, data, minimum=17, maximum=20):
        hours = np.ones(23, dtype=int)
        for reserv in self.raw_data:
            if data in reserv['start']:
                print(reserv)
                start_date = int(reserv['start'].replace(data + "T", "").split(":")[0])
                stop_date = int(reserv['end'].replace(data + "T", "").split(":")[0])
                for idx in range(start_date, stop_date):
                    hours[idx] = 0
                print([x for x in range(start_date, stop_date)])
        print(np.where((hours > 0) & (hours >= minimum) & (hours <= maximum)))

    def test(self):
        self._decode()
        # for idx, data in enumerate(self.raw_data):
        #     print(data)
        #     if idx is 18:
        #         break
        self._get_empty_slots("2018-02-21", minimum=0)


if __name__ == "__main__":
    _test = CascadaNotifier()
    _test.test()