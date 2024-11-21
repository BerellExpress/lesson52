import code_for_log
import unittest
import logging


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены.")
    def test_walk(self):
        runner = code_for_log.Runner("Walker")
        for i in range(10):
            try:
                runner.walk()
                self.assertEqual(runner.distance, 50)
                logging.info('"test_walk" выполнен успешно', exc_info=True)
            except:
                logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены.")
    def test_run(self):
        runner = code_for_log.Runner("Rooney")
        for i in range(10):
            try:
                runner.run()
                self.assertEqual(runner.distance, 100)
                logging.info('"test_run" выполнен успешно', exc_info=True)
            except:
                logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены.")
    def test_challenge(self):
        runner1 = code_for_log.Runner("Alice")
        runner2 = code_for_log.Runner("Totoshka")
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    code_for_log
logging.basicConfig(filemode='w', level=logging.INFO, filename='runner_tests.log',
                    format='%(asctime)s | %(levelname)s | %(message)s')