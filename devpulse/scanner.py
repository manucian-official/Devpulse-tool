<<<<<<< HEAD
import os


def scan_files(path):
    code_files = []

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith((".py", ".js", ".ts", ".java", ".cpp")):
                code_files.append(os.path.join(root, file))

    return code_files
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
