import os
import re
from IPython import embed
def get_fruit(sen):
    #extract the selected fruit
    m = re.search('i want (.*) /end/',sen.lower())
    if m :
        ans = m.group(1)
    return ans.split()[-1]

def to_train_format(file_name):
    with open(file_name, 'r') as f :
        data = f.readlines()
    switch = ['THEM: ', 'YOU: ']
    head = 0
    assert not os.path.exists('train.txt')
    f = open('train.txt', 'w')
    while head < len(data)-1 :
        tail = data[head:].index('-----\n')
        one_dia = data[head:head+tail]
        input_ = one_dia[0].rstrip()
        f.write('<input> '+ input_ + ' </input> ')
        f.write('<dialogue> ')
        ptr = 0
        for line in one_dia[1:] :
            line = line.rstrip()
            if line[-5:] == '/END/' :
                f.write(switch[ptr] + ' <selection> ')
                fruit = get_fruit(line)
            else :
                f.write(switch[ptr]+ line + ' <eos> ')
            ptr = (ptr+1) % 2
        f.write('</dialogue> ')
        f.write('<output> ' + fruit + ' </output> \n')
        head = head + tail + 1
    f.close()

if __name__ == '__main__' :
    to_train_format('data.txt')
