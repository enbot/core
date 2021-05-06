# Core
The core is the *`back-end`* of the applications that contains the emotions calculation and the generations of the text responses.

## Requirements
For this application a python environment is necessary:
* python: `3.8.9` or similar.
* pip: `20.2.3` or similar.

## Installation
Use the package manager [PIP](https://pip.pypa.io/en/stable/) to install the application dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Run the entry file and start the server locally:
```bash
python app.py
```

## Build
To generate a bundle of this project you can use the [pyinstaller](https://www.pyinstaller.org/) package. You can install it with the PIP package manager:
```bash
pip install pyinstaller
```

After the installation run the following command to create a bundle of this project:
```bash
pyinstaller app.py --name core --clean --add-data data;data
```

## Contributing
This application is part of a undergraduate thesis, and the projects will be read-only after they are completed. Unfortunately, no contributions will be accepted.

## License
[MIT](https://github.com/enbot/core/blob/master/LICENSE)
