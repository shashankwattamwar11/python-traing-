def demo():
    print("start")
    yield 1
    print("middle")
    yield 2
    print("end")

gen1=demo()
print(next(gen1))  # Output: start \n 1
print(next(gen1))  # Output: middle \n 2