# Mining into Facebook public profiles with Deep Learning
Applying Deep Learning to Facebook public information to extract interesting patterns

<i>Nothing very precise yet. We're just going to have fun and build a big Facebook dataset in the short term!</i>

## How to use it?

Install the latest `facebook-sdk`.
```
cd /tmp/
git clone git@github.com:mobolic/facebook-sdk.git
cd facebook-sdk
sudo pip3 install .
```

Then clone this repository and follow the instructions below.
```
# For Python 3.x
git clone git@github.com:philipperemy/Facebook-Profile-Deep-Learning.git facebook-explorer
cd facebook-explorer
sudo pip3 install -r requirements.txt
cp credentials.json.example credentials.json
vim credentials.json # Get your Token ID here https://developers.facebook.com/tools/explorer/
python3 profile_miner.py 10 # to start mining facebook profiles. Here we use 10 threads to query Facebook.
```

## Facebook Token ID

https://developers.facebook.com/tools/explorer/

## Scan data

```
python3 scan_data.py
```

```
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

Example of a public profile (contained in `###.pkl` where `###` is the ID of the user. The ID is undisclosed here for privacy reasons):
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
The corresponding profile picture is located in `###.jpg`.

## Common errors

Sometimes the profile is there but it's not available in the Graph API. Most of the time, the profile is inactive and it's better to move on, rather than raising an exception that would block the script:
```
INFO:facebook-deep-learning:Unsupported get request. Object with ID '827435111' does not exist, cannot be loaded due to missing permissions, or does not support this operation. Please read the Graph API documentation at https://developers.facebook.com/docs/graph-api
```
