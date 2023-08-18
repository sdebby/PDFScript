# PDFScript

## Injecting javascript payload into pdf files

A usefull script for injecting js code into innocent pdf file, using pypdf library.

## Features:

This script will open the input file and the payload, and creates a new combind fil.

## requirnemts:

```bash
pip install pypdf
```

### Use
'payload.js' is the payload file

'installation.pdf' is the PDF file you want to inject
```bash
python PDFScript.py -i installation.pdf -p payload.js
```
## TODOs


## Feedback
If you have any feedback, please reach out at shmulik.debby@gmail.com