import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="paymeuz",
    version="0.2",
    author="rajab-murod",
    author_email="rajab.murod1995@gmail.com",
    description="paymeuz",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.5",
    install_requires=['requests', 'django', 'djangorestframework'],
    url="https://github.com/rajab-murod/paymeuz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
)
