def is_prime(n):
    flag = True
    for i in range(2, n-1):
        if n % i == 0:
            flag = False
            break
    return flag


if __name__ == "__main__":

    def list_prime(n):
        p = []
        for i in range(1, n):
            if is_prime(i):
                p.append(i)
        return p

    print(list_prime(10000))
