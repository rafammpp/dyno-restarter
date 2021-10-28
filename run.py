import requests, os

HEROKU_AUTH_KEY = os.environ.get('HEROKU_AUTH_KEY')
HK_APP_NAME = os.environ.get('HK_APP_NAME')

r = requests.get(f'https://api.heroku.com/apps/{HK_APP_NAME}/dynos', headers={
    'Content-Type': 'application/json',
    'Accept': 'application/vnd.heroku+json; version=3',
    'Authorization': f'Bearer {HEROKU_AUTH_KEY}',
})

dyno_list = r.json()
print(dyno_list)

dyno = sorted(dyno_list, key=lambda d: d['updated_at'])[0]
print('dyno to restart:', dyno["name"])
r = requests.delete(f'https://api.heroku.com/apps/{HK_APP_NAME}/dynos/{dyno["name"]}')

if r.ok:
    print('OK!!')
else:
    print(r)
