from setuptools import setup, find_packages

VERSION = '0.1.0'
DESCRIPTION = 'Create advanced sitemaps easily'
LONG_DESCRIPTION = """
Describe your sitemaps with JSON description. No XML needed. URLs, Images, Videos and News are supported. 
You can easily add custom xml-properties and extra child tags. No extra dependencies.
"""

# Setting up
setup(
    name="sitemapa",
    version=VERSION,
    author="Dmitry",
    author_email="<dmitry@abstractkitchen.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],

    keywords=['python', 'sitemap', ''],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3"
    ]
)