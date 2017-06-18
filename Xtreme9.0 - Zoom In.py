columns = int(input())
rows = int(input())

number_of_translations = int(input())

translations = {}

for _ in range(number_of_translations):
    character = input()

    translation = []
    for _ in range(rows):
        translation.append(input())

    translations[character] = translation

number_of_strings = int(input())
strings = []
for _ in range(number_of_strings):
    strings.append(input())

for string in strings :
    for i in range(0,rows):
        line = ""
        for c in string:
            line += translations[c][i]
        print (line)    