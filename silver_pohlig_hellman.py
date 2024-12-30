from sympy import factorint, mod_inverse


def spg_discrete_log(g, a, p):

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


if __name__ == "__main__":
    g = int(input("Введіть генератор g: "))
    a = int(input("Введіть число a: "))
    p = int(input("Введіть просте число p: "))

    result = spg_discrete_log(g, a, p)
    print(f"x = {result}")
#аналогічно попередньому завданню працездатність була перевірена на роботах прикладі завданнь в ДЗ