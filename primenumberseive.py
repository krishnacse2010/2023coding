def SieveOfEratosthenes(n):
    
    prime = [True for i in range(n+1)]
    start = 2
    while (start * start <= n):
            i = start * start
            while i < n+1:
                prime[i] = False
                i +=start
            start +=1
    return prime
    

primeList = SieveOfEratosthenes(20)
for elem in range(2,len(primeList)):
    if primeList[elem]:
        print(elem)