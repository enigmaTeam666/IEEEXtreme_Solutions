scina = int(input())

for _ in range(scina):
    count = 0
    i = 1
    col_num = int(input())
    colors = list(map(int, input().split()))
    b = [colors[0], 0]
    while i < len(colors):
        if colors[i] == colors[i - 1]:
            i += 1
        elif colors[i] in b:
            i += 1
            continue
        else:    
            j = 1
            count += 1
            while j + i < len(colors):
                if colors[i + j] in b:
                    a = b.index(colors[i + j])
                    if a != 0:
                        b[0] = colors[i]
                    else: b[1] = colors[i]
                    break
                j+=1
            if i+j == len(colors):
                b[1]=colors[i]
            i+=1            
    print(count+1)