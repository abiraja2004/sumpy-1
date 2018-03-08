
import argparse
import networkx as nx

"""

python main.py

* won't be implemented in alpha version

[-r] [--remove stopwords]

[-k] [--keywords]

    [window = between 2 and 10]

    * -sim = k [add link if cos similarity between two words is >= k
[-s] [--summary]

    [-l] [--lemmatize]

    [-p] [--pos]

    * [similarity = common_words | cosine ...]

    * [-v] [--visualize]

    * [ratio = integer]

pagerank visualization python library: https://graph-tool.skewed.de/static/doc/centrality.html#graph_tool.centrality.pagerank

http://www.graphviz.org/gallery/

"""


def check_args(opt):
    return True

def parse_cmdline():
    parser = argparse.ArgumentParser(description='Run automatic keywords extraction or extractive summarizer')

    parser.add_argument('-f', '--file',  type=argparse.FileType('r'))

    group = parser.add_mutually_exclusive_group()

    group.add_argument('--keywords', action = 'store_true', default = False,
                        help = 'preforming kwywords extraction task')

    group.add_argument('--summary', action = 'store_true', default = False,
                        help = 'performing sentence extraction/summarization task')

    parser.add_argument('-n', '--no_stopwords', action = 'store_true',
                        default = False, help = 'removing stopwords from input text')

    parser.add_argument('-w', '--window', default = 2, type=int,
                        help = 'window size to create' +
                        ' link between keywords')


    parser.add_argument('-l', '-lemmatize', action = 'store_true', default = False,
                        help= 'lemmatizing input text')

    parser.add_argument('-p', '--pos', action = 'store_true', default = False,
                        help = 'pos tagging input text')

    args = vars(parser.parse_args())

    # this works! -> print(args['file'].readlines())

def main():
    print('hello')
    parse_cmdline()
    G = nx.Graph()
    text = """ The screen is filled with green, cascading code which gives way to the title, The Matrix. A phone rings and text appears on the screen: "Call trans opt: received. 2-19-98 13:24:18 REC: Log>" As a conversation takes place between Trinity (Carrie-Anne Moss) and Cypher (Joe Pantoliano), two free humans, a table of random green numbers are being scanned and individual numbers selected, creating a series of digits not unlike an ordinary phone number, as if a code is being deciphered or a call is being traced. Trinity discusses some unknown person. Cypher taunts Trinity, suggesting she enjoys watching him. Trinity counters that "Morpheus (Laurence Fishburne) says he may be 'the One'," just as the sound of a number being selected alerts Trinity that someone may be tracing their call. She ends the call. Armed policemen move down a darkened, decrepit hallway in the Heart O' the City Hotel, their flashlight beam bouncing just ahead of them. They come to room 303, kick down the door and find a woman dressed in black, facing away from them. It's Trinity. She brings her hands up from the laptop she's working on at their command. Outside the hotel a car drives up and three agents appear in neatly pressed black suits. They are Agent Smith (Hugo Weaving), Agent Brown (Paul Goddard), and Agent Jones (Robert Taylor). Agent Smith and the presiding police lieutenant argue. Agent Smith admonishes the policeman that they were given specific orders to contact the agents first, for their protection. The lieutenant dismisses this and says that they can handle "one little girl" and that he has two units that are bringing her down at that very moment. Agent Smith replies: "No, Lieutenant. Your men are already dead." Inside, Trinity easily defeats the six policemen sent to apprehend her, using fighting and evasion techniques that seem to defy gravity. She calls Morpheus, letting him know that the line has been traced, though she doesn't know how. Morpheus informs her that she will have to "make it to another exit," and that Agents are heading up after her. A fierce rooftop chase ensues with Trinity and an Agent leaping from one building to the next, astonishing the policemen left behind. Trinity makes a daring leap across an alley and through a small window. She has momentarily lost her pursuers and makes it to a public phone booth on the street level. The phone begins to ring. As she approaches it a garbage truck, driven by Agent Smith, careens towards the phone booth. Trinity makes a desperate dash to the phone, picking it up just moments before the truck smashes the booth into a brick wall. The three Agents reunite at the front of the truck. There is no body in the wreckage. "She got out," one says. The other says, "The informant is real." "We have the name of their next target," says the other, "His name is Neo." """

if __name__ == "__main__":
    main()


