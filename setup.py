from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="pipackager",
    version="0.4.7",
    packages=find_packages(),
    install_requires=[
        "twine",
        "setuptools",
        "wheel",
        "flake8",
        "black",
        "pytest",
        "pip-upgrader",
    ],
    entry_points={
        "console_scripts": [
            "pipackager=pipackager.cli:main",
            # Ensure no duplicates like:
            # 'pipackager=pipackager.cli:main',
            # 'another_command=another.module:main_function',
        ],
    },
    author="rUv",
    author_email="your-email@example.com",
    description="pipackager is a comprehensive tool designed to manage your PyPI package, simplifying tasks such as cleaning old distributions, building new ones, uploading to PyPI, version incrementing, and more.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ruvnet/pipackager",
    license="Apache License 2.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
