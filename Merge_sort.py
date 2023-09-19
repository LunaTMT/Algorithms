from math import floor

def Merge(A, p, q, r):
    nL = q - p + 1
    nR = r - q

    L = [0] * nL
    R = [0] * nR

    for i in range(nL):
        L[i] = A[p + i]
    for j in range(nR):
        R[j] = A[q + 1 + j]

    i = j = 0 
    k = p

    while i < nL and j < nR:
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while i < nL:
        A[k] = L[i]
        i += 1
        k += 1

    while j < nR:
        A[k] = R[j]
        j += 1
        k += 1
    

def MergeSort(A, p, r):
    if p >= r:
        return 
    q = floor((p+r)/2)
    MergeSort(A, p, q)
    MergeSort(A, q+1, r)
    Merge(A, p, q, r)
    return A

if __name__ == "__main__":
    A = [9,8,7,67,6,56,4,3,3]
    p = 0
    r = len(A) - 1
    print(MergeSort(A, p, r))