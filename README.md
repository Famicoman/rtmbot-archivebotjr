rtmbot-archivebotjr
================

Slack bot plugin to offer downloading/archiving utilities through slack

**Written in python**

Using slackapi/python-rtmbot
Using python 2.7.3

Visit https://github.com/slackapi/python-rtmbot for python-rtmbot info

## Installation

Install pip, then install rtmbot

	sudo easy_install pip
	sudo pip install rtmbot

Make a project folder for your rtmbot instance

	mkdir ~/rtmbot
	cd ~/rtmbot

Make a plugins directory and touch an init module

	mkdir plugins
	touch plugins/__init__.py

Clone this repo and copy rtmbot-archivebotjr.py to your plugins directory

	git clone https://github.com/Famicoman/rtmbot-archivebotjr.git
	cp rtmbot-archivebotjr/rtmbot-archivebotjr.py plugins/rtmbot-archivebotjr.py

Edit your rtmbot.conf to become aware of the new plugin

	nano rtmbot.conf

It should look similar to the below

	DEBUG: True # make this False in production
 	SLACK_TOKEN: "xoxb-your-token"
 	ACTIVE_PLUGINS:## Usage
	    - plugins.rtmbot-archivebotjr.ArchivebotJrPlugin

## Usage

Start rtmbot normally within your project folder

	cd ~/rtmbot
	rtmbot

Check logs if necessary

	tail -f ~/rtmbot/rtmbot.log

## Commands (entered into slack channel)

	!uptime

Run uptime

	!ping <address>

Run IPv4 ping.

	!wget <url>

Run wget with continue option.

	!torsocks-wget <url>

Run wget through torsocks, you can download files on onion sites. You must have torsocks installed!

	!youtube-dl <url>

Run youtube-dl on target video, with highest quality. You must have youtube-dl installed!

