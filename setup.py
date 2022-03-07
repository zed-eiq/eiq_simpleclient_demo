import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eiq_simpleclient_demo",
    version="0.1.0",
    author="EclecticIQ B.V.",
    author_email="wtan@eclecticiq.com",
    description="""Simple Python REST API client for the
EclecticIQ Intelligence Center.""",
    url="https://github.com/zed-eiq/ic-api-simple-client",
    project_urls={
        "Bug Tracker": "https://github.com/zed-eiq/ic-api-simple-client/issues",
        },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2.0 License",
        "Private :: Do Not Upload",
        ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        "requests~=2.23",
        "furl~=2.1",
        "python-dotenv~=0.19",
    ],
)
