# Tinkoff_ML_DL_plagiat
Tinkoff ML and DL in January 2023. Code compare two files and return plagiat score
Описание задачи
1 задание
Антиплагиат
Напишите утилиту для антиплагиата, которая сравнивает два текста программ на Python и выдает оценку их похожести.



Решать можно любым способом. Единственное ограничение — можно использовать только встроенные библиотеки Python и библиотеки, указанные ниже. Для поступления на ML достаточно решить задачу с использованием расстояния Левенштейна или любым другим способом.



Возможный вариант решения
Предлагается следующий простой и эффективный метод — расстояние Левенштейна. Это расстояние оценивает минимальное число вставок, удалений или замен символов, необходимых для преобразования одного текста в другой. Предполагается, что близкие тексты имеют много одинаковых кусков и получить один текст из другого можно небольшим количеством редакционных операций. Чтобы расстояние не зависело от длины текста, можно разделить редакционное расстояние на длину текста.



Прежде, чем оценивать расстояние, полезно нормализовать (предобработать) текст. Для этого можно использовать стандартную библиотеку ast. Эта библиотека позволяет выполнить синтаксический разбор Python кода. В результате библиотека выдает дерево со структурой программы, по которому можно эффективно сделать замены имен переменных, упростить docstrings или аннотации функций. Начиная с версии Python 3.9, синтаксическое дерево можно конвертировать обратно в код. 



В этом методе можно использовать библиотеку Numpy.







Данные
Для подбора параметров модели мы предлагаем корпус текстов. Скачать его можно

п

о ссылке



.



В папке files лежат исходные тексты программ, в папках plagiat1 и plagiat2 можно найти программы, полученные из исходных разными преобразованиями. Тестироваться алгоритм будет на документах, обработанных аналогичным образом.



Интерфейс
Нужно реализовать скрипт compare.py, который принимает файл со списком пар документов и путь до выходного файла. Скрипт должен сравнить пары документов и записать в выходной файл оценки похожести текстов программ.



Пример 

запуска:





python3 compare.py input.txt scores.txt


Пример

 входного файла input.txt:





files/main.py plagiat1/main.py
files/loss.py plagiat2/loss.py
files/loss.py files/loss.py


Пример

 выходного файла scores.txt:





0.63
0.84
0.153


Детали реализации
Создайте репозиторий на гитхабе, залейте туда код и вставьте ссылку в форму. Задание творческое. Нам интересно оценить ваши знания питона и общее умение программировать. Не дописали до конца — не страшно, отправляйте, что есть.



Несколько замечаний:

Удобно реализовать консольный интерфейс через argparse
Для анализа кода можно использовать библиотеку ast
Для работы с текстами может пригодиться библиотека регулярных выражений re
Соблюдайте, пожалуйста, pep8. Пишите хороший код. Следуйте принципам ООП
Для сохранения обученной модели удобно использовать pickle или dill
Создайте только файл compare.py, при необходимости train.py и model.pkl
Нельзя использовать внешние библиотеки. Пользуйтесь тем, что есть по умолчанию в питоне, и тем, что указано в секциях выше
