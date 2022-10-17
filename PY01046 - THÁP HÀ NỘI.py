def Try(n, a, b, c):
    if n == 1:
        print(a + " -> " + c)
        return
    Try(n - 1, a, c, b)
    Try(1, a, b, c)
    Try(n - 1, b, a, c)

Try(int(input()), "A", "B", "C")