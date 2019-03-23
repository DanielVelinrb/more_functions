def determinate_primes_number(number):
    cont = 0
    for i in range(1, number):
        if number % i == 0:
            cont += 1
            if cont > 1:
                return None
    return number


def prime_numbers_list(n):
    prime_list = []
    limit = 0
    while limit <= n: 
        to_eval = determinate_primes_number(limit)
        if to_eval != None:  
            prime_list.append(to_eval)
        limit += 1
    
    return prime_list


def print_twin_primes(n):
    prime_list = prime_numbers_list(n)
    for i in range(len(prime_list) - 1):
        if prime_list[i + 1] - prime_list[i] == 2:
            print(f"({prime_list[i]}, {prime_list[i + 1]})")


def main():
    print_twin_primes(1000)


if __name__ == "__main__":
    main()
