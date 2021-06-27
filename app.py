import sched
import time
from pathlib import Path
from dotenv import load_dotenv
from src.newsletter import Newsletter


def main():
    load_env_variables()
    define_scheduler_retry()


def load_env_variables():
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)


def define_scheduler_retry():
    newsletter = Newsletter()
    scheduler_retry = sched.scheduler(time.time, time.sleep)
    scheduler_retry.enter(0, 1, newsletter.prepare_news, (scheduler_retry,))
    scheduler_retry.run()


if __name__ == '__main__':
    main()
