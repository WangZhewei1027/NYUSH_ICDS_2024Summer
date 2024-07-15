import random
random.seed(0)


def bucket_sort(mylist):
    # initialize the buckets
    mydict = {}

    # place the values to be sorted in the buckets
    for i in range(0, len(mylist)):
        key = mylist[i]//10
        if key not in mydict.keys():
            mydict[key] = [mylist[i]]
        else:
            mydict[key].append(mylist[i])

    # sort each bucket
    for bucket in mydict.values():
        bucket.sort()

    result = []
    # concatenate all the buckets to the result
    for t in sorted(mydict.keys()):
        result += mydict[t]

    return result


def main():
    """ this is not exactly relevant, but the following 4 lines of
    code can be replaced by one line:
    list_a = [random.randint(0, 100) for i in range(100)]
    """
    list_a = []
    for i in range(10):
        list_a.append(random.randint(0, 100))
    print(list_a)

    list_a = bucket_sort(list_a)
    print("SORTED:", list_a)


main()
