n, k = map(int, raw_input().split())
arr = []
for i in xrange(n):
    arr.append(raw_input())

for i in xrange(k):
    for j in xrange(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print '\n'.join(arr)
