# ctf-autowriteup

A scraper to automatically format a writeup markdown document for common CTF platforms
_Currently only works on CTFd platforms, i am planning to expand to the HackTheBox ctf platform and the PicoCTF platform next. DM me on twitter if you have any other suggestions_

# Installation/Usage
```bash
$ pip3 install -r requirements.txt

$ python3 main.py -h

# usage: main.py [-h] [--url URL] [--username USERNAME] [--password PASSWORD]

# Scrape Common CTF Platforms to format for an easy writeup document

# optional arguments:
#  -h, --help            show this help message and exit
#  --url URL             The url for the ctf website e.g. http://ctf.testing.io
#  --username USERNAME, -u USERNAME
#                        Your username for the CTF
#  --password PASSWORD, -p PASSWORD
#                        Your password for the CTF

```
Your overarching statement about the CTF should be placed in the `desc.txt` file.
