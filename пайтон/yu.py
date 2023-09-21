def find_smallest_int(numbers):
    smallest = numbers[0]
    for i in numbers:
        if i < smallest:
            smallest = i
    if not smallest:
        return None
    else:
        return smallest
print(find_smallest_int([34, 15, 88, 2]))
print(find_smallest_int([34, -345, -1, 100]))
print(find_smallest_int([0]))
