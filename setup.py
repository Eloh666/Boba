from setuptools import setup, find_packages

install_requires = [
    "aiohttp",
]

dev_requires = [
    "autopep8",
    "black",
    "pip-tools",
]

setup(
    name="Boba",
    version="0.0.1",
    author="Mr Boba",
    author_email="eloh666@gmail.com",
    description="Mini-wrapper for the twitter API",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=install_requires,
    python_requires=">=3.9",
    setup_requires=["pytest-runner"],
    tests_require=dev_requires,
    extras_require={"dev": dev_requires},
)
