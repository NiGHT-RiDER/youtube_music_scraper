#!/bin/bash

DATE=$(date +%Y-%m-%d)

DIRTARGET="muzika_$DATE/"

TARTARGET="muzika_$DATE.zip"

zip -r $TARTARGET $DIRTARGET
gdrive upload $TARTARGET
gdrive list | grep $DATE | awk '{print $1}' | xargs  gdrive info | grep DownloadUrl | awk '{print $2}'
gdrive list | grep $DATE | awk '{print $1}' | xargs  gdrive share 

 
