import os
from pprint import pprint

import numpy as np
from tqdm import tqdm
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))

# simplify string
def simplify_dot(path_dot_file):
    with open(path_dot_file, "r") as f:
        s = f.read()
        s = s.replace("->", ">")
        s = s.replace(" ", "")
        s = s.replace("\t", "")
        s = s.replace("\n", "")
        s = s.split('""')[-1]
    return s


def test_simplify_dot():
    fname_img = "r-1_h-1_nsh-circle_l-circo_ah-normal.png"
    fname_dot = "_".join(fname_img.split("_")[:2]) + ".dot"

    path_fname_dot = os.path.join(HERE, "dot", fname_dot)

    s = simplify_dot(path_fname_dot)


def convert_dot(path_dot_folder):
    for fname in tqdm(os.listdir(path_dot_folder)):
        if fname[-4:] == ".dot" and fname[:2] != "s_":
            with open(os.path.join(path_dot_folder, "s_" + fname), "w") as f:
                f.write(simplify_dot(os.path.join(path_dot_folder, fname)))


def test_convert_dot():
    path_dot_folder = os.path.join(HERE, "dot") + "/."
    convert_dot(path_dot_folder)


def convert_img(path_img_file):
    img = Image.open(path_img_file).convert("L")
    conv_img = 1.0 - (np.array(img) / 255.0)  # converted image inverted gray_scale
    conv_img = np.expand_dims(conv_img, axis=-1)
    return conv_img


def generate_dataset(path_img_folder, path_dot_folder):
    print("Shrink dot files")
    convert_dot(path_dot_folder)

    print("Converting images and binding with simplified dot")
    dataset = []
    for fname_img in tqdm(os.listdir(path_img_folder)):
        if fname_img[-4:] == ".png":
            conv_img = convert_img(os.path.join(path_img_folder, fname_img))
            fname_dot = "s_" + "_".join(fname_img.split("_")[:2]) + ".dot"
            with open(os.path.join(path_dot_folder, fname_dot), "r") as f:
                s_dot = f.read()
                dataset.append((conv_img, s_dot))
    return dataset


def get_data():
    path_img_folder = os.path.join(HERE, "img") + "/."
    path_dot_folder = os.path.join(HERE, "dot") + "/."
    data = generate_dataset(path_img_folder, path_dot_folder)
    return data


def test_convert_img():
    path_img_folder = os.path.join(HERE, "img") + "/."
    convert_img(path_img_folder)


if __name__ == "__main__":
    data = get_data()
    print(np.shape(data[0][0]))
