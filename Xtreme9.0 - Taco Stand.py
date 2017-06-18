days = int(input())

for _ in range(days):
    shells, meat, rice, beans = input().split()

    shells = int(shells)
    meat = int(meat)
    rice = int(rice)
    beans = int(beans)

    ingredients = [meat, rice, beans]
    ingredients.sort(reverse=True)
    tacos = 0
    if ingredients[0] > ingredients[1] + ingredients[2]:
        tacos = min(shells,ingredients[1] + ingredients[2])
    else :
        
        tmp = ingredients[0] - ingredients[1]    
        tacos +=   tmp
        ingredients[0] -= tmp
        ingredients[2] -= tmp
        
        if ingredients[2] == 2:
            if ingredients[0] == 2:
                tacos = min(shells,int(sum(ingredients)/2))
            else :    
                tacos += ingredients[0] +2
            
        elif ingredients[2] < 2:
            tacos +=   ingredients[0]
            
        else : 
            tacos = min(shells,int(sum(ingredients)/2))
        
        tacos = min(tacos,shells)
        
    print(tacos)     