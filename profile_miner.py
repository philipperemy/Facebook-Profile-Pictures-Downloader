import sys
from time import sleep

from numpy.random import randint

from utils import *

USER_REQUEST_LIMIT_REACHED_SECONDS_BEFORE_RESUMING_SEC = 3600 * 2


def main():
    while True:
        try:
            default_profile_id = 1676655434
            profile_id = get_last_known_profile_id(default=default_profile_id)
            assert len(sys.argv) == 2, 'Please input the number of threads as a parameter.'
            num_threads = int(sys.argv[1])
            log('Using {} threads.'.format(num_threads))
            profile_ids = [default_profile_id]
            while True:
                profile_ids = randint(10, profile_id, size=num_threads)
                if num_threads > 1:
                    smallest_difference = find_smallest_different_between_two_elements(profile_ids)
                    if smallest_difference > 1e5:
                        break
                else:
                    break
            parallel_function(run, profile_ids, num_threads)
        except UserRequestLimitReached as urlr:
            print(str(urlr))
            log('UserRequestLimitReached exception raised. Lets pause down the script for a while')
            log('Going to wait for {} seconds.'.format(USER_REQUEST_LIMIT_REACHED_SECONDS_BEFORE_RESUMING_SEC))
            sleep(USER_REQUEST_LIMIT_REACHED_SECONDS_BEFORE_RESUMING_SEC)
        except AccessTokenExpired as ate:
            print(str(ate))
            log('AccessTokenExpired exception raised. Lets update the token.')
            log('Lets check if the server from auto_token_generator.py is started')
            try:
                response = requests.get('http://localhost:5000/')
                assert response.status_code == 200
                new_token = response.content['fb_auth_token']
                log('New token successfully fetched = {}'.format(new_token))
                overwrite_current_token(new_token)
                log('Script is going to restart. Stay tuned!')
            except:
                log('Script is going to end. Could not contact the auto token generator.')
                log('Please start it or get a new token at https://developers.facebook.com/tools/explorer/.')
                exit(1)
        except InvalidToken as it:
            print(str(it))
            log('Invalid token. Application will stop.')
            log('Please request a new and valid token here https://developers.facebook.com/tools/explorer/.')
            exit(1)


# Get your token ID here https://developers.facebook.com/tools/explorer/
if __name__ == '__main__':
    main()
