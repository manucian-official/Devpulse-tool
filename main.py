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
