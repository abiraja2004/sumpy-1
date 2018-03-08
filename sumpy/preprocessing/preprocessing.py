import spacy
from spacy.lang.en import English

class Preprocessing:

    def __init__(self, path="", text=""):
        """
        Returns an object with preprocessed data.

        self._text = plain no processed text
        self._text_read = spacy preprocessed text
        TODO:
            - add options to not use the stemmer and the lemmatizer in order to perform experiments on the dataset
            - add multilingual support
        Args:
            path: string with the path containing the data to be used

        Returns:
            A Preprocessing object that can return lemmatized file, tokens or plain taxt

        Raises:
            FileNotFoundError
        """

        if path is not "" and text is not "":
            print('Error! Only one between file path and text must be provided')
            exit(1)

        eng = spacy.load('en', disable=['ner'])
        tokenizer = English().Defaults.create_tokenizer(eng)

        if path is not "":
            try:
                with open(path, 'r') as f:
                    self._text_read = f.read()
                    self._text = eng(self._text_read)

            except FileNotFoundError:
                print('Can\'t access the file specified by', path,
                        ', please provide a valide path')

        else:
            self._text_read = text
            self._text = eng(text)

        self._doc = tokenizer(self._text_read)  # spacy-doc object
                                                # with preprocessed file

    def get_text(self):
        return self._text_read

    def get_tokens(self):
        final = []
        for tokens in self._doc:
             final.append(tokens)
        return final

    def get_lemmas(self):
        """
        Shows all the lemmas for the given text.

        a Doc objects contain multiple tokens, each has multiple properties
        e.g. lemma property has a number as index for the element in a spacy vocab
        the lemma_ property has the string representation for it
        """
        final = []
        for tokens in self._doc:
            final.append(tokens.lemma_)
        return final

    def show_dep(self):
        final = []
        #for tokens in self._doc:
        #    print(tokens.)i

        for chunk in self._doc.noun_chunks:
            print(chunck.head)


    def show_pos(self):
        for tokens in self._text:
            print('token: ', tokens.text, '| pos: ', tokens.pos_,
                    '| istagged: ', self._text.is_tagged)

text = '''The screen is filled with green, cascading code which gives way to the title, The Matrix. A phone rings and text appears on the screen: "Call trans opt: received. 2-19-98 13:24:18 REC: Log>" As a conversation takes place between Trinity (Carrie-Anne Moss) and Cypher (Joe Pantoliano), two free humans, a table of random green numbers are being scanned and individual numbers selected, creating a series of digits not unlike an ordinary phone number, as if a code is being deciphered or a call is being traced. Trinity discusses some unknown person. Cypher taunts Trinity, suggesting she enjoys watching him. Trinity counters that "Morpheus (Laurence Fishburne) says he may be 'the One'," just as the sound of a number being selected alerts Trinity that someone may be tracing their call. She ends the call. Armed policemen move down a darkened, decrepit hallway in the Heart O' the City Hotel, their flashlight beam bouncing just ahead of them. They come to room 303, kick down the door and find a woman dressed in black, facing away from them. It's Trinity. She brings her hands up from the laptop she's working on at their command. Outside the hotel a car drives up and three agents appear in neatly pressed black suits. They are Agent Smith (Hugo Weaving), Agent Brown (Paul Goddard), and Agent Jones (Robert Taylor). Agent Smith and the presiding police lieutenant argue. Agent Smith admonishes the policeman that they were given specific orders to contact the agents first, for their protection. The lieutenant dismisses this and says that they can handle "one little girl" and that he has two units that are bringing her down at that very moment. Agent Smith replies: "No, Lieutenant. Your men are already dead." Inside, Trinity easily defeats the six policemen sent to apprehend her, using fighting and evasion techniques that seem to defy gravity. She calls Morpheus, letting him know that the line has been traced, though she doesn't know how. Morpheus informs her that she will have to "make it to another exit," and that Agents are heading up after her. '''

path = '2.abstr'
a = Preprocessing(text = text)
tok = a.get_tokens()
#print(tok)
lem = a.get_lemmas()
#print(lem)
print(a.show_dep())

