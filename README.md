# PDF Halver

A simple Python script using the `pypdf` library to split PDF pages in half.

## Usage

1. Install the required library:

    pip install pypdf
    
2. Run the script:

    python pdfpagesplit.py
    
   Ensure that you have an input PDF named `input.pdf` in the same directory, and the script will generate an output PDF named `output.pdf` with pages split in half.

## How it works

The script processes each page of the input PDF, splitting it into left and right halves. It then creates a new PDF with these modified pages, resulting in a document where each original page is divided into two.

## Dependencies

- [pypdf](https://pypi.org/project/pypdf/): A Python library for reading and writing PDF files.

## Notes

- Make sure to backup your original PDF before using this script, as it modifies the structure of the pages.

Feel free to contribute, report issues, or suggest improvements!
