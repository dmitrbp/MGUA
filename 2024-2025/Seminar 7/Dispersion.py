def dispersion(n, m):
    rng = list(range(n - m + 1, n + m))
    disper = 0.0
    for i in rng:
        disper += (i - m) ** 2
    disper /= len(rng)
    return rng, disper

for i in range(11):
    lst, disp = dispersion(i, 5)
    print(f'i = {i}, list = {lst}, disp = {disp}')