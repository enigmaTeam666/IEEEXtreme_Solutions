test_cases = int(input())
case_list = []

for case in range(test_cases):
    booking_list = {1:{}}
    booking_num = int(input())
    for booking in range(booking_num):
        start , end , cost = input().split()
        start ,end ,cost = int(start) ,int(end),int(cost)
        try :
            booking_list[start][end] = max(booking_list[start][end],cost)
        except :
            try:
                booking_list[start][end] = cost 
            except :    
                booking_list[start] = {end:cost}
    booking_list[48] = {49:0}       
    case_list.append(booking_list)
    
def exist_in(prev,dic_arcs , index):
    try:
        dic_arcs[prev][index]
        return True
    except :
        return False
def bigger_next(value,bookings):
    for i in range(value+1,max(bookings)+1):
        try :
            tmp = bookings[i]
            return i
        except :
            pass
    return -1
                
def connexe_graph(bookings):
    prev = -1
    tmp = dict(bookings)
    for index , values in  bookings.items() :
        for value in values :
            try :
                tmp[value]
            except:
                i = bigger_next(value,tmp)
                if i!=-1:
                    tmp[value] = {}
                    tmp[value][i] = 0
        if prev != -1:
            if not exist_in(prev,tmp,index) :
                tmp[prev][index] = 0 
        prev = index
    return tmp
def find_all_paths(graph, start, path=[],value=0):
        
        global paths
        path = path + [start]
        value += start[1]
        try :
            graph[start[0]]
        except :
            return value
        for node in graph[start[0]]:
            print(1)
            path_node = [node,graph[start[0]][node]]
            if path_node not in path: 
                newpath = find_all_paths(graph,path_node,path,value)
                if newpath != None:
                    paths.append(newpath)

def compress_graph(graph):
    root = min(graph)
    max_value = 0
    finish = False
    while True:
        finish = False
        
        try :
            min_node = min(graph[root])
        except :
            return max_value
        try :
            inser_node = graph[min_node]
        except :
            if len(graph[root]) == 0:
                return max_value
            max_value = max(max_value,graph[root][min_node])
            del graph[root][min_node]     
            finish = True
        if  not finish :
            for i in inser_node:
                try :
                    graph[root][i] = max(graph[root][i] , graph[root][min_node] + graph[min_node][i])
                   
                except :
                    graph[root][i] = graph[root][min_node] + graph[min_node][i]
            max_value = max(max_value,graph[root][min_node])      
            del graph[min_node]
            del graph[root][min_node]
            
from collections import OrderedDict
for case in case_list :
    paths = []
    case = OrderedDict(sorted(case.items(), key=lambda t: t[0]))
    case  = connexe_graph(case)
    print(compress_graph(case))