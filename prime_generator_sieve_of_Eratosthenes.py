import time, math
def sieve(n):
   
    #Create a boolean list to track prime status of numbers
    print('Creating a boolean list...')
    prime = [True] * (n + 1)
    print('Boolean list created, moving on to algorithm...')
    p = 2

    # Sieve of Eratosthenes algorithm
    while p * p <= n:
        
        if p < 11:
            print(p)
        elif p < 101:
            if int(p/11) == p/11:
                print(p)
        elif int(p/101) == p/101:
            print(p)
        
        if prime[p]:
            
            # Mark all multiples of p as non-prime
            for i in range(p * p, n + 1, p):
                prime[i] = False
        if p == 2:
            p += 1
        else:
            p += 2
    print('Algorithm finished, collecting numbers...')
    # Collect all prime numbers
    res = []
    for p in range(2, n + 1):
        if prime[p]:
            res.append(p)
    print('Numbers collected...')
    return res

if __name__ == "__main__":
    n = 10_000_000
    print(math.sqrt(n))
    start = time.time()
    res = sieve(n)
    print(f'Prime numbers generated: {len(res)}')
    print(f'Time taken: {(time.time()-start)} seconds.')
    print('Starting to write to file...')
    with open('prime_numbers.py', 'w', encoding='utf-8') as f:
        f.writelines('primes = '+str(res))
    print('File written to, exiting program...')
    