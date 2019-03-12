#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author : Yi(Joy) Zeng

import tempfile
from utils.pdf_convert import convert_pdf_to_image
from utils import file_helper
from ocr.baidu_ocr import BaiduOCR


def main():
    pdf_path = 'sample.pdf'
    baidu_client = BaiduOCR()
    with tempfile.TemporaryDirectory() as output_dir:
        convert_pdf_to_image(pdf_path, output_dir)
        images = file_helper.get_all_files_with_extension(output_dir, 'jpg')
        for image in images:
            baidu_client.post_image(image)


if __name__ == '__main__':
    main()
