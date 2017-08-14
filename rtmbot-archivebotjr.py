#### rtmbot-archivebotjr.py
#### By Mike Dank (@Famicoman)
#### Version 1.1 (2017-08-14)
#### Slack bot used for archiving material

import os
import pickle
import subprocess
import commands
from rtmbot.core import Plugin

class ArchivebotJrPlugin(Plugin):

	channel = ""
	
	### process_message
	### Boilerplate slack code for channel message processing
	def process_message(self, data):
	    self.channel = data["channel"]
	    text = data["text"]##.encode('ascii','ignore')
	    # Accept tasks on all channels
	    if self.channel.startswith("D") or self.channel.startswith("C"):
	        try:
	            if text.startswith("!youtubedl"):
	                self.cmdYoutubedl(text)
	            elif text.startswith("!uptime"):
	                self.cmdUptime(text)
	            elif text.startswith("!wget"):
	                self.cmdWget(text)
	            elif text.startswith("!torsocks-wget"):
	                self.cmdTorsockswget(text)
	            elif text.startswith("!ping"):
	                self.cmdPing(text)
	        except:
	            print "Error! Attempting recovery..."
	            raise
	
	### sanitize
	### Sanitize the user input, we don't want them to execute any crazy commands
	def sanitize(self, inputStr):
		return inputStr.strip(";|><`'&\\\"")
	
	### logToChannel
	### Log output to the slack channel
	def logToChannel(self, inputStr):
	    self.outputs.append([self.channel, inputStr])
	
	### logToConsole
	### Log output to the local console
	def logToConsole(self, inputStr):
	    print inputStr
	
	### cmdYoutubedl
	### Run youtube-dl on target video, with highest quality
	### This requires a fairly recent build of ffmpeg
	### YOU MUST SET FFMPEG_HOME VARIABLE
	def cmdYoutubedl(self, inputStr):
	    self.logToConsole("[youtube-dl] inputStr: " + inputStr)
	    FFMPEG_HOME = "/home/slackbot/bin"
	    array = inputStr.split(" ")
	    arg = array[1].encode('ascii','ignore').replace('<',"").replace('>',"")
	    if '|' in arg:
	        arg = arg.split('|')[0]
	    arg = arg.replace("https:", "http:")
	    self.logToConsole("[youtube-dl] Using link: " + arg)
	    version = commands.getstatusoutput('youtube-dl --version')
	    self.logToConsole("[youtube-dl] version: " + version[1])
	    self.logToChannel("Version: " + version[1])
	    arg = self.sanitize(arg)
	    log = commands.getstatusoutput("youtube-dl --prefer-ffmpeg --ffmpeg-location " + FFMPEG_HOME + " --title --continue --retries 4 --write-info-json --write-description --write-thumbnail --write-annotations --all-subs --ignore-errors -f bestvideo+bestaudio " + arg)
	    self.logToConsole("[youtube-dl] " + str(log))
	    self.logToChannel(log[1])
	
	### cmdUptime
	### Run the uptime command
	def cmdUptime(self, inputStr):
	    self.logToConsole("[uptime] inputStr: " + inputStr)
	    log = commands.getstatusoutput("uptime")
	    self.logToConsole("[uptime] " + str(log))
	    self.logToChannel(log[1])
	
	### cmdWget
	### Run wget with the continue option	
	def cmdWget(self, inputStr):
	    self.logToConsole("[wget] inputStr: " + inputStr)
	    array = inputStr.split(" ")
	    arg = array[1].replace('<',"").replace('>',"")
	    if '|' in arg:
	        arg = arg.split('|')[0]
	    arg = self.sanitize(arg)
	    log = commands.getstatusoutput("wget -c " + arg)
	    self.logToConsole("[wget] " + str(log))
	    self.logToChannel(log[1])
	
	### cmdTorsockswget
	### Run wget through torsocks
	### YOU MUST HAVE torsocks INSTALLED
	def cmdTorsockswget(self, inputStr):
	    self.logToConsole("[torsocks-wget] inputStr: " + inputStr)
	    array = inputStr.split(" ")
	    arg = array[1].replace('<',"").replace('>',"")
	    if '|' in arg:
	        arg = arg.split('|')[0]
	    arg = self.sanitize(arg)
	    log = commands.getstatusoutput("torsocks wget -c " + arg)
	    self.logToConsole("[torsocks-wget] " + str(log))
	    self.logToChannel(log[1])
	
	### cmdPing
	### Runs IPv4 ping four times on target
	def cmdPing(self, inputStr):
	    self.logToConsole("[ping] inputStr: " + inputStr)
	    array = inputStr.split(" ")
	    arg = array[1].replace('<',"").replace('>',"")
	    if '|' in arg:
	        arg = arg.split('|')[1]
	    arg = self.sanitize(arg)
	    log = commands.getstatusoutput("ping -c 4 " + arg)
	    self.logToConsole("[ping] " + str(log))
	    self.logToChannel(log[1])
