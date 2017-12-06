import spacy
from spacy.lang.en import English

class Preprocessing:

    def __init__(self, path):
        """
        Returns an object with preprocessed data.

        It holds  an object that contains the dataset lemmatized and stemmatized.

        TODO:
            - add options to not use the stemmer and the lemmatizer in order to perform experiments on the dataset
            - add multilingual support
            - handle FileNotFoundError when opening file
        Args:
            path: string with the path containing the data to be used

        Returns:
            Nothing

        Raises:
            FileNotFoundError
        """

        eng = spacy.load('en', disable=['parser', 'ner'])
        tokenizer = English().Defaults.create_tokenizer(eng)

#        tagger = Tagger(eng)
        """ TODO tagger not working yet """

        self._path = path

        try:
            with open(path, 'r') as f:
                self._doc = tokenizer(f.read())     # spacy-doc object with preprocessed file
        except FileNotFoundError:
            print('Can\'t access the file specified by', path,
                    ', please provide a valide path')
            exit(1)


    def show_lemmas(self):
        """
        Shows all the lemmas for the given text.

        a Doc objects contain multiple tokens, each has multiple properties
        e.g. lemma property has a number as index for the element in a spacy vocab
        the lemma_ property has the string representation for it
        """

        for tokens in self._doc:
            print('Lemma: ', tokens.lemma_)

    def show_tokens(self):
        for tokens in self._doc:
            print('token: ', tokens)

    def show_pos(self):
        for tokens in self._doc:
            print('token: ', tokens, '| pos: ', tokens.pos_,
                    '| istagged: ', self._doc.is_tagged)

    def show_text(self):
        with open(self._path, 'r') as f:
            print(f.read())


path = '2.abstr'
a = Preprocessing(path)
#a.show_tokens()
#a.show_lemmas()
#a.show_text()
a.show_pos()

