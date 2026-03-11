from setuptools import setup, find_packages

setup(
    name="devpulse-tool",
    version="1.0.0",
    description="DevPulse - AI powered code scanner and developer productivity tool",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Manucian-Official",
    author_email="khoigaming2102pro@gmail.com",
    url="https://github.com/manucian-official/devpulse",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
            "devpulse=devpulse.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
