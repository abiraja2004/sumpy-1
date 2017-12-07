
import argparse


"""

python main.py

* won't be implemented in alpha version

[-s] [--remove stopwords]

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
                        'to create link between keywords')


    parser.add_argument('-l', '-lemmatize', action = 'store_true', default = False,
                        help= 'lemmatizing input text')

    parser.add_argument('-p', '--pos', action = 'store_true', default = False,
                        help = 'pos tagging input text')

    args = vars(parser.parse_args())

    # thsis works! -> print(args['file'].readlines())

def main():
    print('hello')
    parse_cmdline()

if __name__ == "__main__":
    main()


