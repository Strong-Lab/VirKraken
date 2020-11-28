import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="VirKraken",
    version="0.0.5",
    author="Cody Glickman",
    author_email="glickman.cody@gmail.com",
    description="An extension to Kraken2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Strong-Lab/VirKraken",
    scripts=['bin/virkraken'],
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['pandas', 'scikit-learn', 'biopython', 'importlib-resources'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
