import math


'''
Pasul 1: determinarea H

centers = lista cu centrele de rotatie (lista de tupluri)
D = distanta dintre primul centru de rotatie si ultimul

'''

# TODO GET CENTERS

def get_H(centers):
    n = len(centers)
    D = math.dist(list(centers[0]), list(centers[-1]))
    if n % 2 == 0:
        helper = (D ** 2) / (4 * ((n - 1) ** 2))
    else:
        helper = (D ** 2 - 4) / (4 * n * (n - 2))
    return math.sqrt(1 - helper)


if __name__ == "__main__":
    centers = [(0, 1), (0, -1)]
    H = get_H(centers)
    print(H)
