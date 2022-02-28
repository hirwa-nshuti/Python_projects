# Python Dictionary

Webster's Unabridged Dictionary

## Dataset used

Json scrapped file: [Matt Reagan](https://github.com/matthewreagan/WebstersEnglishDictionary)

Original text file: [Gutenberg Project](https://www.gutenberg.org/ebooks/29765)
Licenced under:

### License for project Gutenberg Project, i.e. dictionary.txt

> This eBook is for the use of anyone anywhere at no cost and with
> almost no restrictions whatsoever.  You may copy it, give it away or
> re-use it under the terms of the Project Gutenberg License included
> with this eBook or online at [www.gutenberg.net](www.gutenberg.net)

## Data used

|Data|Type|Source|
|----|-----|----|
|dictionary original dataset| .txt|[Gutenberg Project](https://www.gutenberg.org/ebooks/29765)|
|scrapped dictionary Json dataset| .json|[Matt Reagan](https://github.com/matthewreagan/WebstersEnglishDictionary)|

## Usage

This is a CLI based program to use it you need to download clone the repository:

```bash
git clone git@github.com:hirwa-nshuti/Python_projects.git
```

Then move to the project directory

```bash
cd Dictionary
```

Activate your virtual environment and run the command:

```bash
python DictionaryApp "word to translate"
```

This is overview of help command line of the project.

```bash
python DictionaryApp -h
```

usage: DictionaryAPP [options] : word

Definition of different words

positional arguments:
  word        Word to search in Dictionary

optional arguments:
  -h, --help  show this help message and exit

Thanks for using our dictionary

## References

* [Gutenberg Project](https://www.gutenberg.org/ebooks/29765)
* [Matt Reagan](https://github.com/matthewreagan/WebstersEnglishDictionary)
