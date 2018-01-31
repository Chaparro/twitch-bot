==========

This is a simple Twitch chat/irc bot written in python, with added TTS support using Microsoft Speech API 5.3 for playback/broadcasting of Text-To-Speech messages.


Install and Configure
============
* Open up your terminal/shell of choice.
* Install the [http://docs.python-requests.org/en/latest/](Requests library) if you haven't already using `pip install requests`. I tested this application on Python 2.7.5.
* Clone the Git repository.

* Move config/config_example.py to config/config.py. Replace all of the placeholders there with your own username/oauth token/channels to join etc (tips are given in the file).


* Type `chmod +x /serve.py`. To run, you simply need to execute the file by typing `./serve.py`.


When running, the bot will log all text messages to console and speak them using Microsoft Speech Engine.


*TODO
============
- Implement queue
- Directory of replaceable usernames/messages, for fun.