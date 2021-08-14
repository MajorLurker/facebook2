import json
import facebook
import datetime
from accessfile import dailyupdate
from configparser import ConfigParser


file = 'config.ini'
config = ConfigParser()
config.read(file)
message1 = config['messages']['message1']
message2 = config['messages']['message2']
general_message = config['messages']['general']
contact = config['messages']['contact']
contact2 = config['messages']['contact2']
contact3 = config['messages']['contact3']
twitter = config['contact']['twitter']
email = config['contact']['email']
website = config['contact']['website']

now = datetime.date.today()
tomorrow = now + datetime.timedelta(days=1)
tomorrow = tomorrow.strftime("%A")
date_tomorrow = now + datetime.timedelta(days=1)
date_tomorrow = date_tomorrow.strftime("%d %B %Y")


print(tomorrow)


def read_creds(filename):
    '''
    Store API credentials in a safe place.
    If you use Git, make sure to add the file to .gitignore
    '''
    with open(filename) as f:
        fb_credentials = json.load(f)
    return fb_credentials


show = dailyupdate(tomorrow)
shows = "\n". join(show)

display = (message1 + " " + tomorrow + " " + date_tomorrow + " are: \n\n"
           + shows + "\n\n" + message2 + "\n" + general_message + "\n" + contact + " "
           + twitter + " " + contact2 + " " + email + '\n' + contact3 + " " + website)

print(display)

credentials = read_creds('credentials.json')
fb = facebook.GraphAPI(access_token=credentials['access_token'])

fb.put_object("me", "feed", message=display)
