import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cli_helper_DM_MS", # Replace with your own username
    version="1.0.0",
    author="dmitrii_malii_and_misha_sid",
    author_email="dmitrii.malii@gmail.com, mishasydorchuk@gmail.com",
    description="Command line personal helper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    entry_points={'console_scripts': ['cli_helper = cli_helper.main:main']}
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "cli_helper"},
    packages=setuptools.find_packages(where="cli_helper"),
    python_requires=">=3.6",
)
