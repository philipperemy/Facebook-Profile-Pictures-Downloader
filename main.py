import json

from utils import *

# https://developers.facebook.com/tools/explorer/
if __name__ == '__main__':
    credentials = json.load(open('credentials.json', 'r'))
    fb_auth_token = credentials['FB_AUTH_TOKEN']
    profile_id = get_last_profile_id(default=1261675464)
    while True:
        print('Processing profile id = {}'.format(profile_id))
        extract_information(profile_id, fb_auth_token)
        profile_id += 1
