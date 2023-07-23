'''
Given a decimal number A and a base B, convert it into its equivalent number in base B.

Input
A = 4
B = 3

Output
11

Input
A = 4
B = 2

Output
100
'''
decimal = int(input())
base = int(input())
ans = ""
while decimal > 0:
    ans += str(decimal % base)
    decimal //= base

print(ans[::-1])