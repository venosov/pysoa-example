from pysoa.test.server import ServerTestCase

from server import ExampleServer


class TestSquareAction(ServerTestCase):
    server_class = ExampleServer
    server_settings = {}

    def test(self):
        result = self.call_action('square', {'number': 2})
        assert 4 == result.body['square']
