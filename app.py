import os
from pathlib import Path
from dotenv import load_dotenv
from src.newsletter import Newsletter


def main():
    load_env_variables()
    newsletter = Newsletter(os.environ['EMAIL'], os.environ['PASSWORD'],
                            os.environ['SLACK_TOKEN'], os.environ['SLACK_CHANNEL'])
    newsletter.prepare_news()


def load_env_variables():
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)


if __name__ == '__main__':
    main()
