def generate_passuword(n):
    password = ""

    # перебор пар и проверка кратности
    for i in range(1, n//2 + 1):
        for j in range(i + 1, n + 1):
            pair_sum = i + j
            if n % pair_sum == 0:
                password += str(i) + str(j)

    return password

n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    result = generate_passuword(n)
    print("Нужный пароль", result)
else:
    print("Число должно быть в диапозоне от 3 до 20")


