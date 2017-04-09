# Mining into Facebook public profiles with Deep Learning
Applying Deep Learning to Facebook public information to extract interesting patterns

<i>Nothing very precise yet. We're just going to have fun and build a big Facebook dataset in the short term!</i>

<div align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/F_icon.svg/2000px-F_icon.svg.png" width="200"><br><br>
</div>



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

### Manual update
Get your Facebook Token ID here and load it into your `credentials.json` file.
https://developers.facebook.com/tools/explorer/

### Automatic update (much more useful)

Before using the automatic updates, make sure that it worked at least one time with the manual procedure (just above). Browse on https://developers.facebook.com/tools/explorer/ and request a Token ID. This part relies on web scraping. If everything is not correctly set up beforehand, it is very likely to fail.

Once it's done, let's start this server that will automatically ask Facebook servers for a new token. The main script `profile_miner.py` auto detects when the token expires. When this happens, a call is made to the server started by `auto_token_generator.py`.

Start the server with this command:
```
export FB_EMAIL=john.appleseed@apple.com FB_PASS='i_love_apple';python3 auto_token_generator.py
```
Where `FB_EMAIL` is your Facebook email address and `FB_PASS` is your Facebook password. I advise you to create a specific Facebook account just for those tasks.

You can check if the server is responding by running this command:

```
curl http://localhost:5000/
```

Or just connecting to http://localhost:5000/ from your favorite browser.


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

The token is only valid for one hour. If you guys have a better way to extend the expiration date, I'll be happy to hear!
```
facebook.GraphAPIError: Error validating access token: Session has expired on Saturday, 08-Apr-17 23:00:00 PDT. The current time is Saturday, 08-Apr-17 23:01:30 PDT.
```

The GraphAPI has implemented user request limits. From my experience it's something like 10,000 calls per hour. But it seems to depend upon the application. It's a very gross rule of thumb. When it happens, the script is put on hold for one hour before resuming.
```
INFO:facebook-deep-learning:(#17) User request limit reached
```
