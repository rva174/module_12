import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):
    def test_run(self):
        r1 = Runner('run')
        for i in range(10):
            r1.run()
        self.assertEqual(r1.distance, 100)

    def test_walk(self):
        r2 = Runner('walk')
        for i in range(10):
            r2.walk()
        self.assertEqual(r2.distance, 50)

    def test_challenge(self):
        r1 = Runner('run')
        r2 = Runner('walk')
        for i in range(10):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance, r2.distance)


if __name__ == '__main__':
    unittest.main()