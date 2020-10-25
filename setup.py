import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fpgrowth_py",
    version="1.0.0",
    author="Chonyy",
    author_email="tcheon8788@gmail.com",
    description="Python implementation of FP Growth algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chonyy/fpgrowth_py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
