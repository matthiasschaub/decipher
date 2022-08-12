# Decipher Hoon Runes

A tool to convert Markdown documentation files of Hoon Runes found at the [developers.urbit.org](https://developers.urbit.org) site to Vim help files.

For the result see [hoon-runes.vim](https://git.sr.ht/~talfus-laddus/hoon-runes.vim).

Reach out to `~talfus-laddus` on Urbit for anything related to this tool.

## Installation

```
pipx install git+https://git.sr.ht/~talfus-laddus/decipher
```

## Usage

```
$ decipher
Usage: decipher [OPTIONS] COMMAND [ARGS]...

Options:
  -l, --log-level TEXT
  --version             Show the version and exit.
  --help                Show this message and exit.

Commands:
  all-runes  Decipher all pre-defined rune documentation markdown files...
  rune       Decipher a single rune documentation markdown file.
```

A single markdown file:

```
$ decipher rune bar.md
```

All markdown files in current directory.

```
$ cd urbit.org/content/docs/hoon/reference/rune/
$ decipher all-runes
```

The name (runes) and order of those files are hard-coded.

## Development Setup

Dependencies:
- Python > 3.10
- Poetry > 1.0
