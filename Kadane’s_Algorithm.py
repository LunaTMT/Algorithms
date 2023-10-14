"""
Similar used in leetcode 'Best Time to Buy and Sell Stock'
"""

def maxSubArraySum(A):
    n = len(A)
    Total_MAX = 0
    current_max = 0
 
    for i in range(0, n):
        current_max += A[i]
        if (Total_MAX < current_max):
            Total_MAX = current_max
 
        if current_max < 0:
            current_max = 0

    return Total_MAX

print("Maximum contiguous sum is", maxSubArraySum(A = [-2, -3, 4, -1, -2, 1, 5, -3]))