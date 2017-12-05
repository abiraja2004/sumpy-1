
import argparse



"""

python main.py

[-k] [--keywords]

    [window = between 2 and 10]


[-s] [--summary]

    [-l] [--lemmatize]

    [-p] [--pos]

    [similarity = common_words | cosine ...]

    [-v] [--visualize]

    [ratio = integer]

pagerank visualization python library: https://graph-tool.skewed.de/static/doc/centrality.html#graph_tool.centrality.pagerank

http://www.graphviz.org/gallery/

"""


def main():
    parser = argparse.ArgumentParser(description='Run automatic keywords extraction or extractive summerizer')

    parser.add_argument('-k', '--keywords')

    parser.add_argument('-s', '--summary')

    parser.add_argument('-l', '--lemmatize')

    parser.add_argument('-p', '--pos')

    #parser.add_argument('-v', '--visualize')

    parser.print_help()
    print('hello')

if __name__ == "__main__":
    main()


