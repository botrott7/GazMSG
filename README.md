# GazMSG
Python-скрипт, который извлекает вложения из файлов сообщений (.msg), сохраняя вложения в указанную директорию.

Инструкция по использованию GazMSG

Требования:

* Python 3.9.20 или выше
* Библиотека extract-msg

Установка:
# Linux
# должен быть установлен git
# `apt-get install git`

1. git clone https://github.com/botrott7/GazMSG.git

2. заходим в директорию `cd GazMSG`

3. Устанавливаем виртуальное окружение Python (venv):

`python3 -m venv venv`

4. Активируйте виртуальное окружение:

`source venv/bin/activate`

5. Установите библиотеки extract-msg:
# использовалась extract-msg==0.52.0
`pip install extract-msg`

6. Запустить скрипт
`python main.py`

Использование:

* Создадутся две директории: files и results.
* Поместите файлы сообщений (.msg) в директорию files.
* Запустите скрипт main.py.
* Вложения, которые не являются файлами PNG, будут сохранены в директорию results.

