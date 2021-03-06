import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chefboost",  
    version="0.0.1",
    author="Sefik Ilkin Serengil",
    author_email="serengil@gmail.com",
    description="Lightweight Decision Tree Framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/serengil/chefboost",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["pandas", "numpy", "tqdm"]
)
