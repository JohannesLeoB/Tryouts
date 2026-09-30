"""Längste Collatz-Kette unterhalb einer Grenze (mit Memoisierung)."""
import sys

def longest(limit):
    steps = {1: 0}
    best = (1, 0)
    for n in range(2, limit):
        path, x = [], n
        while x not in steps:
            path.append(x)
            x = x // 2 if x % 2 == 0 else 3 * x + 1
        s = steps[x]
        for p in reversed(path):
            s += 1
            steps[p] = s
        if steps[n] > best[1]:
            best = (n, steps[n])
    return best

if __name__ == "__main__":
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 1_000_000
    n, s = longest(limit)
    print(f"Unter {limit}: Startwert {n} mit {s} Schritten")
