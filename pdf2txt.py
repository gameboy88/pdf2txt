#!/usr/bin/env python

import argparse
import cv2
import pdf2image
import pypdf, PyPDF2
import yaml
from PIL import Image
from img2txt import img2txt, set_tesseract_cmd

def parse_args():
    parser = argparse.ArgumentParser("PDF to Text")
    parser.add_argument("-v", "--verbose", action="store_true", help="print output")
    parser.add_argument("--type", default="text", help="content type of pdf file: text or image")
    parser.add_argument("--input", type=str, default="data/input.pdf", help="input pdf file")
    parser.add_argument("--output", type=str, default="data/page", help="prefix name of output files")
    parser.add_argument("--thresh", type=int, default=150, help="used for thresholding image")
    parser.add_argument("--maxval", type=int, default=255, help="used for Thresholding image")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_args()
    if (args.verbose):
        print("args:\n", args)

    if args.type == "text":
        reader = pypdf.PdfReader(args.input)
        number_of_pages = len(reader.pages)
        if (args.verbose):
            print("total pages:", number_of_pages)

        for i in range(0, number_of_pages):
            page = reader.pages[i]
            text = page.extract_text()
            if (args.verbose):
                print("\n== page", i+1, "==\n", text)
            with open(f"{args.output}_{i + 1}.txt", "w", encoding="utf-8") as output_file:
                output_file.write(text)
    elif args.type == "image":
        with open("config.yml", "r") as f:
            data = yaml.load(f, Loader=yaml.SafeLoader)
        if (args.verbose):
            print("config.yml\n", data)

        images = pdf2image.convert_from_path(args.input, poppler_path = data.get("poppler_path"))
        set_tesseract_cmd(data.get("tesseract_cmd"))

        for i, image in enumerate(images):
            image.save(f"{args.output}_{i + 1}.jpg", "JPEG")
            image = cv2.imread(f"{args.output}_{i + 1}.jpg")
            if (args.verbose):
                print("\n== page", i+1, "==\n")
            img2txt(args.verbose, image, args.thresh, args.maxval, f"{args.output}_{i + 1}.txt")
    else:
        print("please set correct type!")
