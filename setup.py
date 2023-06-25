from setuptools import find_packages, setup

with open("./README.md", "r") as file:
    long_description = file.read()
with open("./requirements.txt") as file:
    requirements = file.readlines()
with open("./LICENSE") as file:
    license = file.read()
setup(
    name="bahire-hasab",
    author="Hundera Awoke",
    version="0.2.8b",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author_email="hunderaweke@gmail.com",
    url="https://github.com/hunderaweke/bahire-hasab",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=requirements,
    keywords="bahire_hasab",
    entry_points={
        "console_scripts": [
            "bahire-hasab=bahire_hasab.__main__:main",
        ]
    },
    license=license,
)
