import requests
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup
from urllib3.util.retry import Retry
import spacy
from spellchecker import SpellChecker
spell = SpellChecker(language='fr')
nlp =spacy.load('fr_core_news_md')


session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

URL = 'https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/French_wordlist_opensubtitles_5000'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find_all('span', class_ = 'Latn') #Pulls all words

result_content = ''

for result in results:
    result_content =result_content + result.text + '\n' #All the words in a string separated by \n

resultLemmaobj = nlp(result_content) #Prepares string for lemmatization 

resultLemma = ''
for token in resultLemmaobj:
    lemma = spell.correction(token.lemma_)
    if type(lemma) == str:
        resultLemma = resultLemma + lemma + '\n' #Lemmatizes the words and saves them into a string separated by \n

words = resultLemma.split() #Splits the string into a list based on \n
resultLemmaUnduplicate = " ".join(sorted(set(words), key=words.index)) #Deletes duplicate words. key=words.index ensures that the original ordering is preserved.
resultLemmaUnduplicate1 = resultLemmaUnduplicate.split() #Re-lists the words, separated by spaces
resultLemmaUnduplicate = ''
for token in resultLemmaUnduplicate1:
    resultLemmaUnduplicate = resultLemmaUnduplicate + token + '\n' #Converts into a string

with open('', 'w') as f: #Insert your desired path
    f.write(resultLemmaUnduplicate) #Writes to text file








