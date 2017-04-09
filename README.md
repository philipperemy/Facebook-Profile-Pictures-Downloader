# Mining into Facebook public profiles with Deep Learning
Applying Deep Learning to Facebook public information to extract interesting patterns

<i>Nothing very precise yet. We're just going to have fun and build a big Facebook dataset in the short term!</i>

## How to use it?

```
# For Python 3.x
git clone git@github.com:philipperemy/Facebook-Profile-Deep-Learning.git facebook-explorer
cd facebook-explorer
sudo pip3 install -r requirements.txt
cp credentials.json.example credentials.json
vim credentials.json # Get your Token ID here https://developers.facebook.com/tools/explorer/
python3 profile_miner.py # to start mining facebook profiles.
```

## Facebook Token ID

https://developers.facebook.com/tools/explorer/

## Scan data

```
python3 scan_data.py
This scripts refreshes every 10 seconds.
--------------------------------------------------------------------------------
Number of Facebook descriptions : 15097 (+15097)
Number of Facebook images       : 15088 (+15088)
--------------------------------------------------------------------------------
Number of Facebook descriptions : 15104 (+7)
Number of Facebook images       : 15096 (+8)
--------------------------------------------------------------------------------
Number of Facebook descriptions : 15115 (+11)
Number of Facebook images       : 15107 (+11)
```

```
{
 'first_name': 'Susan', 
 'updated_time': '2016-12-28T16:26:46+0000', 
  'last_name': 'Cothran', 
  'link': 'https://www.facebook.com/app_scoped_user_id/###/', 
  'name': 'Susan Cothran', 
  'id': '###'
}
```
`###` is the ID of the user (undisclosed here for privacy reasons). The corresponding profile pictures is `###.jpg` in the same folder.
