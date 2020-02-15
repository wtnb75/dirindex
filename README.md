# Install

- pip install dirindex

# Usage

```
# dirindex --help
Usage: dirindex [OPTIONS] COMMAND [ARGS]...

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  make
  read-resource
```

## make directory index

```
# dirindex make --help
Usage: dirindex make [OPTIONS] DIRECTORY

Options:
  --verbose / --no-verbose
  --template TEXT
  --dry / --no-dry              [default: False]
  --recursive / --no-recursive  [default: False]
  --single / --no-single        [default: False]
  --pattern TEXT                [default: *]
  --hide TEXT
  --filename TEXT               [default: index.html]
  --help                        Show this message and exit.
```

create Apache style directory index

- dirindex make --template apache /path/to/directory
- open /path/to/directory/index.html
- [built-in styles](dirindex/templates/)
- template
    - Jinja2
    - arguments... dirindex make --dry --template /dev/null /path/to/directory --filename - --verbose

# Links

- [pypi](https://pypi.org/project/dirindex/)
- [coverage](https://wtnb75.github.io/dirindex/)
- ~~[local pypi repo](https://wtnb75.github.io/dirindex/dist/)~~
