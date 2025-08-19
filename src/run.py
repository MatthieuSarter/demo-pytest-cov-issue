import os
import subprocess
import time
from pathlib import Path


def run(cmd: list[str] | None=None, dry_run=False) -> int:
    hello_path = Path(__file__).parent / "hello.py"
    hello_relpath = hello_path.relative_to(Path.cwd())
    print(hello_relpath)
    if not dry_run:
        p = subprocess.run(
            cmd or ["python", hello_relpath], capture_output=True, text=True, check=False
        )

        print(p.stdout)
        return p.returncode
    time.sleep(1)
    print("Dry run")
    return 42

if __name__ == "__main__":

    cwd = Path.cwd()
    os.chdir(Path(__file__).parent.parent / "src")
    rc = run()
    os.chdir(cwd)
    exit(rc)
