from setuptools import setup
setup(
    name = 'gitcfg',
    version = '0.1.0',
    packages = ['gitcfg'],
    entry_points = {
        'console_scripts': [
            'gitcfg = gitcfg.__main__:main'
        ]
    })