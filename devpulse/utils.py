<<<<<<< HEAD
import os


def detect_language(file):
    ext = os.path.splitext(file)[1]

    mapping = {
        ".py": "Python",
        ".js": "JavaScript",
        ".ts": "TypeScript",
        ".java": "Java",
        ".cpp": "C++",
        ".c": "C",
        ".go": "Go",
        ".rs": "Rust"
    }

    return mapping.get(ext, "Unknown")


def count_todos(text):
    return text.lower().count("todo")
=======
import os

def scan_files(path):
    code_files = []

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith((".py",".js",".cpp",".c",".java",".ts",".go")):
                code_files.append(os.path.join(root,file))

    return code_files
>>>>>>> 5213bfe3a19e1e0d02a98fbbffca7d4eeddacd5f
