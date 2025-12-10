import math as m
# Kiểm tra tam giác đều, cân, vuông
class Bai1:
    def exercise(self):
        a, b, c = map(float, input("Nhập vào 3 số nguyên dương").split())
        # Check valid Triagle
        if a + b > c and c + a > b and b + c > a:
            pass
        else:
            return "Không phải tam giác"
        # Check square
        if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or b ** 2 + c ** 2 == a ** 2:
            return "Tam giac vuong"
        # Check tam giac can
        elif a == b == c:
            return "Tam giac deu"
        elif a == b or a == c or b == c:
            return "Tam giac can"
        else:
            return "Tam giac thuong"
class Bai2:
    def exercise(self):
        n = int(input("Nhập vào 1 số nguyên dương: "))
        
        if self.sieve(n):
            return n
        res = []

        for i in range (2, int(m.sqrt(n) + 1) + 1):
            while n % i == 0:
                res.append(i)
                n //= i
        if n > 1:
            res.append(n)

        return res
        
    def sieve(self, n):
        
        is_prime = [True] * (n + 1)
        is_prime[0], is_prime[1] = False, False

        for i in range (2, int(m.sqrt(n + 1)) + 1):
            for j in range (i*i, n + 1, i):
                is_prime[j] = False
        
        return is_prime[n]

class Bai3:
    def exercise(self):
        n = int(input("Nhập vào 1 số nguyên dương: "))

        return n // 2 + 1
class Bai4:
    def exercise(self):
        n = int(input("Nhập vào 1 số nguyên dương: "))
        cnt = 0
        for i in range (1, n):
            if 3*i + 3 == n:
                cnt += 1
        return cnt
class Bai5:
    def exercise(self):
        n = int(input("Nhập vào 1 số nguyên dương: "))

        fact = self.factorial(n)
        fact = str(fact)
        
        cnt = 0
        for i in range(len(fact) - 1, -1, -1):
            if fact[i] == '0':
                cnt += 1
            if fact[i] != '0':
                break
        return cnt

    def factorial(self, n):
        if n == 1:
            return 1
        fact = 1
        for i in range (2, n + 1):
            fact *= i
        return fact

class Bai6:
    def exercise(self):
        n = int(input("Nhập vào 1 số nguyên dương: "))

        n = str(n)

        return (len(n) - 1 ) // 3
