import requests
from bs4 import BeautifulSoup
import json
import argparse



def getChallengeNames(url, uname=None, password=None):

    if uname != None:
        r = requests.session()

        x = r.get(url+'/login')
        soup = BeautifulSoup(x.content,'html.parser')
        nonce = soup.find(id="nonce")
        nonce =  nonce.get('value')
        title = soup.title.contents[0]
        params = (
            ('next', '/api/v1/challenges'),
        )
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'cookie': "session="+str(x.cookies.get_dict()["session"])
        }
        data = {
        'name': uname,
        'password': password,
        '_submit': 'Submit',
        'nonce': nonce,
        }

        response = r.post(url+'/login', params=params, data=data, verify=False)
    else: 
        response = requests.get(url + '/api/v1/challenges')
        x = requests.get(url)
        soup = BeautifulSoup(x.content,'html.parser')
        title = soup.title.contents[0]
        print(title)
    return response.text,title


def parseChallenges(url, username=None, password=None):
    names = []
    pointsList = []
    categoryList = []
    solvesList = []
    solved = []
    tags = []
    if username != None:
        data,title = getChallengeNames(url, username, password)
    else:
        data, title = getChallengeNames(url)
    try:
        data = json.loads(data)
    except Exception:
            print("[!!!] decoding json data, likely a login failure")
            quit()
    for i in data['data']:
        names.append(i['name'])
        if 'value' in i: pointsList.append(i['value'])
        if 'category' in i: categoryList.append(i['category'])
        if 'solves' in i: solvesList.append(i['solves'])
        if 'solved_by_me' in i: solved.append(i['solved_by_me'])
        if 'tags' in i:tags.append(i['tags'])
    return names, pointsList, categoryList, solvesList, solved, tags,title

def writeMarkdown(names, pointsList, categoryList, solvesList, solved, tags,title, description):

    with open('writeup.md','w') as f:
        f.write(f"# {title}\n\n")
        f.write(f"{description}\n\n")
        categories = []
        for i in categoryList:
            if i not in categories:
                categories.append(i)
        for x in categories:
            f.write(f"## {x.capitalize()}\n")
            for n in names:
                if categoryList[names.index(n)] == x:
                    if tags[names.index(n)] != []:  
                            tagsFinal = "\n##### Tags: "
                            for k in tags[names.index(n)]:
                                tagsFinal += f"{k['value']} "
                    else:
                        tagsFinal = ""
                    final = f"### {n} \n#### "
                    if pointsList != []:
                        final += f"Points: {pointsList[names.index(n)]}, "
                    if solvesList != []:
                        final += f"Solves: {solvesList[names.index(n)]}, "
                    if solved != []:
                        final += f"Solved by my Team: {solved[names.index(n)]}\n "
                    final += f"{tagsFinal}\n---\n\n"

                    f.write(final)

def getDesc():
    with open('desc.txt','r') as f:
        desc = ""
        for i in f.readlines():
            desc += f"{str(i).strip()}"
        return desc