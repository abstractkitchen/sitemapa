from setuptools import setup, find_packages

VERSION = '0.1.1'
DESCRIPTION = 'Create advanced sitemaps easily'
LONG_DESCRIPTION = """
Sitemapa is a small package to reduce your work while generating sitemaps. You describe your sitemaps with JSON-structure. Sitemapa is framework agnostic and not indexing your website — it's just generating sitemaps from your description. Noting more. I use it to generate sitemaps for millions of URLs on my websites.
"""

# Setting up
setup(
    name="sitemapa",
    version=VERSION,
    author="Dmitry S.",
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