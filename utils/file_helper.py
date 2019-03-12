#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author : Yi(Joy) Zeng


from pathlib import Path
import uuid
import shutil
import glob


def is_file_exists(file_path: str) -> bool:
    path = Path(file_path)
    return path.exists()


def delete_if_exists(file_path: str):
    path = Path(file_path)
    if path.exists():
        path.unlink()


def append_line(line, output_file_path: str):
    path = Path(output_file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a', encoding='utf-8') as f:
        print(line, file=f)


def append_lines(lines, output_file_path: str):
    path = Path(output_file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a', encoding='utf-8') as f:
        for line in lines:
            print(line, file=f)


def generate_hex_uuid_4() -> str:
    """Generate UUID (version 4) in hexadecimal representation.
    :return: hexadecimal representation of version 4 UUID.
    """
    return str(uuid.uuid4().hex)


def generate_random_file_name_with_extension(file_extension: str) -> str:
    return "{}.{}".format(generate_hex_uuid_4(), file_extension)


def merge_csv(folder_path, output_file):
    '''
    Merge csv files in a folder to one file. The csv files should have the same headers.
    :param folder_path: folder of csv files.
    :param output_file: the output csv.
    :return:
    '''
    # Copied from https://stackoverflow.com/a/44791486/1736751
    all_files = glob.glob(folder_path + "/*.csv")
    all_files.sort()
    with open(output_file, 'wb') as outfile:
        for i, file_name in enumerate(all_files):
            with open(file_name, 'rb') as infile:
                if i != 0:
                    infile.readline()  # Throw away header on all but first file
                # Block copy rest of file from input to output without parsing
                shutil.copyfileobj(infile, outfile)


def get_file_bytes(file_path: str):
    return Path(file_path).read_bytes()


def get_all_files_with_extension(dir_path: str, extension: str) -> [str]:
    """
    Get sorted paths of files with specific extension under a directory
    :param dir_path: The directory containing files
    :param extension: File extension
    :return: Sorted paths of files
    """
    return get_all_files_with_pattern(dir_path, f'*.{extension}')


def get_all_files_with_pattern(dir_path: str, pattern: str) -> [str]:
    """
    Get sorted paths of files of naming pattern under a directory
    :param dir_path: The directory containing files
    :param pattern: File name pattern
    :return: Sorted paths of files
    """
    p = Path(dir_path)
    file_list = list(p.glob(f'**/{pattern}'))
    return sorted(file_list)
