import json

import numpy as np
from numpy.random import randint

from utils import *


def parallel_function(f, sequence, num_threads=None):
    from multiprocessing import Pool
    pool = Pool(processes=num_threads)
    result = pool.map(f, sequence)
    cleaned = [x for x in result if x is not None]
    pool.close()
    pool.join()
    return cleaned


def run(profile_id_start):
    while True:
        log('Processing profile id = {}'.format(profile_id_start))
        extract_information(profile_id_start, fb_auth_token)
        profile_id_start += 1


def find_smallest_different_between_two_elements(arr):
    return min(np.diff(np.sort(arr)))


# https://developers.facebook.com/tools/explorer/
if __name__ == '__main__':
    credentials = json.load(open('credentials.json', 'r'))
    fb_auth_token = credentials['FB_AUTH_TOKEN']
    profile_id = get_last_profile_id(default=1261675464)
    num_threads = 8
    # profile_ids = np.cumsum([profile_id // num_threads] * num_threads)
    while True:
        profile_ids = randint(10, profile_id, size=num_threads)
        smallest_difference = find_smallest_different_between_two_elements(profile_ids)
        if smallest_difference > 1e5:
            break
    parallel_function(run, profile_ids, num_threads)
