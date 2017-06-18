import sys
from collections import Counter

test_cases = int(sys.stdin.readline())
t = 0
all_data = []
while t < test_cases:
    s = sys.stdin.readline()
    D = int(s.split()[0])
    S = int(s.split()[-1])
    Words = []
    for i in range(0,D):
        Words.append(sys.stdin.readline().rstrip())
    Dic = []
    for i in range(0,S):
        Dic.append(sys.stdin.readline().rstrip())
    all_data.append([Words,Dic])
    t += 1
occ = {}
wordsDB = {}

def update_needs():
    for i in list(occ):
        try :
            if occ[i] > wordsDB[i]:
                wordsDB[i] = occ[i]
        except KeyError:
            wordsDB[i] = occ[i]
def dictionarystring(src):
    check = False
    count_ = 0
    for i in list(wordsDB):
        try :
            if wordsDB[i] > src[i] :
                count_ += wordsDB[i] - src[i]
                check = True
        except KeyError:
                count_ += wordsDB[i]
                check = True
    return count_
for i in range(0,test_cases):

    for word in all_data[i][0]:
        occ = dict(Counter(word))
        update_needs()
    for dic in all_data[i][1]:
        occ = dict(Counter(dic))
        if occ == wordsDB:
            print("Yes Yes")
        elif(dictionarystring(occ) > 0):
            print('No '+ str(dictionarystring(occ)))
        else:
            print("Yes No")
    wordsDB = {}