from scipy import integrate

def fun(x): return 16/(16+x**2)
answer = integrate.romberg(fun, 0, 4, show=True)

print(answer)
