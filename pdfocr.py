#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author : Yi(Joy) Zeng

import tempfile
from utils.pdf_convert import convert_pdf_to_image


def main():
    pdf_path = ''
    with tempfile.TemporaryDirectory() as output_path:
        convert_pdf_to_image(pdf_path, output_path)


if __name__ == '__main__':
    main()
