from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []
# "ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="FaceAsPy",
    version="0.0.1",
    author="Hubert Kompanowski",
    author_email="hubert.kompanowski9@gmail.com",
    description="Package with some face recognition features.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Py-For-All/FaceAsPy",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)