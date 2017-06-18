test_cases = int(input())
if test_cases == 0 or test_cases > 10:
    exit()
list_test_cases = []
for _ in range(test_cases):
    line = input()
    if len(line) == 0 or len(line) > 10**6:
        exit()
    list_test_cases.append(line)



def patternCount(string,patternSize):
    global lastMax
    i = max(lastMax, patternSize)
    for char_index in range(i,len(string)):
        try :
            if string[char_index] in "ABCDEFGHIJKLMNOPQRSTUWXYZ123456789/*-+.,;:!)_è-('":
                1/0
                exit()
            if string[char_index] != string[char_index % patternSize]:
                lastMax = char_index
                return False
        except:
            return False
    return True 

def solution(string):
    for i in range(1,len(string)):
        if patternCount(string, i):
            return i
    return len(string)    
            
for case in list_test_cases:
    lastMax = 0
    print(solution(case))