import sys

from numpy.random import randint

from utils import *
from utils import parallel_function, run, find_smallest_different_between_two_elements


def main():
    profile_id = get_last_known_profile_id(default=1676655434)
    assert len(sys.argv) == 2, 'Please input the number of threads as a parameter.'
    num_threads = int(sys.argv[1])
    print('Using {} threads.'.format(num_threads))
    while True:
        profile_ids = randint(10, profile_id, size=num_threads)
        if num_threads > 1:
            smallest_difference = find_smallest_different_between_two_elements(profile_ids)
            if smallest_difference > 1e5:
                break
        else:
            break
    parallel_function(run, profile_ids, num_threads)


# Get your token ID here https://developers.facebook.com/tools/explorer/
if __name__ == '__main__':
    main()
