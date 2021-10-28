import requests, os, logging

HEROKU_AUTH_KEY = os.environ.get('HEROKU_AUTH_KEY')
HK_APP_NAME = os.environ.get('HK_APP_NAME')

if not HEROKU_AUTH_KEY:
    logging.error('HEROKU_AUTH_KEY enviroment var is required')
if not HK_APP_NAME:
    logging.error('HK_APP_NAME enviroment var is required')

if not HEROKU_AUTH_KEY or not HK_APP_NAME: exit(-1)

r = requests.get(f'https://api.heroku.com/apps/{HK_APP_NAME}/dynos', headers={
    'Content-Type': 'application/json',
    'Accept': 'application/vnd.heroku+json; version=3',
    'Authorization': f'Bearer {HEROKU_AUTH_KEY}',
})
if not r.ok:
    logging.error(f"API ERROR: HTTP_{r.status_code} {r.json()['message']}")
    exit(-1)

dyno_list = r.json()
try:
    dyno = sorted(dyno_list, key=lambda d: d['updated_at'])[0]
except KeyError:
    logging.error('Malformed json, updated_at key is not present')
    exit(-1)
except IndexError:
    logging.error(f'There are no dynos running for {HK_APP_NAME} app.')
    exit(-1)

r = requests.delete(f'https://api.heroku.com/apps/{HK_APP_NAME}/dynos/{dyno["name"]}', headers={
    'Content-Type': 'application/json',
    'Accept': 'application/vnd.heroku+json; version=3',
    'Authorization': f'Bearer {HEROKU_AUTH_KEY}',
})

if r.ok:
    print(f'Dyno {dyno["name"]} of {HK_APP_NAME} restarted.')
else:
    logging.error(r.json()['message'])
