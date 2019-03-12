#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author : Yi(Joy) Zeng


from pdf2image import convert_from_path
from PIL import Image


def convert_pdf_to_image(pdf_path: str, image_dir: str):
    """
    Transform pdf to single images
    :param pdf_path: The path of the pdf file.
    :param image_dir: The output directory of images.
    :return:
    """
    dpi = 100   # The image quality in DPI
    thread_count = 2    # Avoid more than 4
    quality = 20    # Image resize quality
    max_pixel = 4096
    image_format = 'jpeg'
    images = convert_from_path(pdf_path, dpi=dpi, fmt=image_format, thread_count=thread_count, output_folder=image_dir)

    # Reduce image size if one edge's pixel is more than the threshold.
    for image in images:
        if max(image.width, image.height) > max_pixel:
            image_path = image.filename
            ratio = max_pixel / max(image.width, image.height)
            image = image.resize((int(image.width * ratio), int(image.height * ratio)), Image.ANTIALIAS)
            image.save(image_path, quality=quality, optimize=True)
