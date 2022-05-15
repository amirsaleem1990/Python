#!/usr/bin/python3
# https://stackoverflow.com/questions/50197643/youtbe-dl-multiple-downloads-at-the-same-time
import multiprocessing.dummy
import subprocess

arr = []
for i in open("mp4.txt", "r").read().splitlines():
    arr.append({'url' : i})

def download(v):
    subprocess.check_call([
        'youtube-dl', v['url']])
p = multiprocessing.dummy.Pool()
p.map(download, arr)
 