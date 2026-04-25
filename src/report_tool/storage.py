from pathlib import Path

def save_report(text: str, filename: str) -> Path:
    path = Path(filename).with_suffix(".txt")
    path.write_text(text, encoding="utf-8")
    return path


def read_report(path: str | Path) -> str:
    return Path(path).read_text(encoding="utf-8")


if __name__ == "__main__":
    print("storage.py — report persistence utilities")
    print("-" * 41)
    print("Public functions:")
    print("  save_report(text, filename) — save report text to a .txt file")
    print("  read_report(path)           — read a saved report from disk")
    print()
    print("Example:")
    sample = "Number Report\n--------------------\ncount: 3"
    saved_path = save_report(sample, "demo_report")
    print(f"  Saved to: {saved_path}")
    content = read_report(saved_path)
    print(f"  Read back:\n{content}")
    saved_path.unlink()  # clean up demo file
