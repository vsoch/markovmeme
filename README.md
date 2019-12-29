# Markov Meme

[![PyPI version](https://badge.fury.io/py/markovmeme.svg)](https://pypi.org/project/markovmeme/)
[![GitHub actions status](https://github.com/vsoch/markovmeme/workflows/ci/badge.svg?branch=master)](https://github.com/vsoch/markovmeme/actions?query=branch%3Amaster+workflow%3Aci)

Wouldn't it be great to generate themed memes with Markov Models? Or just randomly
generated text? I think so too.

## Usage

### Install

You can install from pypi

```bash
pip install markovmeme
```

or install from the repository directly:

```bash
$ git clone https://github.com/vsoch/markovmeme
$ python setup.py install
```

## Usage

You can see the basic usage as follows. Basically, there is a "generate" command:

```bash
$ markov-meme 
usage: markov-meme [-h] {generate} ...

Markov Meme Generator

optional arguments:
  -h, --help  show this help message and exit

actions:
  actions for Markov Meme Generator

  {generate}  markovmeme actions
    generate  generate a meme
```

You can see the corpus available by looking at the generate help:

```bash
$ markov-meme generate --help
usage: markov-meme generate [-h] [--outfile OUTFILE] [--fontsize FONTSIZE]
                            [--font {OpenSans-Regular,Pacifico-Regular,Anton-Regular}]
                            [--corpus {hamlet,dr_seuss,trump_speech,the_office,office/stanley,office/toby,office/meredith,office/holly,office/creed,office/oscar,office/deangelo,office/david,office/dwight,office/kelly,office/phyllis,office/jim,office/nellie,office/gabe,office/clark,office/roy,office/karen,office/michael,office/andy,office/charles,office/kevin,office/pam,office/ryan,office/erin,office/robert,office/darryl,office/pete,office/jan,office/jo,office/angela}]
                            [--custom-corpus CUSTOM_CORPUS]
                            [--image CUSTOM_IMAGE] [--no-model]

optional arguments:
  -h, --help            show this help message and exit
  --outfile OUTFILE     the output file to save the image (defaults to
                        randomly generated png)
  --fontsize FONTSIZE   font size of text (if desired) defaults to 16
  --font {OpenSans-Regular,Pacifico-Regular,Anton-Regular}
                        choice of font (defaults to open sans)
  --corpus {hamlet,dr_seuss,trump_speech,the_office,office/stanley,office/toby,office/meredith,office/holly,office/creed,office/oscar,office/deangelo,office/david,office/dwight,office/kelly,office/phyllis,office/jim,office/nellie,office/gabe,office/clark,office/roy,office/karen,office/michael,office/andy,office/charles,office/kevin,office/pam,office/ryan,office/erin,office/robert,office/darryl,office/pete,office/jan,office/jo,office/angela}
                        the corpus to use to generate the meme, matches to
                        images.
  --custom-corpus CUSTOM_CORPUS
                        A custom corpus file, full path
  --image CUSTOM_IMAGE  A custom image file, full path
  --no-model            Don't generate a sentence from corpus, just randomly
                        select sentence.
```

### Random Generation

To generate a meme from a random corpus, you can just run:

```bash
$ markov-meme generate
```

If the randomly selected corpus doesn't have matching images, you'll see

```bash
No images exist for corpus office/clark. Please specify --image.
```

### Corpus and Image Selection

And you can run the same command again, or specify a specific corpus and image.

```bash
$ markov-meme generate --corpus office/michael --image markovmeme/data/images/office/michael1.png
```

The same can be done for specifying a custom corpus, which should be a text file with lines
to generate the model from.

```bash
$ markov-meme generate --custom-corpus markovmeme/data/corpus/office/michael.txt --image markovmeme/data/images/office/michael2.png
```

### Skip Model

If you don't want to use a model (and want real lines from some corpus) add `--no-model`

```bash
$ markov-meme generate --no-model
```

## Interactive Python
For the most part, text size and number of characters are limited to fit reasonable within
1-3 lines. If you want to customize or otherwise play around with this, you can interact
with the class directly:

```python
from markovmeme.main import MemeImage
from markovmeme.text import generate_text

# corpus is absolute path, or relative to module's data/corpus folder
corpus = "office/michael"

text = generate_text(corpus=corpus, use_model=True, size=10)

# Set image to full path, or None to select based on corpus
meme = MemeImage(image=None, corpus=corpus)

# Add text generated, centered on top
meme.write_text(text, fontsize=args.fontsize, font=font)

# Leave outfile as None to generate random name
meme.save_image(None)
```

## Support

Do you have a question? Or want to suggest a feature to make it better?
Please [open an issue!](https://www.github.com/vsoch/markovmeme)
