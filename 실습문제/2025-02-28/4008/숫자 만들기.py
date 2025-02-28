import sys
sys.stdin = open('input.txt')

T = int(input())
for testcase in range(1, T+1):
    N = int(input())
    arr = list(input())
    num = list(input())
    stack = []
    for i in range(arr[0]) :
        stack.append('+')
    for i in range(arr[1]) :
        stack.append('-')
    for i in range(arr[2])



