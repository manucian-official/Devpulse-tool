<<<<<<< HEAD
from collections import defaultdict
from utils import detect_language, count_todos

COMPLEX_KEYWORDS = [
    "if","for","while","switch","case","try","except","catch"
]

def complexity_score(lines):

    score = 0

    for line in lines:
        for key in COMPLEX_KEYWORDS:
            if key in line:
                score += 1

    return score


def analyze_code(files):

    languages = defaultdict(int)
    todos = 0
    largest_file = ("",0)
    complexity_total = 0

    for file in files:

        with open(file,"r",encoding="utf8",errors="ignore") as f:
            lines = f.readlines()

        line_count = len(lines)

        lang = detect_language(file)
        languages[lang] += line_count

        if line_count > largest_file[1]:
            largest_file = (file,line_count)

        todos += count_todos(lines)

        complexity_total += complexity_score(lines)

    return {
        "languages":languages,
        "todos":todos,
        "largest_file":largest_file,
        "complexity":complexity_total
    }
    
def analyze_code(files):
    result = {
        "total_files": len(files),
        "languages": {},
        "todos": 0
    }

    for file in files:
        with open(file, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()

        if file.endswith(".py"):
            lang = "Python"
        elif file.endswith(".js"):
            lang = "JavaScript"
        else:
            lang = "Other"

        result["languages"][lang] = result["languages"].get(lang, 0) + 1
        result["todos"] += text.lower().count("todo")

    return result
=======
from collections import defaultdict
from utils import detect_language, count_todos

def analyze_code(files):

    languages = defaultdict(int)
    todos = 0
    largest_file = ("",0)

    for file in files:
        with open(file,"r",encoding="utf8",errors="ignore") as f:
            lines = f.readlines()

        line_count = len(lines)

        lang = detect_language(file)
        languages[lang] += line_count

        if line_count > largest_file[1]:
            largest_file = (file,line_count)

        todos += count_todos(lines)

    return {
        "languages":languages,
        "todos":todos,
        "largest_file":largest_file
    }
>>>>>>> 5213bfe3a19e1e0d02a98fbbffca7d4eeddacd5f
