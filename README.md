# Add borders to `.odt`
A Python script which adds borders to all tables of a given `.odt` file

## Motivation
As [Pandoc](https://pandoc.org/) doesn't add borders to it's generated tables when converting from Markdown to `.pdf`/`.docx`/`.odt`, I had to write down this script to do it instead.

In its current state, it doesn't let you customize it in any way, it adds full borders to all the tables of a given `.odt` document, no exception made. If you'd like to modify it to suit your needs, feel free to do so.

## Requirements

- Python 3

## Usage

### Standalone script
**If you just want to add tables to an `.odt` file**

`python3 addBorders.py <file-to-convert>`

Example:
If I wanted to add borders to `file.odt`:

`python3 addBorders.py file.odt`

And `file_new.odt` will be the same file with borders in its tables.

**It also supports a second argument to name the output file**


### Docker image with Pandoc
**If you want to use it alongside Pandoc**
You'll need a Markdown file and an `.odt` template, as explained in Pandocs documentation.
You may also want to add some metadata to the Markdown file as explained in Pandocs documentation. Example:
```
---
title: My Title
author: Me
---
```

Build the image:

`docker build . -t pandoc-md-odt-borders:0.0.1`

Run the image from a directory with both your Markdown file and the template:

`docker run --rm -v "`pwd`:/data" pandoc-md-odt-borders:0.0.1 <INPUT-MD> <OUTPUT-ODT> <TEMPLATE-ODT>`

Your file should be named `<OUTPUT-ODT>_new.odt`.
