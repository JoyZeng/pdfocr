#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author : Yi(Joy) Zeng


import os
from aip import AipOcr
from .abstract_ocr import AbstractOCR
from utils import file_helper

# Baidu OCR API key.
# Please respect it.
APP_ID = '10479433'
API_KEY = 'SWoOHuGFMlkxjP3t5ZrNS7Va'
SECRET_KEY = 'O9qTiNrxry78HeUTPed8WKL00Er9CXYC'

# Support languages
# ENG: English (default)
# CHN_ENG: Chinese mixed with English
# POR: Portuguese
# FRE: French
# GER: German
# ITA: Italian
# SPA: Spanish
# RUS: Russian
# JAP: Japanese
# KOR: Korean
SUPPORTED_LANGUAGES = ['ENG', 'CHN_ENG', 'POR', 'FRE', 'GER', 'ITA', 'SPA', 'RUS', 'JAP', 'KOR']


class BaiduOCR(AbstractOCR):
    def __init__(self, language='ENG'):
        self.client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        if language not in SUPPORTED_LANGUAGES:
            raise ValueError(f'Language is not supported. Please use one of the following: {SUPPORTED_LANGUAGES}')
        self.language = language

    def post_image(self, image_path: str, options: dict):
        image = file_helper.get_file_bytes(image_path)
        params = {
            'language': self.language
        }

        if options.get('accurate', True):
            response = self.client.basicAccurate(image, params)
        else:
            response = self.client.basicGeneral(image, params)
        return self.parse_response(response)

    def parse_response(self, response: dict):
        if 'error_code' in response.keys():
            print(f'Error: {response["error_msg"]}')
            return None
        else:
            result = [x['words'] for x in response['words_result']]
            result = os.linesep.join(result)
            result += os.linesep
            return result
