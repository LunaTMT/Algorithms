"""
Binary Search both recusive and iterative
"""
def BSR(arr, l, r, value):
    if r >= l:
        m = l + ((r - l) // 2)

        if arr[m] == value:
            return f"Value: {value}, Index: {m}"
        elif arr[m] > value:
            return BSR(arr, l, m-1, value)
        else:
            return BSR(arr, m+1, r, value)
    else: 
        return f"{value} does not exist"

def BS(arr, l, r, value):
    while l <= r:
        m = l + ((r - l) // 2)

        if arr[m] == value:
            return f"Value: {value}, Index: {m}"
        elif arr[m] > value:
            r = m-1
        else:
            l = m+1
    return f"{value} does not exist"
 
arr = [1,2,3,4,5,6,7,8,9]
print(BS(arr, 0, len(arr)-1, 2))
