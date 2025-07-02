# frenchVocabFrequencyListLemmatized
A lemmatized French vocabulary list sourced from [https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/French_wordlist_opensubtitles_5000](https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/French/OpenSubtitles_Top_20K). 

I first tried using `spacy` to lemmatize but it was absolutely awful. I have since switched to using `stanza`, which is not perfect but much better. Then, I use `Spellchecker` to fix spelling mistakes that `stanza` may create.

Alternatively, you may want to lemmatize algorithmically by pulling redirects from wiktionary. 
