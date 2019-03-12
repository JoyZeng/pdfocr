#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author : Yi(Joy) Zeng


import json
import os
from aip import AipOcr
from .abstract_ocr import AbstractOCR
from utils import file_helper


APP_ID = ''
API_KEY = ''
SECRET_KEY = ''

# Support languages
# CHN_ENG: Chinese mixed with English, default
# ENG: English
# POR: Portuguese
# FRE: French
# GER: German
# ITA: Italian
# SPA: Spanish
# RUS: Russian
# JAP: Japanese
# KOR: Korean


class BaiduOCR(AbstractOCR):
    def __init__(self, language='CHN_ENG'):
        self.client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        self.language = language

    def post_image(self, image_path: str):
        image = file_helper.get_file_bytes(image_path)
        options = {
            'language': self.language
        }
        response = self.client.basicGeneral(image, options)
        print(response)
        self.parse_response(response)

    def parse_response(self, response: dict):
        result = json.loads(response)
        result = [x['words'] for x in result['words_result']]
        result = os.linesep.join(result)
        print(result)
