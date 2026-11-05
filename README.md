# GiveMeQr

English | [Português (Brasil)](README.pt-br.md)

A terminal-based QR code generator written in Python. Enter a link, preview its QR code as ASCII art, and optionally save it as an image.

## Features

- Generate a single QR code or multiple QR codes in sequence.
- Preview QR codes directly in the terminal.
- Export black QR codes on a white background.
- Generate filenames containing the date, time, and a random number.
- Optionally open images after saving them.
- Reject empty input and handle errors when saving unsupported formats.

## Requirements

- Python 3 and `pip` available on your system.
- The dependency listed in `requirements.txt`: `qrcode[pil]`, which provides image support through Pillow.
- An image viewer if you want to open generated images from the program.

## Installation and execution

Download the project from GitHub or clone the repository. Open a terminal in the folder containing `geraqr.py` and `requirements.txt`.

### Windows (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe geraqr.py
```

If the `py` command is unavailable, use `python` in the first command instead.

### Linux and macOS

```bash
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python geraqr.py
```

These commands use the virtual environment's Python interpreter directly, so activation is not required. On Linux, if environment creation reports that the `venv` module is unavailable, install the corresponding package for your distribution and try again.

## Usage

The program's prompts are in Portuguese. Answer `s` for yes ("sim") and `n` for no. Use `fim` to finish entering a list of links.

### Generate a single QR code

1. Run the program.
2. Answer `n` to the first question, which asks whether you want to generate multiple QR codes in sequence.
3. Enter your link.
4. View the QR code in the terminal.
5. Answer `s` to save it as an image, or `n` to exit without saving.
6. If saving, enter an image format, such as `png`.
7. After saving, answer `s` if you want to open the image.

### Generate multiple QR codes

1. Run the program and answer `s` to the first question.
2. Enter one link at a time, pressing Enter after each one.
3. Type `fim` to finish the list, without the asterisks shown in the prompt.
4. The program generates QR codes in the order entered and asks separately whether to save each one.

### Example input

To generate a single QR code and save it as a PNG without opening the image, provide these answers to the prompts, one at a time:

```text
n
https://example.com
s
png
n
```

## Generated files

Images are saved in the directory from which you run the program, which may differ from the script's directory. The full path is displayed after saving.

Example filename:

```text
qr_2026-01-15_14-30-00-123456.png
```

The prompt lists `PNG`, `JPEG`, `GIF`, `BMP`, `WEBP`, `TIFF`, and `ICO`. Saving depends on Pillow's support for the format and image mode; the program reports any save error. Try `png` first.

## Notes

- The program rejects empty input but does not validate whether the content is a URL or whether the address is reachable.
- You can also enter plain text instead of a link.
- Terminal previews may vary depending on the font, colors, and available space. Use the saved image if needed.
- Opening images automatically depends on your environment and the image viewer available on your system.

## Project structure

```text
GiveMeQr/
├── geraqr.py         # Program and terminal interaction
├── requirements.txt  # Project dependency
├── README.md         # English documentation
└── README.pt-br.md   # Brazilian Portuguese documentation
```

## Author

[Leonardo Cargnelutti Mello](https://github.com/LeonardoCargneluttiMello)
