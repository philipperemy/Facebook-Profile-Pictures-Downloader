from glob import glob
from time import sleep


# https://developers.facebook.com/tools/explorer/

def scan(_prev_num_desc, _prev_num_imgs):
    num_desc = len(glob('data/**.pkl'))
    num_imgs = len(glob('data/**.jpg'))
    print('-' * 80)
    print('Number of Facebook descriptions : {} (+{})'.format(num_desc, num_desc - _prev_num_desc))
    print('Number of Facebook images       : {} (+{})'.format(num_imgs, num_imgs - _prev_num_imgs))
    return num_desc, num_imgs


if __name__ == '__main__':
    prev_num_desc = 0
    prev_num_imgs = 0
    refresh_interval = 10
    print('This scripts refreshes every {} seconds.'.format(refresh_interval))
    while True:
        prev_num_desc, prev_num_imgs = scan(prev_num_desc, prev_num_imgs)
        sleep(refresh_interval)
