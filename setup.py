from setuptools import setup, find_packages

setup(
    name="autoclean-jeet",  # use unique name if autoclean taken
    version="0.1.0",
    author="Jeet Dave",
    description="Automated data cleaning library for pandas DataFrames",
    long_description=open("readme.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.3",
        "numpy>=1.21"
    ],
    python_requires=">=3.8",
)
