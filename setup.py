import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stat_arb_tools",
    version="0.0.5",
    author="Adam Hanna",
    author_email="ahanna@mba2016.hbs.edu",
    description="This package provides statistics arbitrage tools for traders",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/devnull-capital/stat_arb_tools",
    packages=["stat_arb_tools"],
    install_requires=["scipy", "numpy", "statsmodels", "numpydoc"],
    test_suite='nose.collector',
    tests_require=['nose', 'pandas'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
