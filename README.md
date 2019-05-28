# cookiecutter-python3

Cookiecutter template to create python3 package.


## Usage

```bash
$ pip install cookiecutter
$ cookiecutter https://github.com/thazelart/cookiecutter-python3
```

You will be prompted for basic info (your name, package name, etc.) which will be used in the template.

## Output
A basic python3 package with initialized tests

```
├── mypkg
│   ├── __main__.py
│   ├── packageutils
│   │   └── simple_example.py
│   └── utils
│       ├── args.py
│       └── logger.py
├── setup.cfg
├── setup.py
└── test
    ├── __init__.py
    └── test_simple_example.py
```

## Authors
[Thibault Hazelart](https://github.com/thazelart)

## License
[Aache 2.0](/LICENSE)
