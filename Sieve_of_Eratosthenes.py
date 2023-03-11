def SOE(num):
    prime = [True for i in range(num+1)]

    p = 2
    while (p ** 2 <= num):

        if (prime[p] == True):

            for i in range(p ** 2, num+1, p):
                prime[i] = False
        p += 1
    
    return [p for p in range(2, num+1) if prime[p]]


if __name__ == "__main__":
    print(SOE(10))