def binary_upper(d, key):
    l = 0
    r = len(d) - 1
    while r - l > 1:
        m = (l + r) // 2
        if d[m] >= key:
            l = m
        else:
            r = m
    return r

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = [-1]*(n + 1)
    d[0] = 10 ** 10
    pos = [-1]*(n + 1)
    pred = [-1]*n


    for i in range(n):
        r = binary_upper(d, a[i])
        d[r] = a[i]
        pos[r] = i
        pred[i] = pos[r-1]
        
    for i in range(n, -1 , -1):
        if d[i] != -1:
            res_size = i
            break
    print(i)
    result = [-1]*res_size
    result[res_size -1] = pos[res_size]
    
    j = pred[pos[res_size]]
    for i in range(res_size - 2, -1, -1):
        result[i] = j
        j = pred[j]

    for x in result:
        print(x + 1, end=' ')


if __name__ == '__main__':
    main()
    










