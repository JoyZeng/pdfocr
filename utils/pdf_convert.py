#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author : Yi(Joy) Zeng


import os
from pathlib import Path
from pdf2image import convert_from_path
from PIL import Image


def convert_pdf_to_image(pdf_path: str, image_dir: str):
    """
    Transform pdf to single images
    :param pdf_path: The path of the pdf file.
    :param image_dir: The output directory of images.
    :return:
    """
    dpi = 200   # The image quality in DPI
    thread_count = 2    # Avoid more than 4
    image_format = 'jpeg'
    images = convert_from_path(pdf_path, dpi=dpi, fmt=image_format, thread_count=thread_count, output_folder=image_dir)

    # Reduce image size
    for image in images:
        image_path = image.filename
        max_bytes = 4 * 1024 * 1024
        while os.stat(image_path).st_size > max_bytes:
            image.save(image_path, quality=20, optimize=True)


if __name__ == '__main__':
    convert_pdf_to_image('/Users/joy/Documents/personal_workpace/PDFtoTXT/sample.pdf', '/Users/joy/Documents/personal_workpace/pdf-ocr-cli')
