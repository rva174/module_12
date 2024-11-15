import unittest


def skip_if_frozen(test_method):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        return test_method(self, *args, **kwargs)
    return wrapper


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_some_functionality(self):
        # Пример теста для класс Runner
        self.assertEqual(self.part_1.name, 'Усейн')

    @skip_if_frozen
    def test_walk(self):
        self.part_1.walk()
        self.assertEqual(self.part_1.distance, 10)

    def setUp(self):
        self.part_1 = Runner('Усейн', 10)
        self.part_2 = Runner('Андрей', 9)


class TournamentTest(unittest.TestCase):
    is_frozen = True  # Измените его на False, чтобы активировать тесты

    @skip_if_frozen
    def test_run_1(self):
        self.tournament_1 = Tournament(90, self.part_1, self.part_3)
        self.all_results = self.tournament_1.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')

    def setUp(self):
        self.part_1 = Runner('Усейн', 10)
        self.part_2 = Runner('Андрей', 9)
        self.part_3 = Runner('Ник', 3)


if __name__ == '__main__':
    unittest.main()