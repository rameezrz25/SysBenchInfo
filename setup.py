from setuptools import setup, find_packages

setup(
    name="SysBenchInfo",
    version="0.1.2",
    description="A package to get system information and benchmark CPU and GPU for all operating systems",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="rameezrz25",
    author_email="rameezrz25@gmail.com",
    url="https://github.com/rameezrz25/SysBenchInfo",
    packages=find_packages(),
    install_requires=[
        "psutil",
        "GPUtil",
        "tabulate",

    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
