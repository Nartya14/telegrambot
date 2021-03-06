# Разработка бота в Telegram

### Содержание
1. [Общие сведения](#Общие-сведения)
2. [Описание команд](#Описание-команд)
3. [Методика расчёта](#Методика-расчёта)

### Общие сведения
Проект "Чат-бот Jimmi" создан на Python для Telegram Bot API. Jimmi предназначен для подсчёта индекса соответствия выполненной задачи согласно перечню глобальных целей работы отдела.

### Описание команд
Данный бот имеет меню с 2 командами:
<br>
/start - начало работы с ботом;
<br>
/help - подсказка, раскрывающая определение глобальных целей.

### Методика расчёта
Индекс соответствия рассчитывается по 7 глобальным целям:
<br>
1. Субъектная оптимизация
2. Иерархическая оптимизация
3. Функциональная оптимизация
4. Информационная автономность процессов
5. Централизация информации
6. Автоматизация процессов
7. Документация процессов
 <br>
 Ответом на вопрос является цифра:
 <br>
 0 - не соответствует требованиям;
 1 - частично соответствует;
 2 - полностью не соответствует.
