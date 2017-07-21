#!/usr/bin/env python3
# Author: Antonio Maiorano (amaiorano@gmail.com)

import sys
import re

TOC_LIST_PREFIX = "-"
# TOC_LIST_PREFIX = "*"

HEADER_LINE_RE = re.compile("^(#+)\s*(.*?)\s*(#+$|$)", re.IGNORECASE)
HEADER1_UNDERLINE_RE = re.compile("^-+$")
HEADER2_UNDERLINE_RE = re.compile("^=+$")

# Dictionary of anchor name to number of instances found so far
anchors = {}


def print_usage():
    print("\nUsage: md-to-toc <markdown_file>")


def to_github_anchor(title):
    '''
    Converts markdown header title (without #s) to GitHub-formatted anchor.
    Note that this function attempts to recreate GitHub's anchor-naming logic.
    '''

    # Convert to lower case and replace spaces with dashes
    anchor_name = title.strip().lower().replace(' ', '-')

    # Strip all invalid characters
    anchor_name = re.sub("[^A-Za-z0-9\-_]", "", anchor_name)

    # If we've encountered this anchor name before, append next instance count
    count = anchors.get(anchor_name)
    if count is None:
        anchors[anchor_name] = 0
    else:
        count = count + 1
        anchors[anchor_name] = count
        anchor_name = anchor_name + '-' + str(count)

    return '#' + anchor_name


def toggles_block_quote(line):
    '''Returns true if line toggles block quotes on or off'''
    '''(i.e. finds odd number of ```)'''
    n = line.count("```")
    return n > 0 and line.count("```") % 2 != 0

def main(argv=None):
    if argv is None:
        argv = sys.argv

    if len(argv) < 2:
        print_usage()
        return 0

    filespec = argv[1]

    with open(filespec, "r") as f:
        lines = f.readlines()
    toc = create_toc(lines)
    new_lines = list(replace_toc(lines, toc))
    with open(filespec, "w") as f:
        f.write("".join(new_lines))
    return 0

def create_toc(lines):

    in_block_quote = False
    results = []  # list of (header level, title, anchor) tuples
    last_line = ""

    for line in lines:

        if toggles_block_quote(line):
            in_block_quote = not in_block_quote

        if in_block_quote:
            continue

        found_header = False
        header_level = 0

        m = HEADER_LINE_RE.match(line)
        if m is not None:
            header_level = len(m.group(1))
            title = m.group(2)
            found_header = True

        if not found_header:
            m = HEADER1_UNDERLINE_RE.match(line)
            if m is not None:
                header_level = 1
                title = last_line.rstrip()
                found_header = True

        if not found_header:
            m = HEADER2_UNDERLINE_RE.match(line)
            if m is not None:
                header_level = 2
                title = last_line.rstrip()
                found_header = True

        if found_header:
            results.append((header_level, title, to_github_anchor(title)))

        last_line = line

    # Compute min header level so we can offset output to be flush with
    # left edge
    min_header_level = min(results, key=lambda e: e[0])[0]

    toc = []

    for r in results:
        header_level = r[0]
        spaces = "  " * (header_level - min_header_level)
        toc.append("{}{} [{}]({})\n".format(spaces, TOC_LIST_PREFIX, r[1], r[2]))
    return toc

def replace_toc(f, toc):
    it = iter(f)
    for line in it:
        if line in toc:
            break
        yield line
    else:
        for line in toc:
            yield line
        return
    k = toc.index(line)
    for line in it:
        if line.strip() == "":
            break
    for i in range(k, len(toc)):
        yield toc[i]
    yield "\n"
    for line in it:
        yield line
    return

if __name__ == "__main__":
    sys.exit(main())
