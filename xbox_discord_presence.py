import requests
from requests.structures import CaseInsensitiveDict
import time
from discoIPC import ipc
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

client = ipc.DiscordIPC(config['CLIENT']['client_id'])
x_uid = config['X_UID']['x_uid']
open_xbl_key = config['OPEN_XBL_KEY']['open_xbl_key']


def check_open():
    try:
        client.connect()
    except Exception as e:
        print(e)
        return

    print('Connected to Discord client...')

    activity = {
        'timestamps': {},
        'assets': {
            'large_image': 'xbox',
            'large_text': 'Xbox'
        }
    }

    print('Starting Discord ICP')
    time_elapsed = int(time.time())
    prev_game = None
    was_at_home = False

    def set_activity(state, details):
        activity['state'] = state
        activity['details'] = details
        activity['timestamps']['start'] = time_elapsed
        return activity

    while True:
        print('Checking for status update...')
        url = 'https://xbl.io/api/v2/presence/{}'.format(x_uid)
        headers = CaseInsensitiveDict()
        headers["X-Authorization"] = open_xbl_key
        resp = requests.get(url, headers=headers)
        try:
            game = resp.json()[0]['devices'][0]['titles'][1]['name']
        except IndexError:
            print('User is not playing game...')
            prev_game = None
            if not was_at_home:
                time_elapsed = int(time.time())
            was_at_home = True
            cur_activity = resp.json()[0]['devices'][0]['titles'][0]['name']
            client.update_activity(set_activity(cur_activity, 'At...'))
            time.sleep(30)
            continue
        if game == prev_game:
            print('User is playing the same game...')
            time.sleep(30)
            continue
        if was_at_home:
            was_at_home = False
        print('User is playing a new game...')
        time_elapsed = int(time.time())
        prev_game = game
        client.update_activity(set_activity(game, 'Playing...'))
        time.sleep(30)


while True:
    check_open()
    time.sleep(60)
