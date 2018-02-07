import os

from summa import summarizer, keywords

def get_abstr(remove_title, path):
    def _remove_title(abstr):
        final_index = -1
        for idx in range(len(abstr)):
            if abstr[idx] is  "\n" and abstr[idx+1] is not "\t":
                final_index = idx
                break
        return abstr[final_index+1:]

    abstr = []
    for filename in os.listdir(path):
        if ".abstr" in filename:
            abstr_file =  path + '/' + filename
            with open(abstr_file) as f:
                text = ""
                if remove_title:
                    text = _remove_title(f.read()).replace("\n", " ").replace("\t", "")
                else:
                    text = f.read().replace("\n", " ").replace("\t", "" )
                idx = int(filename.split(".")[0])
                abstr.append( (text, idx) )
    return abstr


def get_keywords(path):
    keywords = []
    def clean_text(text):
        return text.replace("\n", " ").replace("\t", "")
    for filename in os.listdir(path):
        if '.uncontr' in filename:
            keywords_file = path + '/' + filename
            with open(keywords_file) as f:
                text = f.read()
                text = clean_text(text).split("; ")
                idx = int(filename.split(".")[0])
                keywords.append( (text, idx) )
    return keywords

def make_string(l):
    final = ""
    for elem in l:
        final = final + elem
        final = final + ", "
    return final


path = "TestHulth"

# True = remove title

hyp = get_abstr(True, path)
hyp = sorted(hyp, key=lambda x : x[1])

gold = get_keywords(path)
gold = sorted(gold, key=lambda x : x[1])

results = []
for elem in range(len(hyp)):
    hyp_list = keywords.keywords(hyp[elem][0]).split("\n")
    total = len(hyp_list)
    total_recall = len(gold[elem][0])
    correct = 0
    for idx in hyp_list:
        if idx in gold[elem][0]:
            correct = correct + 1
    precision  = float(correct / total)
    recall = float(correct / total_recall)
    #results.append(recall)
    to_print = "| Index: " + str(hyp[elem][1]) + " - Precision: " + str(precision) + " - Recall : " + str(recall) + " | Output: " + make_string(hyp_list) + " gold: " + make_string(gold[elem][0])
#    print(to_print)

    results.append( (precision, recall) )

final_prec = 0.0
final_rec = 0.0
for elem in results:
    final_prec = final_prec + elem[0]
    final_rec = final_rec + elem[1]

to_print = "| Final avg precision: " + str(final_prec/500) + " - " + "Final avg recall: " + str(final_rec/500)
print(to_print)
