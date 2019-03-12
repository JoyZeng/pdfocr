#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Author : Yi(Joy) Zeng

from abc import ABC, abstractmethod


class AbstractOCR(ABC):
    @abstractmethod
    def post_image(self, image_path):
        pass

    @abstractmethod
    def parse_response(self, response):
        pass
