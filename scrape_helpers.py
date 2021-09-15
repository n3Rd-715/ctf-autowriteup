import requests
from bs4 import BeautifulSoup
import json
import argparse



def getChallengeNames(url, uname, password):

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
    return response.text,title


def parseChallenges(url, username, password):
    names = []
    pointsList = []
    categoryList = []
    solvesList = []
    solved = []
    tags = []

    data,title = getChallengeNames(url, username, password)
    data = json.loads(data)
    for i in data['data']:
        names.append(i['name'])
        pointsList.append(i['value'])
        categoryList.append(i['category'])
        solvesList.append(i['solves'])
        solved.append(i['solved_by_me'])
        tags.append(i['tags'])
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
                            tagsFinal = "##### Tags: "
                            for k in tags[names.index(n)]:
                                tagsFinal += f"{k} "
                    else:
                        tagsFinal = ""
                    f.write(f"### {n}\n #### Points: {pointsList[names.index(n)]}, Solves: {solvesList[names.index(n)]}, Solved by my Team: {solved[names.index(n)]}\n {tagsFinal}\n---\n\n")

def getDesc():
    with open('desc.txt','r') as f:
        desc = ""
        for i in f.readlines():
            desc += f"{str(i).strip()}"
        print(desc)
        return desc