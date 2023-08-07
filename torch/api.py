import requests
import subprocess
import json

# Amazon API
AMAZON = 'https://checkip.amazonaws.com/'

SOCKS_PORT = 49050
proxies = {'http': f"socks5h://localhost:{SOCKS_PORT}",
           'https': f"socks5h://localhost:{SOCKS_PORT}"}


def get_info_from_ip_api(direct=False):
    url = 'http://ip-api.com/json/'
    response = ''
    if direct:
        response = requests.get(url, verify=True)
    else:
        response = requests.get(url, verify=True, proxies=proxies)

    if response.status_code != 200:
        return 'N/A', 'N/A'
    data = response.json()
    return data['query'], data['country']


def get_country(ip):
    if ip == 'N/A':
        return ip
    url = f'https://api.country.is/{ip}'
    response = requests.get(url, verify=True)
    if response.status_code != 200:
        return f'N/A'
    data = response.json()
    return data['country']


def get_info_from_ipify_req(direct=False):
    url = 'https://api.ipify.org?format=json'
    ip = 'N/A'
    try:
        if direct:
            response = requests.get(url)
            ip = response.json()['ip']
        else:
            response = requests.get(url, proxies=proxies)
            ip = response.json()['ip']
    except Exception:
        pass
    return ip, get_country(ip)


def get_info_from_ipify_curl(direct=False):
    url = 'https://api.ipify.org?format=json'
    ip = 'N/A'
    try:
        if direct:
            response = subprocess.run(["curl", url],  check=True, capture_output=True)
            ip = json.loads(response.stdout.decode('UTF-8'))['ip']
        else:
            response = subprocess.run(["curl", "--socks5", f"127.0.0.1:{SOCKS_PORT}", url],  check=True, capture_output=True)
            ip = json.loads(response.stdout.decode('UTF-8'))['ip']
    except Exception:
        pass
    return ip, get_country(ip)


def get_info(direct=False, api='ip-api', tool='request'):
    if api == 'ip-api':
        return get_info_from_ip_api(direct)
    if api == 'ipify':
        if tool == 'request':
            return get_info_from_ipify_req(direct)
        elif tool == 'curl':
            return get_info_from_ipify_curl(direct)
    return 'bad arg', 'bad arg'
