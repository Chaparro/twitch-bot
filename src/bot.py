"""
Simple IRC Bot for Twitch.tv

Developed by Aidan Thomson <aidraj0@gmail.com>
Fork by Ricardo Chaparro <https://github.com/Chaparro>
"""

import lib.irc as irc_
from lib.functions_general import *

class Dreambot:

	def __init__(self, config):
		self.config = config
		self.irc = irc_.irc(config)
		self.socket = self.irc.get_irc_socket_object()


	def run(self):
		irc = self.irc
		sock = self.socket
		config = self.config

		while True:
			data = sock.recv(config['socket_buffer_size']).rstrip()

			if len(data) == 0:
				pp('Connection was lost, reconnecting.')
				sock = self.irc.get_irc_socket_object()

			if config['debug']:
				print data

			# check for ping, reply with pong
			irc.check_for_ping(data)

			if irc.check_for_message(data):
				message_dict = irc.get_message(data)

				channel = message_dict['channel']
				message = message_dict['message']
				username = message_dict['username']

				if 'ssbm_dream' in username:
					username = 'drim'

				ppi(channel, message, username)
				say(username,message)
