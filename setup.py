from setuptools import setup, find_packages

with open("./README.md", "r") as file:
    long_description = file.read()
setup(
    name="bahire-hasab",
    author="Hundera Awoke",
    version="0.2.6",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email="hunderaweke@gmail.com",
    url="https://github.com/hunderaweke/bahire-hasab",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[],
    keywords="bahire_hasab",
)
