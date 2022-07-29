import sys

sys.stdin = open("_소득불균형.txt")


T = int(input())

for num in range(T):
    n = int(input())
    data = list(map(int,input().split()))