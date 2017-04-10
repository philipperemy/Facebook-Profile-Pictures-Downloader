import sys
from time import sleep

from numpy.random import randint

from utils import *

USER_REQUEST_LIMIT_REACHED_SECONDS_BEFORE_RESUMING_SEC = 3600 * 1  # one hour here.


def main():
    while True:
        try:
            default_max_known_profile_id = 1676655434
            max_known_profile_id = get_last_known_profile_id(default=default_max_known_profile_id)
            assert len(sys.argv) == 2, 'Please input the number of threads as a parameter.'
            num_threads = int(sys.argv[1])
            log('Using {} threads.'.format(num_threads))
            profile_ids = [default_max_known_profile_id]
            while True:
                profile_ids = randint(10, max_known_profile_id, size=num_threads)
                if num_threads > 1:
                    smallest_difference = find_smallest_different_between_two_elements(profile_ids)
                    if smallest_difference > 1e5:
                        break
                else:
                    break
            parallel_function(run, profile_ids, num_threads)
        except UserRequestLimitReached as urlr:
            print(str(urlr))
            log('UserRequestLimitReached exception raised. Lets pause down the script for a while.')
            log('Going to wait for {} seconds before restarting.'.format(
                USER_REQUEST_LIMIT_REACHED_SECONDS_BEFORE_RESUMING_SEC))
            sleep(USER_REQUEST_LIMIT_REACHED_SECONDS_BEFORE_RESUMING_SEC)
        except CaptchaDetectedOnPage as cdop:
            print(str(cdop))
            log('CaptchaDetectedOnPage exception raised. Lets pause down the script for a while.')
            log('Going to wait for {} seconds before restarting.'.format(
                USER_REQUEST_LIMIT_REACHED_SECONDS_BEFORE_RESUMING_SEC))
            sleep(USER_REQUEST_LIMIT_REACHED_SECONDS_BEFORE_RESUMING_SEC)
        except AccessTokenExpired as ate:
            print(str(ate))
            log('AccessTokenExpired exception raised. Lets update the token.')
            update_token()
        except InvalidToken as it:
            print(str(it))
            log('InvalidToken exception raised. Lets update the token.')
            update_token()


# Get your token ID here https://developers.facebook.com/tools/explorer/
if __name__ == '__main__':
    main()
