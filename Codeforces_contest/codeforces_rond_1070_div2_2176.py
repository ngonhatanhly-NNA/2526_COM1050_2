import sys
def operations_with_intersions():
    n = int(input())

    for _ in range (n):
        a = int(input())
        line = list(map(int, input().split()))

        ans = 0
        curr_max = line[0]

        for i in range (1, a):
            if line[i] < curr_max:
                ans += 1
            else:
                curr_max = line[i]

        print(ans)
def optimal_shifts():
    n = int(input())
    for _ in range (n):
        a = int(input())
        string = input()

        for i in range (a - 1, -1, -1):
            if string[i] == '1':
                last = i
                break
        first = -1
        ans = 0
        for i in range (0, a):
            if string[i] == '0':
                if first == -1 :
                    ans = max(ans, i + a - last)
                else:
                    ans = max(ans, i - first)
            else: first = i
        print(ans)


