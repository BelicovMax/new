#Первый способ
def find_average(x):
    sum1 = 0
    for i in x:
        sum1 += i
    if len(x) == 0:
        sum1 = 0
    else:
        sum1 /= len(x)
    return sum1
print(find_average([1, 2, 3, 5]))
print(find_average([]))
print(find_average([7, 7, 7]))





#Второй способ
def find_average(numbers):
    if not numbers:
        return 0
    else:
        return sum(numbers) / len(numbers)
    
print(find_average([1, 2, 3, 5]))
print(find_average([]))
print(find_average([7, 7, 7]))
