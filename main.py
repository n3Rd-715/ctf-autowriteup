from os import write
from scrape_helpers import *
from check_auth_needed import *
import argparse





def main():
    parser = argparse.ArgumentParser(description='Scrape Common CTF Platforms to format for an easy writeup document')
    parser.add_argument('--url', help="The url for the ctf website e.g. http://ctf.testing.io")
    parser.add_argument('--username','-u', help="Your username for the CTF")
    parser.add_argument('--password','-p', help="Your password for the CTF")
    args = parser.parse_args()
    username = args.username
    password = args.password
    URL = args.url
    if check(URL):
        names, pointsList, categoryList, solvesList, solved, tags,title = parseChallenges(URL)
    else:
        names, pointsList, categoryList, solvesList, solved, tags,title = parseChallenges(URL, username, password)
    writeMarkdown(names, pointsList, categoryList, solvesList, solved, tags,title,getDesc())
if __name__ == "__main__":
    main()