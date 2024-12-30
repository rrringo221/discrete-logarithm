import time
def discrete_log_brute_force(g, h, p):
    for x in range(p):
        if pow(g, x, p) == h:
            return x
    return None

if __name__ == "__main__":
    g = int(input("Enter g: "))
    h = int(input("Enter h: "))
    p = int(input("Enter p: "))
    start_time = time.time()
    result = discrete_log_brute_force(g, h, p)
    end_time = time.time()
    print(f"Discrete logarithm x: {result}")
    print(f"Час виконання: {end_time - start_time:.6f} секунд")