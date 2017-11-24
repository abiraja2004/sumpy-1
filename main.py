
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import requests

from gensim.summarization import summarize
from gensim.summarization import keywords

###

text = requests.get('http://rare-technologies.com/the_matrix_synopsis.txt').text


#print ('Input text:')
#print (text)


print ('\n \n Summary:')
print (summarize(text, ratio = 0.01))

print('Keywords:')
#print(keywords(text))
