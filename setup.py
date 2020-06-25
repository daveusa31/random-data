import os
import setuptools

import random_data as lib




if "requirements.txt" in os.listdir("."):
    with open("requirements.txt", encoding="utf-8") as r:
        requires = [i.strip() for i in r] # Зависимости
else:
    requires = []



setuptools.setup(
    name=lib.name,
    version=lib.__version__,
    author=lib.__author__,
    author_email="strelok.127@yandex.ru",
    include_package_data=True,
    python_requires=">=3.5",
    install_requires=requires,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: Russian",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    project_urls={"Source": lib.__source__},
    packages=setuptools.find_packages(),
)