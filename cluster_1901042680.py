def cluster(a):
    max = a[0]
    F = [0] * len(a)
    
    for i in range(len(a)):
        k=0
        F[k] += a[i]
        if F[k] < 0:
            F[k] = 0
        elif max < F[k]:
            max = F[k]
        k += 1
            
    print("maximum profit: ", max)
    
cluster([3, -5, 2, 11, -8, 9, -5])