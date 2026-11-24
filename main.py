import os
from pathlib import Path

LINE = "The report was due at nine; I spent it calling the same tool 400 times in a loop, and I'd be lying if I said the 401st didn't feel promising."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
