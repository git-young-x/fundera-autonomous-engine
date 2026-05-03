import sys
import os

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from graph import run_engine

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("===           STARTING FUNDERA AUTONOMOUS ENGINE               ===")
    print("=" * 70)

    run_engine()

    print("=" * 70)
    print("===                  EXECUTION COMPLETE                        ===")
    print("=" * 70 + "\n")
