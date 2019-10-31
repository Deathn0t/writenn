"""Usefull links

Tuto: https://code-maven.com/create-images-with-python-pil-pillow

"""
import json
import os

import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageMath

HERE = os.path.dirname(os.path.abspath(__file__))


class DataGenerator1:
    def __init__(self, test_mode=False):
        self.test_mode = test_mode  # test or prod
        self.img_mode = "F"
        self.background_color = 256.0
        self.font_color = 0.0
        self.fonts_cfg = os.path.join(HERE, "configs", "fonts_data1.json")
        self.fonts_paths = None
        self.thesaurus_cfg = os.path.join(HERE, "configs", "dict_data1.json")
        self.thesaurus = None

    def create(self):
        self.setup()
        count = 0
        dataset = []
        for w in self.thesaurus:
            for f in self.fonts_paths:
                print(f"{w} :: {f.split('/')[-1]}")
                l = w
                x = self.gen_element(w, f, str(count))
                count += 1
                dataset.append((x, l))
                if self.test_mode and count > 10:
                    break
        return dataset

    def setup(self):
        self.load_fonts()
        self.load_thesaurus()

    def load_fonts(self):
        with open(self.fonts_cfg, "r") as f:
            self.fonts_paths = json.load(f)

    def load_thesaurus(self):
        with open(self.thesaurus_cfg, "r") as f:
            self.thesaurus = json.load(f)

    def gen_element(self, word, font_path, fname):
        img = Image.new(self.img_mode, (100, 30), color=self.background_color)

        fnt = ImageFont.truetype(font_path, 10)
        d = ImageDraw.Draw(img)
        d.text((10, 10), word, font=fnt, fill=self.font_color)

        if self.test_mode:
            im_rgb = img.convert("RGB")
            im_rgb.show()

        return np.array(img)


def generate_data():
    os.chdir(os.path.join(HERE, "DATA", "data1"))
    Gen = DataGenerator1(test_mode=True)
    dataset = Gen.create()
    print(dataset)


if __name__ == "__main__":
    generate_data()

