import sys
import math

def A():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    try:
        n = int(next(it))
    except StopIteration:
        return

    results = []
    for _ in range(n):
        l = int(next(it))
        a = int(next(it))
        b = int(next(it))
        
        g = math.gcd(b, l)
        
        # 2. Mathematical shortcut:
        # The sequence visits all numbers x where x % g == a % g
        # The largest such number <= l - 1 is:
        max_val = (l - 1) - ((l - 1 - a) % g)
        
        results.append(str(max_val))
    
    # Print all results at once for speed
    sys.stdout.write("\n".join(results) + "\n")

def B():
    file = sys.stdin.read().split()
    if not file:
        return
    it = iter(file)
    t = int(next(it))

    for _ in range (t):
        n = int(next(it))
        
        s = next(it)
        for _ in range (n - 1):
            a = next(it)
            option1 = s + a
            option2 = a + s

            if option1 < option2:
                s = option1
            else:
                s = option2
        print(s)
import sys
"""chua lam dc"""
def C():
    file = sys.stdin.read().split()
    if not file:
        return
    it = iter(file)
    t = int(next(it))
    results= []
    for _ in range (t):
        n, k = int(next(it)), int(next(it))
        if k % 2 == 1:
            print(*([str(n)] * (k))) # k odd thì với mọi thay đổi sẽ vẫn return lại nó
        else:
            # Nêu là pow of 2 -> return chính nó và 0 bởi vì thỏa mãn chỉ có duy nhất 1 số lẻ -> nếu cho khác vào sẽ luôn là lẻ ở các vị trí khác
            # 
            if n % 2 == 0:
                print(*([str(n)] * (k-1)  + ['0']))
            else:
                print (*([str(n)] * (k-2) + [str(n-1)] + ['1']) )

    
if __name__ == '__main__':
    C()