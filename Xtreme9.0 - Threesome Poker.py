import sys


class Tree(object):
    def __init__(self,a,b,c):
        self.a = None
        self.b = None
        self.c = None
        self.level = 0
        self.parent = None
        self.data = [a,b,c]

def get_stream():
    a,b,c = sys.stdin.readline().split()
    return[int(a),int(b),int(c)]
def generate_node(root):
    if root.data[0] > root.data[1]:
        A = Tree(root.data[0]-root.data[1],2*root.data[1],root.data[2])
    else :
	    A = Tree(2*root.data[0],root.data[1]-root.data[0],root.data[2])
    if root.data[0] > root.data[2]:
	    B = Tree(root.data[0]-root.data[2],root.data[1],2*root.data[2])
    else:
        B = Tree(2*root.data[0],root.data[1],root.data[2] - root.data[0])
    if root.data[1] > root.data[2]:
        C = Tree(root.data[0],root.data[1]-root.data[2],2*root.data[2])
    else:
        C = Tree(root.data[0],2*root.data[1],root.data[2] - root.data[1])
    A.parent = root
    B.parent = root
    C.parent = root
    A.level = A.parent.level + 1
    B.level = A.level
    C.level = A.level
    root.a = A
    root.b = B
    root.c = C

l = get_stream()
root = Tree(l[0],l[1],l[2])
stack = []
stack.append(root)
level = 0
solutions = []




def generate_tree():
    
    current_level = 0
    i = 1
    cmp = 0
    found = False
    A = stack.pop(0)
    x = 1
    while True:
        x += 1
        if x > 3**10 :
            print('Ok')
            exit(0)
        
        if current_level != A.level and not found:
            current_level = A.level
        elif (current_level != A.level and found) or A.level > 11:
            break
        if equal_bet(A):
            found = True
            solutions.append(A)

        generate_node(A)
        stack.append(A.a)
        stack.append(A.b)
        stack.append(A.c)


        A = stack.pop(0)
def equal_bet(node):
    if (node.data[0] == 0 or node.data[1] == 0 or node.data[2] == 0):
        return True
    else:
        return False
generate_tree()

def get_schema(A):
    l = []
    ptr = A
    while ptr :
        l.append(ptr.data)
        ptr = ptr.parent
    return l
l = []

if solutions:
    l1 = get_schema(solutions[0])
    while l1:
        l.append(l1.pop())
    for i in l:
        print(i[0],i[1],i[2])

else:
    print("Ok")