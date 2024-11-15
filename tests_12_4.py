import logging
import unittest

# Первым делом необходимо добавить проверки на типы и значения
# в конструкторе класса Runner.


class Runner:
    def __init__(self, name, speed):
        if not isinstance(name, str):
            raise ValueError("Неверный тип данных для имени Runner")
        if speed < 0:
            raise ValueError("Неверная скорость для Runner")

        self.name = name
        self.speed = speed
        self.distance = 0

    def run(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name



# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s',
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8'
)

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            # Попробуем передать отрицательное значение в speed
            runner = Runner('Вося', -5)
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)
        else:
            logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        try:
            # Попробуем передать что-то кроме строки в name
            runner = Runner(123, 10)
        except ValueError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)
        else:
            logging.info('"test_run" выполнен успешно')