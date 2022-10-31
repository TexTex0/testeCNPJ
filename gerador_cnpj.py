import random

def generate_cnpj():
    cnpj = [random.randrange(10) for _ in range(8)] + [0, 0, 0, 1]

    for _ in range(2):
        value = sum(v * (i % 8 + 2) for i, v in enumerate(reversed(cnpj)))
        digit = 11 - value % 11
        cnpj.append(digit if digit < 10 else 0)

    return "".join(str(x) for x in cnpj)

print(generate_cnpj())