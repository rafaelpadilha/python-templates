import click
import time

from myapp import __version__ as app_version
from myapp.settings import logger

@click.command()
@click.option('-h', '--help',   is_flag=True, help='Help.')
def start(help):
    """ Starts the app.
    """

    if(help):
        print("Help commands.")
        exit(0)

    start_time = time.time()
    logger.info("MyApp initialization...")
    logger.info(f"Version: {app_version}")

    # App Development

    print("Hello world!")

    end_time = time.time()
    logger.info(f'Execution time: {end_time - start_time} seconds')

if __name__ == "__main__":
    start()
