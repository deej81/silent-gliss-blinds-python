import requests

def close_wesley_blinds():
    operate_blind(35, 'close')
    operate_blind(31, 'close')

def open_wesley_blinds():
    operate_blind(35, 'open')
    operate_blind(31, 'open')

def operate_blind(mid, action):
    # URL
    url = 'http://192.168.1.39/command.jcf'

    # Headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'http://192.168.1.39',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'http://192.168.1.39/sg-edit-locations.html',
        'Priority': 'u=0'
    }

    # Data
    data = f'command=[{{"action":"{action}","mid":"{mid}"}}]'
    print(data)

    # Sending POST request
    response = requests.post(url, headers=headers, data=data)

    # Print response
    print(response.status_code)
    print(response.text)

open_wesley_blinds()
