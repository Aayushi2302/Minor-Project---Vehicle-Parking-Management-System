"""
    Main module for Vehicle-Parking-Management System. 
    This is the entry point of the project.
"""
import logging

from config.statements.config import Config
from config.menu.menu_prompts_config import MenuConfig
from config.query.query_config import QueryConfig
from database.query_executor import QueryExecutor
from utils.authentication import Authentication
from logs.logs_config import LogConfig

# loading config files for queries and prompts
Config.load()
QueryConfig.load()
LogConfig.load()
MenuConfig.load()

# initializing logger for recording logs
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    level = logging.DEBUG,
    filename = Config.logs_file_path
)
logger = logging.getLogger('main')

# for creating tables in database
QueryExecutor.create_all_tables()

if __name__ == "__main__":
    logger.info(LogConfig.project_starting_info_prompt)
    print(Config.welcome_message)

    # for user authentication and granting role based access
    authentication_obj = Authentication()
    authentication_obj.login()
else:
    logger.debug(LogConfig.wrong_file_run_debug_prompt)