import sys

def A():
    file = sys.stdin.read().split()
    if not file:
        return
    it = iter(file)
    MOD = 26
    n = int(next(it))
    for _ in range (n):
        # Chir được có chữ số trong k bảng chữ cái đầu -> và sj - si khác nhau
        # Phải có sj -  s1 chia hết cho x
        
        k, x = int(next(it)), int(next(it))

        # ipnut số đầu là a -> nếu chưa đến khoảng chia hết, cứ input số đó, 
        # với các index thỏa mãn chia hết, thì chữ cái của nó phải khác nhau
        # đây có thể coi là 1 math problem
        print(k*x + 1)

def B():
    file = sys.stdin.read().split()
    if not file:
        return
    it = iter(file)

    t = int(next(it))
    for _ in range (t):
        n = int(next(it))
        arr = [int(next(it)) for _ in range (n)]
        
        if n <= 2:
            print(0)
            continue
        
        difference = [abs(arr[i+1] - arr[i]) for i in range (n - 1)]
        total_sum = sum(difference)
        
        best_reduction = difference[0]
        if difference[-1] > best_reduction:
            best_reduction = difference[-1]
        for i in range (1, n-1):
            reduction = (abs(arr[i] - arr[i-1]) + abs(arr[i+1] - arr[i]) - abs(arr[i+1] - arr[i-1]))
            if reduction > best_reduction:
                best_reduction = reduction
        
        print(total_sum - best_reduction)
import math
def C():
    file = sys.stdin.read().split()
    if not file:
        return
    it = iter(file)

    t = int(next(it))
    for _ in range (t):
        n = int(next(it))
        arr = [int(next(it)) for _ in range (n)]
        # Theo nhuw testcase 1, 2 thì hầu như số return về sẽ luôn là
        # sô bé nhất nếu nó không có điểm chung nào chia hết cho nhau
        arr.sort()
        min_val = min(arr)
        min_greater = arr[1]

        k = max(min_val, min_greater - min_val)
        print(k)

def D():
    file = sys.stdin.read().split()
    if not file:
        return
    it = iter(file)

    t = int(next(it))
    results = []
    for _ in range (t):
        n = int(next(it))
        # lớn nhất khi giữ được nhiều nhất các bit, các số đi sau phải luôn là số có lưu trữ só 1 ở sau
        # 3 -> 2 -> 1 thì giữ đc 1 bit -> 0, 2 đều như nhau vì cái bit của 2 đã bị loại 
        # Ngoại trừ các số giữ toàn bit trong nó thì cá số còn lại sẽ luôn có không, vì vậy nếu gọi lần lợt thì cho đén bit 1 1 1 
        # thí cái bit cũng bị triệt tiêu nhiều phần rồi, nên ta trả lại 0 để giải phóng cac bit lôn
        if n == 1:
            results.append("1 0")
            continue
        # 2 * n - 1 = 1000000 - 1
        num_elements = 1 << n
        p0 = num_elements - 1 # 1 1 -> 3
        res = [p0]
        i = 1
        while (1 << (n - i)) - 1 > 1:
            p1 = (1 << (n-1)) - 1
            res.append(p1)
            i += 1
        res.append(1)
        
        for i in range (num_elements):
            if i not in res:
                res.append(i)
        # Các số đã sử dụng
       
        results.append(" ".join(map(str, res)))
        
    sys.stdout.write("\n".join(results) + "\n")
if __name__ == '__main__':
    D()
