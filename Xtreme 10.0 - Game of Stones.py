import sys

Test_cases = []
T = int(sys.stdin.readline())
for i in range(T):
    games = int(sys.stdin.readline())
    Test_cases.append([])
    pile = []
    for j in range(games):
        sys.stdin.readline()

        Test_cases[i].extend(list(map(int,sys.stdin.readline().split())))

output = []
temp = 0
for item in Test_cases:
    temp = 0
    for i  in item:
        temp += i // 2
    if temp % 2 == 0:
        output.append("Bob")
    else:
        output.append("Alice")
for i in output:
    print(i)