__author__ = "pwcz"
import json
import logging
from time import sleep
from telegram.ext import Updater, CommandHandler


class TelegramSender:
    logger = logging.getLogger(__name__)
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    def __init__(self):
        self.config_file = "config.json"
        self.config = TelegramSender._load_json(self.config_file)
        self.updater = Updater(self.config['TG_BOT_HASH'])
        self.users = self.config["notification_receivers"]

    def _prepare(self):
        dp = self.updater.dispatcher

        # on different commands - answer in Telegram
        dp.add_handler(CommandHandler("start", self._start))
        dp.add_handler(CommandHandler("help", TelegramSender._help))
        dp.add_handler(CommandHandler("stop", self._stop))

        # log all errors
        dp.add_error_handler(self._error)

    def start(self):
        self._prepare()
        self.updater.start_polling()

    def stop(self):
        self.updater.stop()

    def send_messages(self, message):
        for user in self.users:
            self.updater.bot.send_message(chat_id=user, text=message)

    def _error(self, _, update, error):
        """Log Errors caused by Updates."""
        self.logger.warning('Update "%s" caused error "%s"', update, error)

    @staticmethod
    def _help(_, update):
        update.message.reply_text('Hello I\'am  cascada notification bot :)\nuse /start to add to '
                                  'notification list or /stop to remove.')

    def _start(self, _, update):
        chat_id = update.message.chat_id
        if chat_id in self.config["notification_receivers"]:
            update.message.reply_text('You are already in receiver list')
        else:
            self.config["notification_receivers"].append(chat_id)
            self._update_json()
            update.message.reply_text('You have successfully added to receiver list')

    def _stop(self, _, update):
        try:
            self.config["notification_receivers"].remove(update.message.chat_id)
            update.message.reply_text('You have successfully removed from receiver list')
        except ValueError:
            update.message.reply_text('You are not in receiver list')

    def _update_json(self):
        with open(self.config_file, "w+") as file:
            json.dump(self.config, file)

    @staticmethod
    def _load_json(json_file):
        with open(json_file, "r") as file:
            return json.loads(file.read())


if __name__ == "__main__":
    _test = TelegramSender()
    _test.start()
    sleep(15)
    _test.send_messages("halo halo")
    _test.stop()
