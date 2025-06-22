import configparser
from discoIPC import ipc
import requests
from requests.structures import CaseInsensitiveDict
import time


class DiscordRichPresenceForXbox:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.client = ipc.DiscordIPC(config['CLIENT']['client_id'])
        self.x_uid = config['X_UID']['x_uid']
        self.open_xbl_key = config['OPEN_XBL_KEY']['open_xbl_key']
        self.activity = {
            'timestamps': {},
            'assets': {
                'large_image': 'xbox',
                'large_text': 'Xbox'
            }
        }

    def check_and_update_status(self):
        try:
            self.client.connect()
        except Exception as discord_not_running_error:
            print(discord_not_running_error)
            return

        print('Connected to Discord client...')
        time_elapsed = int(time.time())
        prev_game = None
        was_at_home = False

        def set_activity(details, state):
            self.activity['details'] = details
            self.activity['state'] = state
            self.activity['timestamps']['start'] = time_elapsed
            return self.activity

        while True:
            print('Checking for status update...')
            url = 'https://xbl.io/api/v2/{}/presence'.format(self.x_uid)
            xbl_req_headers = CaseInsensitiveDict()
            xbl_req_headers['X-Authorization'] = self.open_xbl_key
            xbl_response = requests.request('GET', url, headers=xbl_req_headers)
            if xbl_response.status_code != 200:
                print('Something went wrong...')
                return
            try:
                game = xbl_response.json()[0]['devices'][0]['titles'][0]['name']
                print(xbl_response.json())
            except IndexError:
                print('User is not playing anything...')
                prev_game = None
                if not was_at_home:
                    time_elapsed = int(time.time())
                was_at_home = True
                cur_activity = xbl_response.json()[0]['devices'][0]['titles'][0]['name']
                self.client.update_activity(set_activity('At...', cur_activity))
                time.sleep(30)
                continue
            except KeyError:
                print('Xbox is turned off...')
                return
            if game == prev_game:
                print('User is playing the same thing...')
                time.sleep(30)
                continue
            if was_at_home:
                was_at_home = False
            print('User is playing something new...')
            time_elapsed = int(time.time())
            prev_game = game
            self.client.update_activity(set_activity('Playing...', game))
            time.sleep(30)


status = DiscordRichPresenceForXbox()
while True:
    try:
        status.check_and_update_status()
    except Exception as base_error:
        print(base_error)
        print('Base Error.')
    time.sleep(20)
