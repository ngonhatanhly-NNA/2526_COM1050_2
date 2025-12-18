class MySolution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # Check condition for rook:
        if a == e:
            # (If bishop is between)
            if c == a and min(b, f) < d < max(b, f):
                pass
            else:
                return 1
        if b == f:
            if b == d and min(a, e) < c < max(a, e):
                pass
            else:
                return 1

        # Check for bishop, we can see that if bishop can eat queen immediately, their position given a square
        if abs(c - e) == abs(d - f):
            if abs(c - a) == abs(d - b):
                if min(c, e) < a < max(c, e) and min(d, f) < b < max(d, f):
                    pass
                else:
                    return 1
            elif self.check(a, b, c, d, e, f):
                if min(c, e) < a < max(c, e) and min(d, f) < b < max(d, f):
                    pass
                else:
                    return 1
            else:
                return 1
        return 2
    def check(self, a, b, c, d, e, f):
        return abs(a - c) == abs(d - e) and abs(b - d) == abs(d - f)

class Greedy_Solution:
    def minMovesToCaptureTheQueen(self, a: int, b:int, c: int, d: int, e: int, f: int):
        if a == e:
            return 2 if c == a and (b < d < f or b > d > f) else 1
        if b == f:
            return 2 if b == d and (a < c < e or a > c > e) else 1
        if c + d == e + f:
            return 2 if a + b == c + d and (c < a < e or c > a > e) else 1
        if c - d == e - f:
            return 2 if a - b == c - d and (c < a < e or c > a > e) else 1
        
        return 2
