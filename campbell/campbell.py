from mpmath import mp, sqrt, log

mp.dps = 1000

lambda1105 = ((sqrt(5)+1)/2)**12 * (4+sqrt(17))**3 * ((15+sqrt(221))/2)**3 * (8+sqrt(65))**3
J3315 = -((64*lambda1105**2)/((lambda1105**2-1)*(9*lambda1105**2-1)**3))

# This denominator must be: -1 + sqrt((-1 + J3315)/J3315)
denom = -1 + sqrt((-1 + J3315) / J3315)
x3315 = mp.mpf('1')/8 * (mp.mpf('2')
    - (3 * (-1/J3315)**(mp.mpf('2')/3)) / (denom**(mp.mpf('1')/3))
    + 3 * ((1 - sqrt((-1 + J3315)/J3315))/J3315)**(mp.mpf('1')/3)
)

lambdaast3315 = sqrt(1-sqrt(1-x3315))/sqrt(2)
lambdaast13260 = (1-sqrt(1-lambdaast3315**2)) / (1+sqrt(1-lambdaast3315**2))
x13260 = 4 * (lambdaast13260**2 - lambdaast13260**4)
z13260 = -27 * x13260 / (1-4*x13260)**3

t3315 = (
    mp.mpf('1095255033002752301233099478037584')/mp.mpf('2050242335692983321671746996556833')
    + mp.mpf('1006588064225996719872149534306400')/mp.mpf('34854119706780716468419698941466161')*sqrt(17)*sqrt(5)
    + mp.mpf('692779168175128551453280427070000')/mp.mpf('34854119706780716468419698941466161')*sqrt(17)
    - mp.mpf('136434536163779492503565618457696')/mp.mpf('2050242335692983321671746996556833')*sqrt(5)
    + mp.mpf('400179322879781860521299209248000')/mp.mpf('26653150364008783181732710955238829')*sqrt(13)
    + mp.mpf('1077564413015882021519209726762688')/mp.mpf('453103556188149314089456086239060093')*sqrt(13)*sqrt(17)*sqrt(5)
    + mp.mpf('120226784218523863048087030809600')/mp.mpf('64729079455449902012779440891294299')*sqrt(17)*sqrt(13)
    + mp.mpf('239369594240980944219359445009600')/mp.mpf('26653150364008783181732710955238829')*sqrt(13)*sqrt(5)
)
alpha3315 = (mp.mpf('1')/2*sqrt(1105/3)*sqrt(1-J3315)*(1-t3315)*2*(1-4*x3315)**(mp.mpf('3')/2) - (4*x3315-1+sqrt(1-x3315))*sqrt(3315)) / (2*(1-4*x3315))
alpha13260 = (4*alpha3315 - 2*sqrt(3315)*lambdaast3315**2) / (1+sqrt(1-lambdaast3315**2))**2
b13260 = ((8*x13260+1)*sqrt(1-x13260)*sqrt(13260)) / (1-4*x13260)**(mp.mpf('3')/2)
a13260 = (2*(1-4*x13260)*alpha13260 + (4*x13260-1+sqrt(1-x13260))*sqrt(13260)) / (2*(1-4*x13260)**(mp.mpf('3')/2))

print("Digits per iteration")
print(log(-1/z13260)/log(10))

print('a13260:', a13260)
print('b13260:', b13260)

s = a13260
print("1st term s (should be close to 2/pi):", s)
pi_approx = 2/s
print("Approx pi (should match pi):", pi_approx)
print("Digits matched:", -mp.log10(abs(pi_approx - mp.pi)))

def poch_product(a, n):
    # Returns prod_{i=0}^{n-1} (a + i), pochhammer(a, n)
    p = mp.mpf(1)
    for i in range(n):
        p *= a + i
    return p

def ramanujan_term(n):
    num = (
        poch_product(mp.mpf('1')/2, n)
        * poch_product(mp.mpf('1')/6, n)
        * poch_product(mp.mpf('5')/6, n)
    )
    den = poch_product(1, n) ** 3
    return num/den * z13260**n * (a13260 + b13260*n)

def ramanujan_sum(N):
    return sum(ramanujan_term(n) for n in range(N))

# --- Try one iteration, two iterations, ... ---

for N in [1, 2, 3]:
    s = ramanujan_sum(N)
    print(f"Ramanujan sum for N={N} term(s):")
    print(s)
    pi_approx = 1 / s
    print(f"Digits matched after {N} terms: {-mp.log10(abs(pi_approx - mp.pi))}")
    print("First digits: ", str(pi_approx)[:80], "\n")
