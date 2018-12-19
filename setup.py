import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'proxy_bouncer',
    version = '0.0.0',
    author = 'Dane Morgan',
    author_email = 'danemorgan91@gmail.com',
    description = 'scraps proxys from an online list then returns and logs a list of valid and anon proxies',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/deadlift1226/',
    install_requires = ['requests', 'bs4',], #3rd party pip packages
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

