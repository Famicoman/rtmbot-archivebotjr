#### rtmbot-archivebotjr.py
#### By Mike Dank (@Famicoman)
#### Version 1.0 (2016-02-15)
#### Slack bot used for archiving material

import os
import pickle
import subprocess
import commands

outputs = []

### process_message
### Boilerplate slack code for channel message processing
def process_message(data):
    channel = data["channel"]
    text = data["text"]##.encode('ascii','ignore')
    # Accept tasks on all channels
    if channel.startswith("D") or channel.startswith("C"):
        try:
            if text.startswith("!youtubedl"):
                cmdYoutubedl(text)
            elif text.startswith("!uptime"):
                cmdUptime(text)
            elif text.startswith("!wget"):
                cmdWget(text)
            elif text.startswith("!torsocks-wget"):
                cmdTorsockswget(text)
            elif text.startswith("!ping"):
                cmdPing(text)
        except:
            print "Error! Attempting recovery..."
            raise

### sanitize
### Sanitize the user input, we don't want them to execute any crazy commands
def sanitize(inputStr):
	return inputStr.strip(";|><`'&\\\"")

### logToChannel
### Log output to the slack channel
def logToChannel(inputStr):
    outputs.append([channel, inputStr])

### logToConsole
### Log output to the local console
def logToConsole(inputStr):
    print inputStr

### cmdYoutubedl
### Run youtube-dl on target video, with highest quality
### This requires a fairly recent build of ffmpeg
### YOU MUST SET FFMPEG_HOME VARIABLE
def cmdYoutubedl(inputStr):
    logToConsole("[youtube-dl] inputStr: " + inputStr)
    FFMPEG_HOME = "/home/slackbot/bin"
    array = inputStr.split(" ")
    arg = array[1].encode('ascii','ignore').replace('<',"").replace('>',"")
    if '|' in arg:
        arg = arg.split('|')[0]
    arg = arg.replace("https:", "http:")
    logToConsole("[youtube-dl] Using link: " + arg)
    version = commands.getstatusoutput('youtube-dl --version')
    logToConsole("[youtube-dl] version: " + version[1])
    logToChannel("Version: " + version[1])
    arg = sanitize(arg)
    log = commands.getstatusoutput("youtube-dl --prefer-ffmpeg --ffmpeg-location " + FFMPEG_HOME + " --title --continue --retries 4 --write-info-json --write-description --write-thumbnail --write-annotations --all-subs --ignore-errors -f bestvideo+bestaudio " + arg)
    logToConsole("[youtube-dl] " + log)
    logToChannel(log[1])

### cmdUptime
### Run the uptime command
def cmdUptime(inputStr):
    logToConsole("[uptime] inputStr: " + inputStr)
    log = commands.getstatusoutput("uptime")
    logToConsole("[uptime] " + log)
    logToChannel(log[1])

### cmdWget
### Run wget with the continue option	
def cmdWget(inputStr):
    logToConsole("[wget] inputStr: " + inputStr)
    array = inputStr.split(" ")
    arg = array[1].replace('<',"").replace('>',"")
    if '|' in arg:
        arg = arg.split('|')[0]
    arg = sanitize(arg)
    log = commands.getstatusoutput("wget -c " + arg)
    logToConsole("[wget] " + log)
    logToChannel(log[1])

### cmdTorsockswget
### Run wget through torsocks
### YOU MUST HAVE torsocks INSTALLED
def cmdTorsockswget(inputStr):
    logToConsole("[torsocks-wget] inputStr: " + inputStr)
    array = inputStr.split(" ")
    arg = array[1].replace('<',"").replace('>',"")
    if '|' in arg:
        arg = arg.split('|')[0]
    arg = sanitize(arg)
    log = commands.getstatusoutput("torsocks wget -c " + arg)
    logToConsole("[torsocks-wget] " + log)
    logToChannel(log[1])

### cmdPing
### Runs IPv4 ping four times on target
def cmdPing(inputStr):
    logToConsole("[ping] inputStr: " + inputStr)
    array = inputStr.split(" ")
    arg = array[1].replace('<',"").replace('>',"")
    if '|' in arg:
        arg = arg.split('|')[1]
    arg = sanitize(arg)
    log = commands.getstatusoutput("ping -c 4 " + arg)
    logToConsole("[ping] " + log)
    logToChannel(log[1])
