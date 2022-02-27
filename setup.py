import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="curry_fabric",
    version="0.0.1",
    author="Sofya Dobychina",
    author_email="sf@contextmachine.ru",
    description="_",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sf-d/curry_fabric",
    project_urls={
        "Bug Tracker": "https://github.com/sf-d/curry_fabric/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)