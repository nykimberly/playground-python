import os
import re

def get_files(filenames, recursive=False):
    """Convert  a list of files and directories to list of files"""
    resolved_files = []

    # BFS traversal through subdirectories and files
    while filenames:
        cur_filename = os.path.abspath(filenames.pop(0))

        if cur_filename.endswith('.swp') or cur_filename.endswith('pyc'):
            continue

        if os.path.isfile(cur_filename):
            resolved_files.append(cur_filename)

        elif os.path.isdir(cur_filename):
           files_in_dir = os.listdir(cur_filename)
           paths = [os.path.join(cur_filename, f) for f in files_in_dir]
           filenames.extend(paths)

    print(resolved_files)
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
                print(relpath)
                return

            elif pattern_only:
                for match in matches:
                    print(match)

            elif show_count:
                count += 1

            elif show_filenames:
                print(relpath, line, sep=":", end=" ")

            else:
                print(line, end="")

    if show_count:

        if show_filenames:
            print(f"{relpath}:", end="")

        print(count)
