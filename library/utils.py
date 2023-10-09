import threading
from typing import *
import locale

def get_message(message_dict):
    system_lang = locale.getdefaultlocale()[0]

    if system_lang == 'ja_JP':
        return message_dict['ja']
    else:
        return message_dict['en']

def fire_in_thread(f, *args, **kwargs):
    threading.Thread(target=f, args=args, kwargs=kwargs).start()