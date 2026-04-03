def factorial(x):
    if x < 0:
        return "Invalid"
    if x == 0 or x == 1:
        return 1
    return x * factorial(x-1)


abs_term=lambda t: t if t >= 0 else -t
def exp_x(x, n):
    total=0
    for i in range(n):
        term = abs_term((x**(2 * i)) / factorial(2 * i))
        if i % 2 == 0:
            total += term
        else:
            total -= term
    return total


g_tot = 0
def geometric_recursive(n, r):
    """
    This function finds the series 1 + r + r^2 + ... + r^n by using recursion.
    If n becomes smaller than 0, the function stops.Else, it adds the current term r^n to the global variable,
    then calls itself again with n-1.
    There is not any changing +/- sign in this series.When r is negative, Python automatically calculates the sign correctly.
    """
    global g_tot
    if n < 0:
        return
    g_tot += r ** n
    geometric_recursive(n - 1, r)


x = float(input("Enter x: "))
n = int(input("Enter n: "))
print("Factorial of", n, "=", factorial(n))
print("Summation result =", round(exp_x(x, n), 4))
n=int(input("Enter n: "))
r = float(input("Enter r: "))
g_tot = 0
geometric_recursive(n, r)
print("Geometric series result =", g_tot)