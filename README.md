# Random-data

[![Build Status](https://travis-ci.com/daveusa31/random_data.svg?branch=master)](https://travis-ci.com/daveusa31/random_data)
[![PyPi Package Version](https://img.shields.io/pypi/v/random_data.svg?style=flat-square)](https://pypi.python.org/pypi/random_data)
[![PyPi status](https://img.shields.io/pypi/status/random_data.svg?style=flat-square)](https://pypi.python.org/pypi/random_data)
[![Downloads](https://pepy.tech/badge/random-data)](https://pepy.tech/project/random-data)
[![Supported python versions](https://img.shields.io/pypi/pyversions/random_data.svg?style=flat-square)](https://pypi.python.org/pypi/random_data)
[![repository size](https://img.shields.io/github/repo-size/daveusa31/random_data)](https://github.com/daveusa31/random_data)
[![DeepSource](https://static.deepsource.io/deepsource-badge-light-mini.svg)](https://deepsource.io/gh/daveusa31/random_data/?ref=repository-badge)

## Установка и использование:
```sh 
pip install random-data
```

```python 
import random_data

print(random_data.russian.names.male()) # Получаем мужское имя
print(random_data.russian.surnames.male()) # Получаем мужскую фамилию

print(random_data.russian.names.female()) # Получаем женское имя
print(random_data.russian.surnames.male()) # Получаем женскую фамилию

print(random_data.etc.uuid()) # Генерируем uuid
print(random_data.etc.password()) # Пароль из букв и цифр. Можно указать нужную длину


```

# To do
- [X] Добавить больше русских мужских фамилий 30.06.20