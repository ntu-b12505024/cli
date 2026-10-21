#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""把整個果實素材流程串成一個專案入口。"""

import argparse
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCRIPTS = {
    "normalize": "Normalized.py",
    "optimize": "Optimized.py",
    "parts": "Immerge.py",
    "blur": "tool.py",
}


def run_script(name: str):
    script_path = ROOT / name
    if not script_path.exists():
        raise FileNotFoundError(f"找不到腳本: {script_path}")

    print(f"\n=== {name} ===")
    runpy.run_path(str(script_path), run_name="__main__")


def main():
    parser = argparse.ArgumentParser(description="Run the fruit asset pipeline together.")
    parser.add_argument("--all", action="store_true", help="執行 normalize → optimize → parts → blur")
    parser.add_argument(
        "--step",
        action="append",
        choices=sorted(SCRIPTS),
        help="單獨執行一個步驟，可多次指定，例如 --step normalize --step optimize",
    )
    parser.add_argument("--dry-run", action="store_true", help="只列出要執行的步驟，不真的跑")
    args = parser.parse_args()

    if args.all:
        steps = ["normalize", "optimize", "parts", "blur"]
    elif args.step:
        steps = args.step
    else:
        steps = ["normalize", "optimize", "parts", "blur"]

    if args.dry_run:
        print("將執行：" + " → ".join(steps))
        return

    for step in steps:
        run_script(SCRIPTS[step])


if __name__ == "__main__":
    main()
