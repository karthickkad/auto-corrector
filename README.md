# Auto Corrector

This Python script performs automatic spelling correction and sentence-level tokenization on input text. It uses the `spaCy` library for sentence segmentation and `TextBlob` for spelling correction.

## Features

- Splits input paragraph into sentences.
- Corrects spelling errors in each sentence.
- Joins corrected sentences back into a paragraph.
- Capitalizes the first letter of each corrected sentence.

## Requirements

- Python 3.x
- spaCy
- TextBlob
- spaCy English language model (`en_core_web_sm`)

## Installation

```bash
pip install spacy textblob
python -m spacy download en_core_web_sm
