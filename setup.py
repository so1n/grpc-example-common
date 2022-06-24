import setuptools  # type: ignore

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()

setuptools.setup(
    name="grpc_example_common",
    version="0.1.6",
    author="so1n",
    author_email="",
    description="grpc example common",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/so1n/grpc-example-common#/",
    packages=setuptools.find_packages(),
    install_requires=required,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
