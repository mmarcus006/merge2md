# merge2md

A powerful tool to batch-convert various document formats to Markdown and merge them into a single document using [Docling](https://github.com/DS4SD/docling).

## Features

- **Multi-format support**: Convert PDF, Word (DOCX), PowerPoint (PPTX), HTML, CSV, Markdown, AsciiDoc, and image files
- **OCR support**: Extract text from scanned documents and images using EasyOCR
- **Batch processing**: Convert multiple files at once with parallel processing
- **Natural sorting**: Files are processed in natural order (e.g., file1, file2, file10)
- **Flexible output**: Export as Markdown (.md) or PDF (.pdf)
- **Customizable**: Configure OCR languages, DPI settings, and more

## Supported File Formats

- **PDF** (.pdf) - With optional OCR for scanned documents
- **Microsoft Word** (.docx)
- **Microsoft PowerPoint** (.pptx)
- **HTML** (.html, .htm)
- **CSV** (.csv) - Converted to Markdown tables
- **Markdown** (.md)
- **AsciiDoc** (.asciidoc, .adoc)
- **Images** (.png, .jpg, .jpeg, .gif, .bmp, .tiff) - With OCR support

## Installation

```bash
pip install merge2md
```

Or install from source:

```bash
git clone https://github.com/yourusername/merge2md.git
cd merge2md
pip install -e .
```

## Usage

### Command Line

Basic usage:
```bash
python -m merge2md document1.pdf document2.docx -o merged.md
```

Convert multiple file types and export as PDF:
```bash
python -m merge2md *.pdf *.docx *.html -o combined.pdf --title "My Documents"
```

With OCR in multiple languages:
```bash
python -m merge2md scanned*.pdf --lang en --lang es --lang fr -o output.md
```

Disable OCR for faster processing:
```bash
python -m merge2md *.pdf --no-ocr -o output.md
```

Using glob patterns:
```bash
python -m merge2md "reports/*.pdf" "docs/*.docx" -o all_docs.md --threads 8
```

### Python API

```python
from pathlib import Path
from merge2md import convert_and_merge, ConversionSettings

# Basic usage
paths = [Path("doc1.pdf"), Path("doc2.docx"), Path("doc3.html")]
convert_and_merge(paths, Path("output.md"), title="Merged Documents")

# With custom settings
settings = ConversionSettings(
    ocr=True,
    languages=["en", "es"],
    dpi=400,  # Higher DPI for better OCR quality
)
convert_and_merge(paths, Path("output.pdf"), settings=settings)

# Using the converter directly
from merge2md import DoclingMarkdownConverter

converter = DoclingMarkdownConverter(settings)
markdown_blocks = converter.to_markdown(paths)
for md in markdown_blocks:
    print(md)
```

## Configuration Options

### ConversionSettings

- `ocr` (bool): Enable/disable OCR processing (default: True)
- `languages` (list): OCR languages to use (default: ["en"])
- `dpi` (int): DPI for processing images/PDFs (default: 300)
- `allowed_formats` (list): Limit which file formats to process

### Command Line Options

- `-o, --output`: Output file path (default: merged.md)
- `--title`: Add a title to the merged document
- `--threads`: Number of parallel workers (default: 4)
- `--lang`: OCR language (can be specified multiple times)
- `--no-ocr`: Disable OCR processing

## Examples

### Convert a Mix of Documents

```bash
# Convert PDFs, Word docs, and web pages into a single report
python -m merge2md \
    report_*.pdf \
    meeting_notes.docx \
    research.html \
    data.csv \
    -o final_report.pdf \
    --title "Q4 2024 Report"
```

### Process Scanned Documents

```bash
# Extract text from scanned PDFs in multiple languages
python -m merge2md \
    scanned_contract_*.pdf \
    --lang en --lang de \
    --dpi 600 \
    -o contracts.md
```

### Batch Convert Research Papers

```bash
# Convert all PDFs in a directory, maintaining natural order
python -m merge2md papers/*.pdf -o literature_review.md --threads 8
```

## Requirements

- Python 3.8+
- [Docling](https://github.com/DS4SD/docling)
- [pypandoc](https://github.com/bebraw/pypandoc) (optional, for PDF export)
- pandoc (optional, for PDF export without pypandoc)

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
