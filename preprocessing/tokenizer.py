import spacy
from spacy.lang.en import English

eng = spacy.load('en', disable=['parser', 'tagger', 'ner'])

tokenizer = English().Defaults.create_tokenizer(eng)
doc = tokenizer(u'This were my houses')

for tokens in doc:
    print('token: ', tokens, 'lemma: ', tokens.lemma_)
