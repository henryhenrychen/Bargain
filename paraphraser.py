from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import wordnet as wn

def tag(sentence):
    words = word_tokenize(sentence)
    words = pos_tag(words)
    return words

def paraphraseable(tag):
    return tag.startswith('NN') or tag == 'VB' or tag.startswith('JJ')

def pos(tag):
    if tag.startswith('NN'):
        return wn.NOUN
    elif tag.startswith('V'):
        return wn.VERB

def synonyms(word, tag):
    return set([lemma for lemma in wn.synsets(word)[0].lemma_names()])

def synonymIfExists(sentence):
    for (word, t) in tag(sentence):
        if paraphraseable(t):
            syns = synonyms(word, t)
            if syns:
                if len(syns) >= 1:
                    #yield [word, list(syns)]
                    yield list(syns)
                    continue
        yield [word]

def paraphrase(sentence):
    return [x for x in synonymIfExists(sentence)]

#if __name__ == '__main__':
    #return paraphrase("I want to buy an orange")
