def power(base, exp, mod):
    if exp == 1:
        return base
    temp = power(base, int(exp/2), mod)
    if(exp % 2 == 0):
        return (temp*temp) % mod
    else:
        return (((temp*temp) % mod)*base) % mod


n = int(input("Enter the value of n\t"))
g = int(input("Enter the value of g\t"))
x = int(input("Enter the value of x for first person\t"))
a = power(g, x, n)
y = int(input("Enter the value of y for second person\t"))
b = power(g, y, n)
print(f'Key for first person is {power(b,x,n)}')
print(f'Key for second person is {power(a,y,n)}')
