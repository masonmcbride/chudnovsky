#!/usr/bin/env python3
import sys
from pathlib import Path

# ANSI color & style codes
GREEN = "\033[32m"
RED   = "\033[31m"
BOLD  = "\033[1m"
UNDER = "\033[4m"
RESET = "\033[0m"

CONTEXT = 5    # how many digits before/after to show

def load_pi(path):
    raw = Path(path).read_text().strip()
    if raw.startswith("3."):
        return raw
    elif raw[0] == "3":
        return raw[0] + "." + raw[1:]
    else:
        return "3." + raw

def find_mismatch(a, b):
    limit = min(len(a), len(b))
    for i in range(limit):
        if a[i] != b[i]:
            return i
    return None

def color_diff(a, b, idx):
    start = max(0, idx - CONTEXT)
    end   = min(len(a), idx + CONTEXT + 1)
    ca = a[start:end]
    cb = b[start:end]
    out_a, out_b, caret = [], [], []
    for rel_i, (x, y) in enumerate(zip(ca, cb)):
        abs_i = start + rel_i
        if abs_i < idx:
            out_a.append(GREEN + x + RESET)
            out_b.append(GREEN + y + RESET)
            caret.append(" ")
        elif abs_i == idx:
            out_a.append(RED + UNDER + x + RESET)
            out_b.append(RED + UNDER + y + RESET)
            caret.append("^")
        else:
            out_a.append(x)
            out_b.append(y)
            caret.append(" ")
    return "".join(out_a), "".join(out_b), "".join(caret)

def read_input():
    if not sys.stdin.isatty():
        # read piped-in data
        data = sys.stdin.read().strip().split()[0]
        return data
    elif len(sys.argv) == 2:
        return sys.argv[1].strip()
    else:
        print(f"Usage: {Path(sys.argv[0]).name} <your_pi_string>  (or pipe into it)")
        sys.exit(1)

def main():
    approx = read_input()
    true_pi = load_pi(Path.home()/"w/cs/fun/chudnovsky/pi_1mil.txt")

    idx = find_mismatch(approx, true_pi)
    if idx is None:
        print(f"{BOLD}✔ No mismatch in the first {len(approx)} characters.{RESET}")
        return

    if idx == 0:
        pos = "leading '3'"
    elif idx == 1:
        pos = "the decimal point"
    else:
        pos = f"decimal digit {idx-1}"
    print(f"{BOLD}Mismatch at {pos}.{RESET}\n")

    a_col, b_col, caret = color_diff(approx, true_pi, idx)
    print(f"  yours : {a_col}")
    print(f"  true  : {b_col}")
    print(f"          {caret}")

if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        # suppress traceback when piping into something that closes early
        sys.exit(0)