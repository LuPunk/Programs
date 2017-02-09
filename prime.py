def generator(n):
    primes = []
    i = 0

    while len(primes) < n:
        if isPrime(i) == True:
            primes.append(i)
        i += 1

    return primes

def isPrime(num):
    divs = 0

    for i in range(1,num+1):
        if num % i == 0:
            divs += 1

    if divs == 2:
        return True
    else:
        return False

def prime_digs(p_list):
    prime_digits = []

    for i in p_list:
        prime_digits.append(int(str(i)[-1]))

    return prime_digits

def main():
    n = int(input("n:"))
    pr_list = generator(n)
    pr_digits = prime_digs(pr_list)

    a,b = 0,1
    match = 0

    while b < len(pr_digits):
        if pr_digits[a] == pr_digits[b]:
            match += 1
        a += 1
        b += 1

    print("{0} számból {1} egyezés van.".format(n,match))
    return None

main()