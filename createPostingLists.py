import re
import string

test_corpus = """Cray gluten-free put a bird on it, Etsy reprehenderit odd future do fingerstache mollit bicycle rights bushwick vinyl lomo skateboard. American Apparel esse veniam, art party officia carles jean shorts Brooklyn Wes Anderson do. Aliqua ex American Apparel pickled. Shoreditch vinyl 8-bit biodiesel keytar nulla. Cliche occaecat iphone sartorial, Austin do yr magna jean shorts tattooed delectus. Exercitation salvia et kogi, pop-up brunch single-origin coffee. Adipisicing next level semiotics, duis consectetur organic trust fund magna sartorial ut nesciunt squid."""

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

if __name__ == "__main__":
   posting_      =  posting(test_corpus)
   posting_list_ =  posting_list(test_corpus)
   print(posting_list_)
