import bs4
import requests
import wget


def extract_information(profile_id, base_url):
    # FULL NAME
    r = requests.get('http://facebook.com/profile.php?id={}'.format(profile_id))
    assert r.status_code == 200
    print('[profile redirect url] -> {}'.format(r.url))
    soup = bs4.BeautifulSoup(r.content, 'html.parser')
    name = str(soup.find_all('span', {'id': 'fb-timeline-cover-name'})[0].string)
    with open('data/{}.txt'.format(profile_id), 'w') as f:
        f.write(name)

    # PICTURE
    url = base_url + profile_id + '/picture?width=9999'
    print('[profile picture url] -> {}'.format(url))
    output_filename = 'data/{}.jpg'.format(profile_id)
    wget.download(url, out=output_filename)
    # http://stackoverflow.com/questions/8574759/getting-full-size-profile-picture
    # http://stackoverflow.com/questions/12827775/facebook-user-url-by-id
    # http://stackoverflow.com/questions/20475552/python-requests-library-redirect-new-url/20475712#20475712


profile = 100000425733973  # Start From Profile ID

while True:
    base_url = 'https://graph.facebook.com/'
    s_index = str(profile)
    file_name = s_index
    # Now download the image. b for binary
    try:
        extract_information(file_name, base_url)
    except AssertionError:
        pass
    profile += 1
