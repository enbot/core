from setuptools import setup

setup(
    name='core',
    packages=['core'],
    include_package_data=True,
    install_requires=[
        'nltk',
        'flask',
        'python-aiml',
    ],
)
