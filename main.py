'''xRPC allows you to customize your Discord rich presence. You can specify your own text,
images, and buttons that will be displayed on your Discord profile whenever the program
is running.'''
import argparse
import json
import logging
import sys
import time

import coloredlogs
import pyfiglet
import pypresence

APP_NAME = 'xRPC'
APP_VERSION = '1.0.0'


def setup_logging():
    '''Sets up the log message formatter.'''
    coloredlogs.install(
        level=logging.INFO,
        fmt='%(asctime)s %(name)s[%(process)d] %(levelname)s %(message)s'
    )


setup_logging()

parser = argparse.ArgumentParser(
    description=f'{APP_NAME} lets you customize your Discord rich presence.')

parser.add_argument(
    'config',
    nargs='?',
    help='The configuration file to use. Defaults to config.json.',
    default='config.json'
)

args = parser.parse_args()

pyfiglet.print_figlet(APP_NAME, font='slant', colors='GREEN')
logging.info('Loading %s...', APP_NAME)

try:
    with open(args.config, encoding='utf-8') as config_file:
        config = json.load(config_file)
        logging.info('Configuration file loaded!')
except FileNotFoundError:
    logging.error('Config file not found! Ensure the file is intact.')
    sys.exit()
except json.JSONDecodeError:
    logging.error(
        'Could not parse config file. Ensure that the file is valid JSON.')
    sys.exit()
except Exception as exception:  # pylint: disable=broad-except
    logging.error('Unknown error occurred while loading config: %s', exception)
    sys.exit()


def get_config_value(key: str) -> any:
    '''Gets the value of a key in the config.json file,
    or None if its value is an empty string.'''
    value = config[key]
    return value if not value == '' else None


try:
    client_id = get_config_value('client_id')
    top_text = get_config_value('top_text')
    bottom_text = get_config_value('bottom_text')
    buttons = get_config_value('buttons')
    large_image = get_config_value('large_image_name')
    small_image = get_config_value('small_image_name')
except KeyError:
    logging.error('Config file is missing required keys!')
    logging.error('Please follow the format of the default config file.')
    sys.exit()

rpc = pypresence.Presence(client_id)
try:
    rpc.connect()
    logging.info('RPC connected!')
except pypresence.DiscordError as err:
    logging.error('Could not connect! Error message:')
    logging.error(err.message)
    sys.exit()

rpc.update(
    details=top_text,
    state=bottom_text,
    buttons=buttons,
    large_image=large_image,
    small_image=small_image
)

while True:
    try:
        time.sleep(15)
    except KeyboardInterrupt:
        logging.info('Bye!')
        sys.exit()
