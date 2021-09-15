import requests
import argparse
def check(url):

    r = requests.get(url + '/api/v1/challenges', allow_redirects=False)
    if r.status_code == 302:
        print(f"[*] Login Needed to Access Challenge API")
        return False
    elif r.status_code == 200:
        print(f"[+] No login needed")
        return True
    else:
        print(f"[!!!] Error, Please Check if the Challenge API Is at the correct path")
        return False