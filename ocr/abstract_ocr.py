#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author : Yi(Joy) Zeng

from abc import ABC, abstractmethod


class AbstractOCR(ABC):
    @abstractmethod
    def post_image(self, image_path):
        pass

    @abstractmethod
    def parse_result(self, result):
        pass

    @staticmethod
    def get_file_content(file_path: str):
        with open(file_path, 'rb') as fp:
            return fp.read()
