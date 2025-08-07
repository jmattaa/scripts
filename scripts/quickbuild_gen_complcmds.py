#!/usr/bin/env python3

import os
import subprocess
import json

'''
hopefully quickbuild will be able to just give output of commands in the future
and render this function redunant
'''


def run_quickbuild_cmd(cmd_name):
    result = subprocess.run(
        ["quickbuild", "--log-quiet", cmd_name],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return result.stdout.splitlines()


project_dir = os.path.abspath(".")

src_files = run_quickbuild_cmd("echocfiles")
if src_files:
    src_files = src_files[0].split()
else:
    src_files = []

compile_flags_lines = run_quickbuild_cmd("echocompileflags")
compile_flags = " ".join(compile_flags_lines) if compile_flags_lines else ""

entries = []
for f in src_files:
    entry = {
        "directory": project_dir,
        "command": f"{compile_flags} {f} -o bin/obj/{os.path.basename(f)}.o",
        "file": f,
    }
    entries.append(entry)

with open("compile_commands.json", "w") as out_file:
    json.dump(entries, out_file, indent=2)
