import sys
sys.setrecursionlimit(10 ** 6)

def  solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    S_raw = input_data[0]
    N = len(S_raw)

    S = ' ' + S_raw
    
    D_odd = [0] * (N + 1)
    D_even = [0] * (N + 1)

    def calc_d_odd():
        L, R = 1, 0
        for i in range (1, N + 1):
            if i > R:
                D_odd[i] = 0
            else:
                D_odd[i] = min(R-i, D_odd[L + (R - i)])
            
            while (i - D_odd[i] -1 > 0 and i + D_odd[i] + 1 <= N and
                   S[i-D_odd[i] - 1] == S[i + D_odd[i] + 1]):
                    
                D_odd[i] += 1

            if i + D_odd[i] > R:
                R = i + D_odd[i]
                L = i - D_odd[i]

    def calc_d_even():
        L, R = 1, 0
        for i in range(1, N):
            j = i + 1
            if j > R:
                D_even[i] = 0
            else:
                D_even[i] = min(R - j + 1, D_even[L + (R - j)])
            
            while (i - D_even[i] > 0 and 
                   j + D_even[i] <= N and 
                   S[i - D_even[i]] == S[j + D_even[i]]):
                D_even[i] += 1
            
            if i + D_even[i] > R:
                R = i + D_even[i]
                L = j - D_even[i]

    calc_d_odd()
    calc_d_even()

    # Chuẩn bị kết quả in ra
    result = []
    for i in range(1, N):
        result.append(str(D_odd[i] * 2 + 1))
        result.append(str(D_even[i] * 2))
    
    result.append(str(D_odd[N] * 2 + 1))
    
    # In tất cả kết quả trên một dòng, cách nhau bởi khoảng trắng
    sys.stdout.write(" ".join(result) + "\n")

if __name__ == "__main__":
    solve()