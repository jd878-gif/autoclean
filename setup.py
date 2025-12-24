from setuptools import setup, find_packages

setup(
    name="autoclean",
    version="0.1.0",
    author="Jeet Dave",
    author_email="jd.878@njit.edu",
    description="Automated data cleaning library for pandas DataFrames",
    long_description=open("readme.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jd878-gif/autoclean",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.3",
        "numpy>=1.20"
    ],
    python_requires=">=3.8",
)
