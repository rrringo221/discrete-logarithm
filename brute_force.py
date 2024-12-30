def brute_force_discrete_log(g, a, p):
    """
    Обчислює x для рівняння g^x ≡ a (mod p) методом перебору.
    """
    for x in range(p):
        if pow(g, x, p) == a:
            return x
    return None

if __name__ == "__main__":
    g = int(input("Введіть генератор g: "))
    a = int(input("Введіть число a: "))
    p = int(input("Введіть просте число p: "))

    result = brute_force_discrete_log(g, a, p)
    if result is not None:
        print(f"x = {result}")
    else:
        print("Розв'язок не знайдено.")

#працездатність коду було перевірено на прикладах з домашнього завдання. Працездатність підтверджено