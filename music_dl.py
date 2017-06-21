# 
# imports 
# 
from __future__ import unicode_literals
from datetime import datetime

import os 
import sys 
import errno 
import youtube_dl

#
# creates a folder in the current dir with this format and returns its name
# output : muzika_20171230
#
def create_file():
    date = datetime.now()
    dir_name = date.strftime('muzika_%Y-%m-%d')
    try:
        os.mkdir(dir_name)
        print "[log] directory {} created succesfully".format(dir_name)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass
    return dir_name 

if __name__ == "__main__" : 
    dir_name = create_file()
    yld_options = {
        'format': 'bestaudio/best',
        'outtmpl': dir_name+'/'+'%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }
    ydl = youtube_dl.YoutubeDL(yld_options) 
    for line in sys.argv[1::] :
        try : 
            ydl.download([line])
        except youtube_dl.utils.DownloadError as exc :
            pass
