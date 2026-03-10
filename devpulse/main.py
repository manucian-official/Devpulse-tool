<<<<<<< HEAD
import sys
import subprocess

from scanner import scan_files
from analyzer import analyze_code
from dashboard import dashboard
from ai_commit import generate_commit


def main():

    if len(sys.argv) < 2:
        print("Usage:")
        print("python main.py scan <project_path>")
        print("python main.py commit")
        return

    command = sys.argv[1]

    # ======================
    # SCAN PROJECT
    # ======================
    if command == "scan":

        if len(sys.argv) < 3:
            print("Please provide project path")
            return

        path = sys.argv[2]

        files = scan_files(path)

        result = analyze_code(files)

        dashboard(result)

    # ======================
    # AI COMMIT
    # ======================
    elif command == "commit":

        try:

            # chỉ lấy diff file python
            diff = subprocess.check_output(
                ["git", "diff", "--cached", "--", "*.py"],
                encoding="utf-8",
                errors="ignore"
            )

            if not diff.strip():
                print("No staged Python changes.")
                return

            # generate commit message bằng AI
            message = generate_commit(diff)

            if not message:
                print("Failed to generate commit message.")
                return

            # commit tự động
            subprocess.run(["git", "commit", "-m", message])

        except Exception as e:

            print("Git error:", e)

    else:

        print("Unknown command")


if __name__ == "__main__":
    main()
=======
import sys
from scanner import scan_files
from analyzer import analyze_code
from utils import ascii_chart

def main():
    if len(sys.argv) < 2:
        print("Usage: devpulse <project_path>")
        return
    
    path = sys.argv[1]

    files = scan_files(path)
    result = analyze_code(files)

    print("\n📊 DevPulse Report\n")
    
    print("Languages:")
    for lang, count in result["languages"].items():
        print(f"  {lang}: {count} lines")

    print("\nTODO / FIXME:")
    print(result["todos"])

    print("\nLargest File:")
    print(result["largest_file"])
    print("\nLanguage Chart:\n")
    print(ascii_chart(result["languages"]))

if __name__ == "__main__":
    main()
>>>>>>> 5213bfe3a19e1e0d02a98fbbffca7d4eeddacd5f
