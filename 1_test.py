text="""Mary Noun Name
loves Verb No-Name
John Noun Name
. Punct No-Name

John Noun Name
loves Verb No-Name
Mary Noun Name
. Punct No-Name"""

from itertools import takewhile

sentences = []
split = iter(text.splitlines())
print split
while True:
    sentence = list(takewhile(bool, split))
    print "Hello"
    print sentence
    if not sentence:
        break
    types = set(el.split()[1] for el in sentence)
    words = [el.split(' ', 1)[0] for el in sentence]
    sentences.append(
        {
        'sentence': sentence,
        'types': types,
        'words': words
        }
    )


print sum(1 for el in sentences if 'Noun' in el['types']), 'sentences contain Noun'
print sentences[0]['words']
