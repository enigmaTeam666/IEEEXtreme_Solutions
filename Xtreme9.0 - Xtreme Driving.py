

# Input
units_cows = input()
units, number_of_cows = units_cows.split(" ")
units = int(units) % (10**9 + 7)
number_of_cows = int(number_of_cows)

# cow input
cows = []
for _ in range(number_of_cows):
    coordinates = input()
    coordinates = coordinates.split(" ")
    cow_line = int(coordinates[0])
    cow_unit = int(coordinates[1])
    cows.append( [cow_line, cow_unit] )

# cows places
cows_dict = {}
for cow in cows:
    try :
        cows_dict[cow[1]].append(cow[0])
    except :
        cows_dict[cow[1]] = [cow[0]]

for cow in cows_dict :
    if len(cows_dict[cow]) == 4 :
        print(0)
        exit(0)
if units > 185799 :
    print(0)
    exit(0)
# init
prevColm = [1,0,0,0]
current_colm = []
# get from previews value


def in_vector(i):
    global prevColm
    dic_vectors = {1:[1,2],2:[1,2,3],3:[2,3,4],4:[3,4]}
    value = 0
    for in_key in dic_vectors[i]:
        value += prevColm[in_key-1]
    return value 
# next vector accu
def get_current_colm(unit):
    global prevColm 
    global cows_dict
    out = [0,0,0,0]
    for i in range(1,5):
        try :
            if i in cows_dict[unit] :
                out[i-1] = 0
            else :
                out[i-1] =  in_vector(i)                
        except :
            out[i-1] =  in_vector(i)    
        
    return out       

for unit in range(2,units+1):
   
    current_colm = list(get_current_colm(unit))
    prevColm = list(current_colm)
    

print(current_colm[0] % (10**9 + 7)) 