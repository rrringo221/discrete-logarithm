import time
from sympy import factorint, mod_inverse
from concurrent.futures import ThreadPoolExecutor, as_completed


def discrete_log_brute_force(g, h, p):
    """
    Метод перебору для обчислення x у рівнянні g^x ≡ h (mod p).
    """
    for x in range(p):
        if pow(g, x, p) == h:
            return x
    return None


def spg_discrete_log(g, a, p):
    """
    Алгоритм Сільвера-Поляга-Геллмана для g^x ≡ a (mod p).
    """
    factors = factorint(p - 1)
    x_values = []

    for q, e in factors.items():
        g_q = pow(g, (p - 1) // q, p)
        a_q = pow(a, (p - 1) // q, p)

        for x in range(q):
            if pow(g_q, x, p) == a_q:
                x_values.append((x, q))
                break

    x, mod = 0, 1
    for x_q, q in x_values:
        mod_inv = mod_inverse(mod, q)
        x = (x + mod * mod_inv * (x_q - x)) % (mod * q)
        mod *= q

    return x


def measure_time(method, g, h, p):
    """
    Замір часу для обраного методу.
    """
    start_time = time.time()
    result = method(g, h, p)
    end_time = time.time()
    return result, end_time - start_time


if __name__ == "__main__":
    # Вхідні дані
    g = int(input("Введіть генератор g: "))
    h = int(input("Введіть число h: "))
    p = int(input("Введіть просте число p: "))

    # Завдання для кожного типу задачі та методу
    tasks = [
        ("Метод перебору для задачі першого типу", discrete_log_brute_force, g, h, p),
        ("Метод перебору для задачі другого типу", discrete_log_brute_force, g, h, p),
        ("Алгоритм С-П-Г для задачі першого типу", spg_discrete_log, g, h, p),
        ("Алгоритм С-П-Г для задачі другого типу", spg_discrete_log, g, h, p),
    ]

    # Паралельне виконання з негайним поверненням результатів
    with ThreadPoolExecutor() as executor:
        future_to_task = {executor.submit(measure_time, task[1], task[2], task[3], task[4]): task[0] for task in tasks}

        print("\nРезультати (з'являються одразу після завершення):\n")
        for future in as_completed(future_to_task):
            task_name = future_to_task[future]
            try:
                result, elapsed_time = future.result()
                print(f"{task_name}: x = {result}, Час: {elapsed_time:.6f} секунд")
            except Exception as e:
                print(f"{task_name}: помилка {e}")
