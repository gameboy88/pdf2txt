#!/usr/bin/env python

import argparse
import cv2
import pytesseract
import yaml
import sys
sys.stdout.reconfigure(encoding="utf-8")

def parse_args():
    parser = argparse.ArgumentParser("Image to Text")
    parser.add_argument("-v", "--verbose", action="store_true", help="print output")
    parser.add_argument("--input", type=str, default="data/input.jpg", help="input image file")
    parser.add_argument("--output", type=str, default="data/output.txt", help="output text file")
    parser.add_argument("--thresh", type=int, default=150, help="used for thresholding image")
    parser.add_argument("--maxval", type=int, default=255, help="used for Thresholding image")
    args = parser.parse_args()
    return args

def set_tesseract_cmd(tesseract_cmd):
    pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
    print("pytesseract supports languages:", pytesseract.get_languages(config='.'))

def img2txt(verbose, image, thresh, maxval, output):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, thresh, maxval, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(binary_image, lang = "eng+chi_sim")
    if (verbose):
        print("text:\n", text)
    with open(output, "w", encoding="utf-8") as output_file:
        output_file.write(text)

if __name__ == "__main__":
    args = parse_args()
    if (args.verbose):
        print("args:\n", args)

    with open("config.yml", "r") as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)
    if (args.verbose):
        print("config.yml\n", data)
    set_tesseract_cmd(data.get("tesseract_cmd"))

    image = cv2.imread(args.input)
    img2txt(args.verbose, image, args.thresh, args.maxval, args.output)