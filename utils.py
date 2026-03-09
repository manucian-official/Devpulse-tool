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