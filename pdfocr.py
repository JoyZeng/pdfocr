#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author : Yi(Joy) Zeng

import tempfile
from utils.pdf_convert import convert_pdf_to_image
from utils import file_helper
from ocr.baidu_ocr import BaiduOCR


def main():
    pdf_path = 'sample.pdf'
    output_path = 'output.txt'
    baidu_client = BaiduOCR()
    with tempfile.TemporaryDirectory() as output_dir:
        print('Processing pdf, it might take a while...')
        convert_pdf_to_image(pdf_path, output_dir)
        images = file_helper.get_all_files_with_extension(output_dir, 'jpg')
        for i in range(len(images)):
            print(f'Applying OCR on page {i + 1}')
            result = baidu_client.post_image(images[i])
            if result:
                file_helper.append_line(result, output_path)

    print('Done.')


if __name__ == '__main__':
    main()
