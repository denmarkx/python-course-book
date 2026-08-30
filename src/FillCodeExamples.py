from re import sub

from markdown_it import MarkdownIt
from pathlib import Path
import os, subprocess

PREFIX = "```python,runnable"

if not os.path.exists("examples"):
    os.mkdir("examples")

for file in Path("").rglob("*.md"):
    name = file.stem

    lines = ""
    with open(file, "r") as f:
        lines = f.readlines()

    num = 0
    codeEndPos = -1
    stdout = ""

    newLines = ""
    for i, line in enumerate(lines):
        if (line.startswith(PREFIX)):
            code = ""
            for j, codeLine in enumerate(lines[i + 1:]):
                if codeLine.startswith("```"):
                    codeEndPos = i + j + 1
                    break
                code += codeLine

            codeFileName = f"examples/{name}_{num}.py"
            with open(codeFileName, "w+") as codeFile:
                codeFile.write(code)

            proc = subprocess.Popen(["python", codeFileName], stdout=subprocess.PIPE,
                stderr=subprocess.PIPE, text=True)
            stdout, stderr = proc.communicate()

            num += 1

        if (codeEndPos > 0 and i == codeEndPos): # after the concluding ```
            line += f"\n```\nOutput:\n{stdout}```\n"

        newLines += line

    with open(file, "w") as f:
        f.write(newLines)
