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
results = soup.find_all('span', class_ = 'Latn')

result_content = ''

for result in results:
    result_content =result_content + result.text + '\n'

with open('C:/Users/Computer/Downloads/Python Scripts/FrenchWordsBeforeLemmatization.txt', 'w') as f:
    f.write(result_content)

resultLemmaobj = nlp(result_content)

resultLemma = ''
for token in resultLemmaobj:
    lemma = spell.correction(token.lemma_)
    if type(lemma) == str:
        resultLemma = resultLemma + lemma + '\n'

with open('C:/Users/Computer/Downloads/Python Scripts/FrenchWordsAfterLemmatization.txt', 'w') as f:
    f.write(resultLemma)

words = resultLemma.split()
resultLemmaUnduplicate = " ".join(sorted(set(words), key=words.index))
resultLemmaUnduplicate1 = resultLemmaUnduplicate.split()
resultLemmaUnduplicate = ''
for token in resultLemmaUnduplicate1:
    resultLemmaUnduplicate = resultLemmaUnduplicate + token + '\n'

with open('C:/Users/Computer/Downloads/Python Scripts/FrenchWordsAfterFilter.txt', 'w') as f:
    f.write(resultLemmaUnduplicate)








