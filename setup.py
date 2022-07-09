try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Exercise 49',
    'author': 'Ben Heavner',
    'url': 'URL for this project',
    'download_url': 'download URL',
    'author_email': 'bheavner@gmail.com',
    'version': '0.1',
    'install_requires': [''],
    'packages': ['ex_49'],
    'scripts': [],
    'name': 'Exercise 49'
}

setup(**config)

