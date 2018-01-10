import urllib.request
from bs4 import BeautifulSoup

class Fetchy(object):
	
	def __init__(self, address):
		self.address = address

	def gotta_get_texty(self):
		url = self.address
		html = urllib.request.urlopen(url).read()
		soup = BeautifulSoup(html, "html.parser")
		[s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
		clean_text = soup.get_text()
		file = open("input_markov_chain.txt","w")
		file.write(clean_text)
		file.close()
		print("File with clean text created")
		return "input_markov_chain.txt"
	