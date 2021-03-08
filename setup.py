from setuptools import setup

setup(
    name='emotions',
    packages=['emotions'],
    include_package_data=True,
    install_requires=[
        'flask',
        'pandas',
        'numpy',
        'matplotlib',
        'nltk',
        'flask',
    ],
)