#!/usr/bin/env python3

import os
import sys

text_extensions = [
   ".md",
   ".txt",

   ".sln",
   ".cs",
   ".csproj",

   ".sh",

   ".py",

   ".cpp",
   ".hpp",

   ".xml",
   ".html",
   ".js",
   ".css",
]

check_mode = False
if len(sys.argv) >= 2:
    if sys.argv[1] == "--check":
        check_mode = True

ok = True
for root, dirs, files in os.walk("."):
    if ".git" in dirs:
        del dirs[dirs.index(".git")]
    for filename in files:
        full_filename = os.path.join(root, filename)
        ext = os.path.splitext(filename)[1]
        if filename == ".gitignore":
            pass
        elif ext not in text_extensions:
            print("skipped non-text file", full_filename)
            continue
        if os.stat(full_filename).st_size > 262144:
            print("skipped large file", full_filename)
            continue
        with open(full_filename, "rb") as f:
            data = f.read()
        old_data = data
        if data[:3] == b"\xef\xbb\xbf":
            data = data[3:]
        data = data.replace(b"\x0d\x0a", b"\x0a")
        while True:
            if len(data) < 2:
                break
            if data[-1:] == b"\x0a":
                if data[-2:-1] == b"\x0a":
                    data = data[:-1]
                    continue
                break
            else:
                data += b"\x0a"
                break

        lines = data.split(b"\x0a")
        for i in range(len(lines)):
            line = lines[i]
            line = line.replace(b"\t", b"    ")
            line = line.rstrip()
            lines[i] = line
        data = b"\x0a".join(lines)

        if data != old_data:
            if check_mode:
                print("failed", full_filename)
                ok = False
            else:
                print("fixed", full_filename)
                with open(full_filename, "wb") as f:
                    f.write(data)

if check_mode and not ok:
    sys.exit(1)
sys.exit(0)
