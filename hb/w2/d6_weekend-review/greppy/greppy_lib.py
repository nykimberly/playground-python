import os
import re


def get_files(filenames, recursive=False):
    """Convert  a list of files and directories to list of files"""

    resolved_files = []

    for filename in filenames:
        if recursive:
            for root, dirs, files in os.walk(filename, topdown=False):
               for name in files:
                    resolved_files.append(os.path.join(root, name))
        else:
            if os.path.isfile(filename):
                resolved_files.append(filename)

    if len(resolved_files) < 1:
        print(f"!!! No Files found. Please provide files to search through."\
                "\nIf you are providing a directory, please set -r to recurse"\
                "\nNow entering stdin...")

    return resolved_files


def process_file_handle(show_count, suppress_filenames, show_filenames,
        case_insensitive, files_only, pattern_only, inverse, pattern,
        file_handle):

    count = 0

    for line in file_handle:
        relpath = os.path.relpath(file_handle.name)
        matches = pattern.findall(line)

        if matches and not inverse:

            if files_only:
                print(f"{relpath}:", end="\n")
                return

            elif pattern_only:
                for match in matches:
                    print(match)

            elif show_count:
                count += 1

            elif show_filenames:
                print(relpath, line, sep=":", end="")

            # else:
                # print(line, end="")

    if show_count:

        if show_filenames:
            print(f"{relpath}:", end="")

        print(count)
