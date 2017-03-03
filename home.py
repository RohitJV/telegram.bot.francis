import sys
import time
import telepot
import json
import random
import urllib
from pprint import pprint

from FComics import getXkcdImageUrl
from FComics import getCnhImageUrl

bot = telepot.Bot('335510254:AAEd_Rkt7uARSPwHRrroVcr-uMeDAg0hFC4');

def comic(msg):
	content_type, chat_type, chat_id = telepot.glance(msg);
	txtMsg = msg["text"];
	if("xkcd" in txtMsg):
		try:
			f = urllib.urlopen('https:'+getXkcdImageUrl());
			show_keyboard = {'keyboard': [['More xkcd comics!'],["Cyanide and Happiness!"]], "one_time_keyboard": True};
			bot.sendPhoto(chat_id, ('xkcd.jpg', f), reply_markup=show_keyboard);
		except:
			bot.sendMessage(chat_id, "Error in retriving comic");
	elif(("cnh" in txtMsg) or ("Cyanide" in txtMsg)):
		try:			
			f = urllib.urlopen('https:'+getCnhImageUrl());
			show_keyboard = {'keyboard': [["More Cyanide and Happiness!"],["xkcd comics!"]], "one_time_keyboard": True};
			bot.sendPhoto(chat_id, ('cnh.jpg', f), reply_markup=show_keyboard);
		except:
			bot.sendMessage(chat_id, "Error in retriving comic");

def handle_text(msg):
	content_type, chat_type, chat_id = telepot.glance(msg);
	txtMsg = msg["text"];
	if( ("xkcd" in txtMsg) or ("cnh" in txtMsg) or ("Cyanide" in txtMsg)):
		bot.sendChatAction(chat_id, "upload_photo");
		comic(msg);
	else:
		bot.sendMessage(chat_id, msg["text"]);

def handle_message(msg):
	# pprint(msg);
	content_type, chat_type, chat_id = telepot.glance(msg);
	print(content_type, chat_type, chat_id);
	if content_type == "text":		
		handle_text(msg);

def main():
	print("Starting Bot...\n\n");
	print(bot.getMe());
	print("\n\n...............................\n\n");
	# Keep the program running.
	while 1:
	    time.sleep(10)

bot.message_loop(handle_message);

if __name__ == "__main__":
	main()
