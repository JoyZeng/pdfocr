#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author : Yi(Joy) Zeng


import json
import os
from aip import AipOcr
from .abstract_ocr import AbstractOCR
from utils import file_helper


APP_ID = '10479433'
API_KEY = 'SWoOHuGFMlkxjP3t5ZrNS7Va'
SECRET_KEY = 'O9qTiNrxry78HeUTPed8WKL00Er9CXYC'

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
        self.parse_response(response)

    def parse_response(self, response: dict):
        if 'error_code' in response.keys():
            print(f'Error: {response["error_msg"]}')
            return
        else:
            result = [x['words'] for x in response['words_result']]
            result = os.linesep.join(result)
            print(result)
