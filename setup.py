import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kineticmodels",
    version_config=True,
    setup_requires=["setuptools-git-versioning"],
    author="Pau Cabaneros",
    author_email="pau.cabaneros@gmail.com",
    description="tool including most used function.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/paucablop/fermentation.kinetic.models",
    project_urls={
        "Bug Tracker": "https://github.com/paucablop/fermentation.kinetic.models/issues/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.10",
    install_requires=[
        "numpy>=1.23.2",
    ],
)
