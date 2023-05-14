def binary_search(list, item):
    low, high = 0, len(list)-1
    while low <= high:
        mid = (low+high)//2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid-1
        else:
            low = mid+1
    return None


if __name__ == '__main__':
    list = [1, 10, 50, 63, 78, 98, 100]
    print(binary_search(list, 98))
    print(binary_search(list, 65))
