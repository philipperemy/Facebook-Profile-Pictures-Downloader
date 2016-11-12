import json

from utils import *

if __name__ == '__main__':
    credentials = json.load(open('credentials.json', 'r'))
    fb_auth_token = credentials['FB_AUTH_TOKEN']
    profile_id = get_last_profile_id(default=1)
    while True:
        extract_information(profile_id, fb_auth_token)
