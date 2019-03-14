#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author : Yi(Joy) Zeng

import tempfile
import fire
from utils.file_convert import convert_pdf_to_image, reduce_image_size
from utils import file_helper
from ocr.baidu_ocr import BaiduOCR


def _process_pdf(pdf_path: str, output_path: str, lang: str):
    baidu_client = BaiduOCR(lang)
    with tempfile.TemporaryDirectory() as output_dir:
        print('Processing pdf, it might take a while...')
        convert_pdf_to_image(pdf_path, output_dir)
        images = file_helper.get_all_files_with_extension(output_dir, 'jpg')
        for i in range(len(images)):
            print(f'Applying OCR on page {i + 1}')
            result = baidu_client.post_image(images[i])
            if result:
                file_helper.append_line(result, output_path)


def _process_image(image_path: str, output_path: str, lang: str):
    baidu_client = BaiduOCR(lang)
    reduce_image_size(image_path)
    print(f'Applying OCR on image...')
    result = baidu_client.post_image(image_path)
    if result:
        file_helper.append_line(result, output_path)


def process(i: str, o='', lang='ENG'):
    """
    OCR a file and save the text.
    :param i: The input file path. Support pdf, jpg, png, bmp.
    :param o: The output file path
    :param lang: Use one the following: 'ENG' (default), 'CHN_ENG', 'POR', 'FRE', 'GER', 'ITA', 'SPA', 'RUS', 'JAP', 'KOR'
    :return:
    """
    file_path = i
    if not file_helper.is_file_exists(file_path):
        raise FileNotFoundError('The input file does not exist.')

    output_path = o
    if output_path == '':
        output_path = f'{file_helper.get_file_stem_name(file_path)}.txt'

    file_helper.delete_if_exists(output_path)
    extension = file_helper.get_file_extension(file_path).lower()
    if extension == 'pdf':
        _process_pdf(file_path, output_path, lang)
    elif extension in ['jpg', 'jpeg', 'png', 'bmp']:
        _process_image(file_path, output_path, lang)
    else:
        raise ValueError('Only support file types: pdf, jpg, png, bmp.')

    print('Done.')


if __name__ == '__main__':
    fire.Fire(process)
