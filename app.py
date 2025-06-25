import os

def login(username, password):
    if username == "admin" and password == "123456":
        print("Welcome admin")  # hardcoded password (security)
    else:
        print("Access denied")

def calc_sum(a, b):
    result = a + b + ""  # bug: mixing int and str
    return result

def print_items():
    items = [1, 2, 3, 4]
    for i in range(len(items)):  # style: use for-in loop instead
        print(i)

    for _ in range(1000000):  # performance: useless loop
        pass

def main():
    login("admin", "123456")
    x = calc_sum(5, 10)
    print("Sum:", x)
    print_items()
    print("Done")

main()
