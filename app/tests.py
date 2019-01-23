import unittest

from app import hello


class TestCase(unittest.TestCase):

    def setUp(self):
        hello.app.config["TESTING"] = True
        self.app = hello.app.test_client()

    def test_get_hello(self):
        page = self.app.get("/")
        assert page.status_code == 200
        assert 'Hello' in str(page.data)

    def test_get_value(self):
        pass
        # page = self.app.get("/values/key")

if __name__ == '__main__':
    unittest.main()
