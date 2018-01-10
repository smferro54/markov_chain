from markov_python.cc_markov import MarkovChain
from fetch_data import Fetchy

#Request website from where you want to fetch data
website = "http://www." + input("From which website do you want to fetch text?: http://www.")
website = Fetchy(website)
clean_text_file = website.gotta_get_texty()
mc = MarkovChain()
mc.add_file(clean_text_file)
print(mc.generate_text())