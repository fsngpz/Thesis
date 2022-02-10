import os
import yaml
from telegram.ext import MessageHandler, Updater, Filters

def resrictedUser_space(update, context):
    update.message.reply_text("Valid User")

if __name__ == "__main__":
    base_path = os.path.dirname(os.path.abspath(__file__))
    config = yaml.load(open(os.path.join(base_path, 'config.yaml')).read(), Loader=yaml.FullLoader)
    updater = Updater(token=config['general']['token'], use_context=True)

    dispatcher = updater.dispatcher
    user_handler = MessageHandler(Filters.chat(username=config['general']['usernames']),resrictedUser_space)
    dispatcher.add_handler(user_handler)
    updater.start_polling()