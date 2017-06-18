# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(raw_input())
for tc in range(t):
    n,k = map(int,raw_input().split())
    arr = sorted([ int(raw_input()) for _ in range(n) ])
    res = arr[-1] - arr[0]
    arr = sorted([ x-y for (x,y) in zip(arr,arr[1:]) ])
    print res + sum(arr[:k-1])