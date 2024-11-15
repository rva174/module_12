import unittest
from tests_12_3 import RunnerTest, TournamentTest

# Создание тестового набора
test_suite = unittest.TestSuite()
# test_suite.addTests(unittest.makeSuite(RunnerTest))
# test_suite.addTests(unittest.makeSuite(TournamentTest))
test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))
# Запуск тестов
runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_suite)