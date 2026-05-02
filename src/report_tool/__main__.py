from report_tool import parse_numbers, analyze, build_sorted_report, save_report


def _print_header():
    print("=" * 48)
    print("  report_tool — numeric report generator")
    print("=" * 48)
    print()
    print("A simple tool that parses numbers, computes")
    print("statistics, formats a report, and saves it.")
    print()


def _print_capabilities():
    print("Public API (importable from report_tool):")
    print()
    print("  parse_numbers(text)                  — parse comma/semicolon-separated string")
    print("  analyze(numbers)                     — compute count, sum, min, max, mean")
    print("  build_report(stats)                  — format statistics as plain text")
    print("  build_sorted_report(numbers, stats)  — same, with sorted values appended")
    print("  save_report(text, filename)          — write report to a .txt file")
    print("  read_report(path)                    — read a saved report from disk")
    print()


def _print_usage():
    print("Usage:")
    print()
    print("  # Run as a package (this output):")
    print("  python -m report_tool")
    print()
    print("  # Import and use in your own code:")
    print("  from report_tool import parse_numbers, analyze, build_sorted_report")
    print('  numbers = parse_numbers("4, 8, 15, 16, 23, 42")')
    print("  stats   = analyze(numbers)")
    print("  report  = build_sorted_report(numbers, stats)")
    print("  print(report)")
    print()


def _run_example():
    print("-" * 48)
    print("Live example:")
    print()
    text = "4, 8, 15, 16, 23, 42"
    numbers = parse_numbers(text)
    stats = analyze(numbers)
    report = build_sorted_report(numbers, stats)
    print(report)
    print()
    path = save_report(report, "report_output")
    print(f"Report saved to: {path}")
    print("-" * 48)


def main():
    _print_header()
    _print_capabilities()
    _print_usage()
    _run_example()


if __name__ == "__main__":
    main()
