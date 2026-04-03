import sys

def selection_sort(A, n, target_count):
    swap_count = 0
    #아 백준문제는 뒤에서부터... 큰 수를 뒤에 먼저 놓음
    for last in range(n-1, 0, -1):
        max_index = 0
        for j in range(1, last+1): 
            if A[j] > A[max_index]:
                max_index = j

        if max_index == last:  #아오 예외처리 안 했네 
            continue

        swap_count += 1
        
        if swap_count == target_count:
            x, y  = A[last], A[max_index]
            if x > y:  # 여기도 예외 처리 
                x, y = y, x
            return x, y
        
        A[last], A[max_index] = A[max_index], A[last]
    return -1

def solve():
    #백준 23881
    input = sys.stdin.readline
    n, K = map(int, input().split())
    A = list(map(int, input().split()))
    result = selection_sort(A, n, K)
    if result == -1:
        print(-1)
    else:
        print(*result)

if __name__ == "__main__":
    solve()