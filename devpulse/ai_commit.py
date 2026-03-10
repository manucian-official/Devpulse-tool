import requests
import re

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "deepseek-coder"


def _fallback_commit(diff):
    """
    Simple heuristic fallback nếu AI trả lời sai
    """
    if "scanner" in diff:
        return "feat(scanner): add project file scanner"
    if "dashboard" in diff:
        return "feat(dashboard): add project dashboard"
    if "analyzer" in diff:
        return "feat(analyzer): implement code analyzer"
    if "main.py" in diff:
        return "feat(cli): add CLI command handling"
    return "chore: update project files"


def generate_commit(diff: str):

    if not diff.strip():
        print("No staged changes.")
        return ""

    # limit diff size
    diff = diff[:5000]

    prompt = f"""
You generate git commit messages.

Return ONLY ONE line.

Format strictly:
type(scope): short summary

Valid types:
feat, fix, refactor, chore, docs, test

Do not explain anything.
Do not ask questions.
Do not repeat the prompt.

Diff:
{diff}
"""

    try:

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        data = response.json()
        text = data.get("response", "").strip()

        # remove markdown blocks
        text = text.replace("```", "").strip()

        # find first conventional commit line
        match = re.search(
            r"(feat|fix|refactor|chore|docs|test)(\([\w\-]+\))?: .+",
            text
        )

        if match:
            message = match.group(0)
        else:
            message = _fallback_commit(diff)

        print("\nSuggested Commit Message:\n")
        print(message)

        return message

    except Exception as e:

        print("AI error:", e)

        message = _fallback_commit(diff)

        print("\nFallback Commit Message:\n")
        print(message)

        return message