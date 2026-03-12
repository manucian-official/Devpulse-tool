from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="devpulse-tool",
    version="1.0.0",
    description="DevPulse - AI powered code scanner and developer productivity tool",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="Manucian Official",
    author_email="khoigaming2102pro@gmail.com",

    url="https://github.com/manucian-official/devpulse",

    project_urls={
        "Source": "https://github.com/manucian-official/devpulse",
        "Tracker": "https://github.com/manucian-official/devpulse/issues",
    },

    license="MIT",

    packages=find_packages(exclude=("tests", "docs")),

    include_package_data=True,

    install_requires=[
        # future dependencies
    ],

    entry_points={
        "console_scripts": [
            "devpulse=devpulse.cli:main",
        ],
    },

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Quality Assurance",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",

        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    python_requires=">=3.8",
)