from sympy import factorial, log, N
from mpmath import mp

mp.dps = 100  # high precision

def chudnovsky_term(k):
    M_k = factorial(6 * k)
    L_k = 545140134 * k + 13591409
    X_k = (640320 ** 3) ** k
    K_k = factorial(3 * k) * (factorial(k) ** 3)
    return M_k * L_k / (K_k * X_k)

def digit_gain(k):
    T_k = N(chudnovsky_term(k), mp.dps)
    T_next = N(chudnovsky_term(k + 1), mp.dps)
    return log(abs(T_k / T_next), 10).evalf()

# Show digits gained by each new term
n = 20
cumm = 0 
for k in range(n):
    digits_gained = digit_gain(k)
    cumm += digits_gained
    print(f"k = {k} → digits gained by term {k+1} = {digits_gained}")
print(f"average digits gained = {cumm/n}")

