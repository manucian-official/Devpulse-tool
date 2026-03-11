import sys
from devpulse.scanner import scan_files
from devpulse.analyzer import analyze_code
from devpulse.dashboard import dashboard
from devpulse.ai_commit import generate_commit
from devpulse.quality import CodeQualityAnalyzer

def run_quality_scan(path="."):
    analyzer = CodeQualityAnalyzer()
    report = analyzer.analyze_project(path)

    print("\nDevPulse Code Quality Report")
    print("----------------------------")
    print("Files scanned:", report["files"])
    print("Lines of code:", report["lines"])
    print("Functions:", report["functions"])
    print("Classes:", report["classes"])
    print("TODOs:", report["todos"])

    if report["large_files"]:
        print("\nLarge files:")
        for f in report["large_files"]:
            print("-", f)

    if report["deep_nesting"]:
        print("\nDeep nesting detected:")
        for f in report["deep_nesting"]:
            print("-", f)


def main():

    if len(sys.argv) < 2:
        print("DevPulse CLI")
        print("Usage:")
        print("  devpulse scan <path>")
        print("  devpulse commit")
        return

    command = sys.argv[1]

    if command == "scan":
        if len(sys.argv) < 3:
            path = "."
        else:
            path = sys.argv[2]

        files = scan_files(path)
        result = analyze_code(files)
        dashboard(result)

    elif command == "commit":
        import subprocess

        diff = subprocess.check_output(
            ["git", "diff", "--cached"],
            encoding="utf-8",
            errors="ignore"
        )

        generate_commit(diff)

    else:
        print("Unknown command:", command)


if __name__ == "__main__":
    main()