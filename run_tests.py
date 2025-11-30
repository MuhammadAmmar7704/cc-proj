import glob
import subprocess
import sys

def main():
    examples = sorted(glob.glob("examples/*.mpl"))
    if not examples:
        print("No examples found in examples/")
        sys.exit(1)

    print(f"Found {len(examples)} tests.")
    failed = 0
    for ex in examples:
        print(f"--- Running {ex} ---")
        res = subprocess.run([sys.executable, "run.py", ex], capture_output=True, text=True)
        if res.returncode != 0:
            print(f"FAILED {ex}")
            print("Stderr:", res.stderr)
            failed += 1
        else:
            print(res.stdout)
            print(f"PASSED {ex}")
        print()

    if failed == 0:
        print("All tests passed!")
    else:
        print(f"{failed} tests failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
