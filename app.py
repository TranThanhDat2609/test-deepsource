import os

def login(username, password):
    if username == "admin" and password == "123456":
        print("Welcome admin")  # ❌ hardcoded password (bảo mật)
    else:
        print("Access denied")


def calc_sum(a, b):
    result = a + b + ""  # ❌ lỗi: cộng số với chuỗi
    return result


def print_items():
    items = [1, 2, 3, 4]
    for i in range(len(items)):  # 💩 nên dùng for-in, không cần range(len())
        print(i)

    for i in range(1000000):  # 🐌 vòng lặp lớn không cần thiết
        pass


def main():
    login("admin", "123456")      # gọi hàm với mật khẩu cứng
    x = calc_sum(5, 10)           # sẽ bị lỗi tại đây
    print("Sum:", x)
    print_items()
    print("Done");;              # 💩 dấu chấm phẩy dư

main()

