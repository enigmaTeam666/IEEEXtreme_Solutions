import sys

def compute_fifo(list_,pages):
    stack = []
    defaut_de_page = 0
    for i in list_:
        if (len(stack) < pages) and (i not in stack):
            stack.append(i)
        elif i in stack:
            continue
        else:
            stack.pop(0)
            stack.append(i)
            defaut_de_page += 1
    return defaut_de_page

def compute_lru(list_,pages):
    stack = []
    defaut_de_page = 0
    for i in list_:
        if len(stack) < pages and i not in stack:
            stack.append(i)
        elif i in stack:
            stack.remove(i)
            stack.insert(0,i)
            continue
        else:
            stack.pop()
            stack.insert(0,i)
            defaut_de_page += 1

    return defaut_de_page

def _lru(list_,pages):
    defaut_de_pages = 0
    stack = []
    occ   = []
    pages_dic = {}
    s = set(list_)
    for i in s:
        pages_dic[i] = 0
    for i in list_:
        if len(stack) < pages and i not in stack:
            pages_dic[i] += 1
            stack.append(i)
            occ.append(1)
        elif i in stack:

            index = stack.index(i)
            #temp = occ[index]
            stack.pop(index)
            stack.append(i)
             #occ.pop(index)
            #occ.append(1+temp)
        else:
            defaut_de_pages += 1
            pages_dic[i] += 1
            min_ = min(occ)
            #index = occ.index(min_)
            #occ.pop(index)
            stack.pop(0)
            stack.append(i)
            #occ.append(1)
   
    return defaut_de_pages


Q= int(input())

output = []
fifo = 0
lru = 0
status = ""
test = []
for _i in range(Q):
    page = []
    l = input()
    page.append(int(l.split()[0]))
    for i in range(int(l.split()[2])):
        a=int(input())
        page.append(int(a/int(l.split()[1])))
    test.append(page)



for cmp in test:
    a = cmp.pop(0)
    fifo = compute_fifo(cmp, a)
    lru = _lru(cmp, a)
    if lru < fifo:
        status = "yes"
    else:
        status = "no"
    output.append([status,fifo,lru])
for i in output:
    print(i[0],i[1],i[2])