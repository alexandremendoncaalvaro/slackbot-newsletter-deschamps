import unittest
from pathlib import Path
from dotenv import load_dotenv
from src.newsletter import Newsletter


class TestNewsletter(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        env_path = Path('.') / '.env'
        load_dotenv(dotenv_path=env_path)
        self.newsletter = Newsletter()

    def test_check_email(self):
        server, data = self.newsletter.check_email()
        self.assertIsNotNone(server)
        self.assertGreater(len(data), 0)

    def test_config_slack_client(self):
        client, channel = self.newsletter.config_slack_client()
        self.assertIsNotNone(client)
        self.assertRegex(channel, '(#+[a-zA-Z0-9(_)]{1,})')


if __name__ == '__name__':
    unittest.main()
