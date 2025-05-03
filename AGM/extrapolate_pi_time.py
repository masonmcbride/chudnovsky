"""
OUTPUT
(ia) mason :: ~/w/cs/fun/chudnovsky/AGM > time ./glagm 14  33219    >/dev/null
./glagm 14 33219 > /dev/null  0.00s user 0.00s system 73% cpu 0.011 total
(ia) mason :: ~/w/cs/fun/chudnovsky/AGM > time ./glagm 17       332193    >/dev/null 
./glagm 17 332193 > /dev/null  0.05s user 0.00s system 97% cpu 0.056 total
(ia) mason :: ~/w/cs/fun/chudnovsky/AGM > time ./glagm 19       3321929    >/dev/null
./glagm 19 3321929 > /dev/null  0.52s user 0.01s system 99% cpu 0.531 total
(ia) mason :: ~/w/cs/fun/chudnovsky/AGM > python3 extrapolate_pi_time.py \
  -m 10000 0.011 \
  -m 100000 0.056 \
  -m 1000000 0.531

Fitted constant C = 1.287e-08

Predicted wall-clock time for 1,000,000,000 digits:
  1352.5 seconds
  → 0.38 hours
  → 0.02 days
  → 0.00 years

"""
import math
import numpy as np
import argparse

def fit_C(decimals, times):
    """
    Fit C to T_i = C * n_i * log2(n_i) across all measurement points
    by simple averaging: C ≈ mean( T_i / (n_i*log2(n_i)) ).
    """
    ns = np.array([d * math.log2(10) for d in decimals])  # bits
    Ts = np.array(times)
    Cs = Ts / (ns * np.log2(ns))
    return Cs.mean()

def predict_time(decimals_target, C):
    """
    Given C, predict T for decimals_target via T = C * n * log2(n).
    """
    n = decimals_target * math.log2(10)
    return C * n * math.log2(n)

def main():
    parser = argparse.ArgumentParser(
        description="Fit O(n log n) model to timing data and extrapolate to 1B digits"
    )
    parser.add_argument(
        "--measure", "-m",
        nargs=2, metavar=("DIGITS","TIME"),
        action="append",
        type=float,
        help="Add a measurement: decimal_digits measured_seconds"
    )
    parser.add_argument(
        "--target", "-t",
        type=float,
        default=1e9,
        help="Target decimal digits to extrapolate (default: 1e9)"
    )
    args = parser.parse_args()

    if not args.measure or len(args.measure) < 2:
        parser.error("Please supply at least two --measure entries (e.g. -m 10000 0.12)")

    decimals, times = zip(*args.measure)
    C = fit_C(decimals, times)

    print(f"Fitted constant C = {C:.3e}")
    T_pred = predict_time(args.target, C)

    # Present in human-friendly units
    hours = T_pred / 3600
    days  = hours / 24
    years = days / 365.25

    print(f"\nPredicted wall-clock time for {int(args.target):,} digits:")
    print(f"  {T_pred:.1f} seconds")
    print(f"  → {hours:.2f} hours")
    print(f"  → {days:.2f} days")
    print(f"  → {years:.2f} years")

if __name__ == "__main__":
    main()