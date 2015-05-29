import re
import string


def posting(corpus):
    posting = []    
    tokens = tokenize(corpus)
    for index, token in enumerate(tokens):
        posting.append([token, (index+1)])
    return posting

def posting_list(corpus):
    posting_list = {}
    
    tokens = tokenize(corpus)
    for index, token in enumerate(tokens):
        if token not in posting_list:
            posting_list[token] = [(index + 1)]
        else:
            posting_list[token].append(index + 1)
    return posting_list


def tokenize(corpus):
    assert type(corpus) is str, 'Corpus must be a string of characters.'
    # split
    tokenized = corpus.split()
    # normalize
    for index, token in enumerate(tokenized):
        tokenized[index] = re.sub('\W\Z', '', tokenized[index])
        tokenized[index] = re.sub('\A\W', '', tokenized[index])
    return tokenized


def readFile(fileName):
    f = open(fileName,'r')
    data = f.read()
    return data

if __name__ == "__main__":
   test_corpus   =  readFile("geo.csv")
   posting_      =  posting(test_corpus)
   posting_list_ =  posting_list(test_corpus)
   print(posting_list_)
