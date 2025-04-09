import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

n = int(input())

number = list(map(int, input().split()))
queue = deque(number)

calculator = list(map(int, input().split()))
A = list(permutations(calculator, len(calculator)))



