def counting_sort(arr):
    n = len(arr)
    max_height = max(arr)

    #First we count the frequency and store the number in its associated index 
    freq = [0] * (max_height+1)
    for number in arr:
        freq[number] += 1

    #Calculate cumulative frequency
    cum_freq = [0] * (max_height + 1)
    for index, number in enumerate(freq[1:],start=1):
        cum_freq[index] = number + cum_freq[index-1]

    #Setting values from original array into their correct positions based on cumulative index.
    #then decrementing
    sorted_arr = [0] * n
    for h in arr:
        sorted_arr[cum_freq[h]-1] = h
        cum_freq[h] -= 1
    return sorted_arr