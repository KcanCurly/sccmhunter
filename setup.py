from setuptools import setup, find_packages

setup(
    name="sccmhunter",
    version="1.0.0",
    author="KcanCurly",
    description="The ldap2json script allows you to extract the whole LDAP content of a Windows domain into a JSON file..",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KcanCurly/sccmhunter",
    packages=find_packages(),
    install_requires=[
        "cmd2",
        "cryptography",
        "impacket",
        "ldap3",
        "pandas",
        "pyasn1",
        "pyasn1_modules",
        "Requests",
        "requests_ntlm",
        "requests_toolbelt",
        "rich",
        "tabulate",
        "typer",
        "urllib3",
        "pyopenssl",
        "pycryptodome"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "sccmhunter.py=sccmhunter.py:main"
        ],
    },
)