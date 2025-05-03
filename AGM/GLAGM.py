# Run example
import os
import time
from decimal import Decimal, getcontext

# ===============================
# Configurable Cache Setup (√2)
# ===============================

CACHE_FILE = "sqrt2_cache.txt"

def get_cached_sqrt2(required_prec: int, recompute=False) -> Decimal:
    """
    Retrieve or compute sqrt(2) to required precision.
    - required_prec: precision in decimal digits
    - recompute: force recomputation even if cache exists
    """
    getcontext().prec = required_prec

    def write_cache(s2: Decimal, digits: int, elapsed: float):
        with open(CACHE_FILE, "w") as f:
            f.write(f"precision:{digits}\n")
            f.write(f"sqrt2:{str(s2)}\n")
            f.write(f"computed_in_seconds:{elapsed:.10f}\n")

    if not recompute and os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            lines = f.readlines()
            try:
                cached_prec = int(lines[0].strip().split(":")[1])
                cached_val = lines[1].strip().split(":")[1].strip()
                if cached_prec >= required_prec:
                    print(f"√2 loaded from cache at {cached_prec} digits.")
                    return Decimal(cached_val)
                else:
                    print(f"Cached √2 precision ({cached_prec}) < required ({required_prec}). Recomputing...")
            except Exception as e:
                print(f"Cache read error: {e}. Recomputing...")

    print(f"Computing √2 to {required_prec} digits...")
    start = time.time()
    sqrt2 = Decimal(2).sqrt()
    elapsed = time.time() - start
    write_cache(sqrt2, required_prec, elapsed)
    print(f"√2 computed in {elapsed:.6f} seconds.")
    return sqrt2

# ===============================
# Gauss–Legendre Category-Theoretic Structure
# ===============================

class GLObject:
    def __init__(self, a, g, t, p):
        self.a = Decimal(a)
        self.g = Decimal(g)
        self.t = Decimal(t)
        self.p = Decimal(p)

    def __repr__(self):
        return f"a={self.a}, g={self.g}, t={self.t}, p={self.p}"

def morphism(x: GLObject) -> GLObject:
    a_next = (x.a + x.g) / 2
    g_next = (x.a * x.g).sqrt()
    t_next = x.t - x.p * (x.a - a_next) ** 2
    p_next = x.p * 2
    return GLObject(a_next, g_next, t_next, p_next)

def π_approx(x: GLObject) -> Decimal:
    return ((x.a + x.g) ** 2) / (4 * x.t)

# ===============================
# Core Driver
# ===============================

def compute_pi(iterations: int, target_pi_digits: int, sqrt2_digits: int = None, verbose=False) -> Decimal:
    """
    Compute π to `target_pi_digits`, using optionally specified digits of sqrt(2).
    - If sqrt2_digits is None, uses same as target_pi_digits.
    - Returns final π value (Decimal)
    """
    sqrt2_prec = sqrt2_digits or target_pi_digits
    working_prec = target_pi_digits + 100  # safety margin
    getcontext().prec = working_prec
    print(f"Working precision set to {working_prec} digits")

    sqrt2 = get_cached_sqrt2(sqrt2_prec)
    g0 = Decimal(1) / sqrt2
    x = GLObject("1", g0, "0.25", "1")

    for i in range(iterations):
        if verbose:
            print(f"Step {i}: a={x.a}, g={x.g}, t={x.t}, p={x.p}, π ≈ {π_approx(x)}")
        x = morphism(x)

    return π_approx(x)

# ===============================
# Comparison Tool
# ===============================

def compare_pi_raw_str(π: Decimal, reference_file: str):
    if not os.path.exists(reference_file): return print("Reference file missing.")
    with open(reference_file) as f: ref = f.readline().strip()
    computed = str(π)
    match = next((i for i, (a, b) in enumerate(zip(computed, ref)) if a != b), min(len(computed), len(ref)))
    print(f"{match=}")
    print(f"{ref[match]=} != {computed[match]=}")
    print(f"✅ Matched {match} characters (including decimal point).")

if __name__ == "__main__":
    π_final = compute_pi(iterations=20, 
                         target_pi_digits=100000, 
                         verbose=False)
    print(f"\nFinal π ≈ {π_final}")
    compare_pi_raw_str(π_final, "pi_1mil.txt")
