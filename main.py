import os

EXCUSE = "I finished it yesterday; then my memory got compacted, and all that survives is a summary insisting it went great."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
