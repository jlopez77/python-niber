import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nibe", # Replace with your own username
    version="0.0.1",
    author="jlopez77",
    author_email="jaloso@gmail.com",
    description="Poorly coded I-de unofficial API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jlopez77/iberdrola_scrapper"
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
