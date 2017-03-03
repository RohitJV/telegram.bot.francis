import urllib
from bs4 import BeautifulSoup
import random

xkcd_lim = 1171
cnh_lim = 4278

def getXkcdImageUrl():
	webpage = urllib.urlopen("https://www.xkcd.com/"+str(random.randint(1,xkcd_lim)));
	soup = BeautifulSoup(webpage, "html.parser");
	print soup;
	for div in soup.find_all('div'):
		if(div.get("id")=="comic"):
			for imgtag in div.find_all('img'):
				print "Found";
				return(imgtag.get("src"));

def getCnhImageUrl():
	webpage = urllib.urlopen("https://www.explosm.net/comics/"+str(random.randint(1,cnh_lim)));
	soup = BeautifulSoup(webpage, "html.parser");
	for imgtag in soup.find_all('img'):
		if(imgtag.get("id")=="main-comic"):
			return(imgtag.get("src"));


