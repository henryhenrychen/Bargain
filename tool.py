import json
import os
from IPython import embed
import re
import nltk

def clean_phrase(line):
    #return nltk.word_tokenize(line.lower())
    return line
def parse_log(file_name):
    data = json.load(open(file_name))
    EOS = ' <eos> '
    ans = ''
    input_ = '<input> '+' '.join([str(i) for unit in data['input'] for i in unit]) \
        + ' </input> '
    dialogue = '<dialogue> '
    for unit in data['dialogue']:
        m = re.search('<choose (.+?)>', unit['msg'])
        if m :
            fruit = m.group(1)
            buyer = unit['agent']
            break
    #too see who's first
    switch = ['BUYER: ', 'SELLER: ']
    if buyer == data['dialogue'][0]['agent'] :
        ptr = 0
    else :
        ptr = 1

    for unit in data['dialogue'] :
        dialogue += switch[ptr]+unit['msg']+ EOS
        ptr = (ptr+1)%2
    dialogue += ' </dialogue> '
    output = ' <output> '+ fruit + ' </outpupt> '
    rating = ' <rating> '+ str(data['rating'])+ ' </rating>\n '

    return(input_+dialogue+output+rating)

def extend_train_data(train_file, log_path):
    if os.path.isdir(log_path) :
        if not log_path[-1]=='/':
            log_file += '/'
        with open(train_file, 'w') as F:
            names = [f for f in os.listdir(log_path) if f.endswith('.txt')]
            for name in names :
                F.write(parse_log(log_path+name))

    else :
        with open(train_file, 'a+') as f:
            f.write(parse_log(log_path))

