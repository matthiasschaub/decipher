# Decipher Hoon Runes and Standard Library

A tool to convert Markdown documentation files of Hoon Runes and Standard Library found at the [developers.urbit.org](https://developers.urbit.org) site to Vim help files.

For the result see [hoon-runes.vim](https://git.sr.ht/~talfus-laddus/hoon-runes.vim) and [hoon-stdlib.vim](https://git.sr.ht/~talfus-laddus/hoon-stdlib.vim).

Reach out to `~talfus-laddus` on Urbit for anything related to this tool.

## Installation

```
pipx install git+https://git.sr.ht/~talfus-laddus/decipher
```

## Usage

```
$ decipher --help
Usage: decipher [OPTIONS] COMMAND [ARGS]...

Options:
  -l, --log-level TEXT
  --version             Show the version and exit.
  --help                Show this message and exit.

Commands:
  run      Decipher a single markdown file.
  run-all  Decipher all markdown files in a directory.
```

A single markdown file:

```
$ decipher run --type rune bar.md
```

All markdown files in a directory.

```
$ decipher run-all --type rune .
```

The name (runes) and order of those files are hard-coded.

## Development Setup

Dependencies:
- Python > 3.10
- Poetry > 1.0
