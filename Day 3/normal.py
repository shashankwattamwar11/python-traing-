def square_number(num):
    result = []
    for i in range(num):
        result.append(i * i)
    return result
    
s = square_number(2)
print(s)