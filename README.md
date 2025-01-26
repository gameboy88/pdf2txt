# pdf2txt / img2txt

**pdf2txt** is a python tool that can be used to convert pdf content to text. 
It contains another tool **img2txt** that can be used to convert image content to text.

## Install External Packages

You need to install poppler and tesseract.
Configure these operating environments, and configure config.yml.

```yaml
    poppler_path: your_path\poppler\Library\bin
    tesseract_cmd: your_path\Tesseract-OCR\tesseract.exe
```

## Usage
You need to specify the input and output file locations.
The default input file is data/input.pdf or data/input.jpg,
and the output is data/output.txt or data/page_no.txt.

### Command and Parameters
```bash
pdf2txt.py [-h] [-v] [--type TYPE] [--input INPUT] [--output OUTPUT] [--thresh THRESH] [--maxval MAXVAL]
```

options:
  -h, --help       show this help message and exit\
  -v, --verbose    print output\
  --type TYPE      content type of pdf file: text or image\
  --input INPUT    input pdf file\
  --output OUTPUT  prefix name of output files\
  --thresh THRESH  used for thresholding image\
  --maxval MAXVAL  used for Thresholding image

```bash
img2txt.py [-h] [-v] [--input INPUT] [--output OUTPUT] [--thresh THRESH] [--maxval MAXVAL]
```

options:
  -h, --help       show this help message and exit\
  -v, --verbose    print output\
  --input INPUT    input image file\
  --output OUTPUT  output text file\
  --thresh THRESH  used for thresholding image\
  --maxval MAXVAL  used for Thresholding image
