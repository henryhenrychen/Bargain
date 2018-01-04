from nltk.corpus import wordnet as wn
from paraphraser import paraphrase
from IPython import embed

with open('data.txt', 'r') as f:
    data = f.readlines()[1:]

head = 0
while head != len(data) :
    sen_num = data[head:].index('-----\n')+1
    tmp = [[] for _ in range(sen_num)]
    for sen in data[head:head+sen_num] :
        result = paraphrase(sen)

        embed()
