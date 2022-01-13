from setuptools import setup
setup(
    name = 'git-config',
    version = '0.1.0',
    packages = ['git-config'],
    entry_points = {
        'console_scripts': [
            'git-config = git-config.__main__:main'
        ]
    })