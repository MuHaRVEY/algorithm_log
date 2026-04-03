#백준 23968 버블정렬
import sys

def bubble_sort(A, n, target_count):
    swap_cout = 0
    for last in range(n-1, 0, -1):
        for j in range(1, last + 1):
            if A[j-1] > A[j]:
                A[j-1], A[j] = A[j], A[j-1]
                swap_cout += 1
                if swap_cout == target_count:
                    x, y = A[j-1], A[j]
                    if x > y:
                        x, y = y, x
                    return x, y

    return -1
def solve():
    input = sys.stdin.readline
    n, K = map(int, input().split())
    A = list(map(int, input().split()))

    result = bubble_sort(A, n, K)
    if result == -1:
        print(-1)
    else:
        print(*result)

if __name__ == "__main__":
    solve()

# 버블정렬에 힙을 사용하면 시간복잡도가 O(n log n)으로 줄어들 수 있다고 한다.