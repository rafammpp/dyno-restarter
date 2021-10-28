# Dyno restarter
This script restart the eldest dyno of a given app. This prevents memory leaks without affecting performance much.

## Requirements
python 3.6
requests

## Instructions
Set this env vars:

HEROKU_AUTH_KEY, go to [https://dashboard.heroku.com/account](https://dashboard.heroku.com/account) and copy the API Key
HK_APP_NAME

Run the script:
`python restart-dyno.py`

## Optional: Set this up in Heroku
1. Create an app.
2. Push this repository. 
3. Set Heroku Scheduler addon. 
4. Add a job every hour (for example) and type the command `python restart-dyno.py`.