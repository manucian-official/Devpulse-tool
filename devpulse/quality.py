import os
import ast

CODE_EXTENSIONS = (".py", ".js", ".ts", ".cpp", ".c", ".java", ".go")


class CodeQualityAnalyzer:

    def __init__(self):
        self.total_files = 0
        self.total_lines = 0
        self.total_functions = 0
        self.total_classes = 0
        self.total_todos = 0

        self.large_files = []
        self.deep_nesting_files = []

    def analyze_project(self, path):
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(CODE_EXTENSIONS):
                    file_path = os.path.join(root, file)
                    self.analyze_file(file_path)

        return self.report()

    def analyze_file(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            lines = content.splitlines()

            self.total_files += 1
            self.total_lines += len(lines)
            self.total_todos += content.lower().count("todo")

            if len(lines) > 500:
                self.large_files.append(file_path)

            if file_path.endswith(".py"):
                self._analyze_python(content, file_path)

        except Exception:
            pass

    def _analyze_python(self, content, file_path):
        try:
            tree = ast.parse(content)

            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    self.total_functions += 1

                if isinstance(node, ast.ClassDef):
                    self.total_classes += 1

            max_depth = self._get_max_depth(tree)

            if max_depth > 4:
                self.deep_nesting_files.append(file_path)

        except Exception:
            pass

    def _get_max_depth(self, node, depth=0):
        if not list(ast.iter_child_nodes(node)):
            return depth

        return max(
            self._get_max_depth(child, depth + 1)
            for child in ast.iter_child_nodes(node)
        )

    def report(self):
        return {
            "files": self.total_files,
            "lines": self.total_lines,
            "functions": self.total_functions,
            "classes": self.total_classes,
            "todos": self.total_todos,
            "large_files": self.large_files,
            "deep_nesting": self.deep_nesting_files,
        }