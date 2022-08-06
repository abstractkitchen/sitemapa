from setuptools import setup, find_packages
from pathlib import Path

VERSION = '0.1.4'
DESCRIPTION = 'Create advanced sitemaps easily'

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


# Setting up
setup(
    name="sitemapa",
    version=VERSION,
    author="Dmitry S.",
    author_email="<dmitry@abstractkitchen.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[],
    url='https://abstractkitchen.com/blog/sitemaps-for-devs/',
    keywords=['python', 'sitemap', ''],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3"
    ]
)