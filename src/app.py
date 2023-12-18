"""
    Main module for Vehicle-Parking-Management System. 
    This is the entry point of the project.
"""
import logging

from config.app_config import AppConfig
from config.log_prompts.log_prompts import LogPrompts
from config.prompts.prompts import Prompts
from models.database import db
from views.auth_views import AuthViews

# loading the prompts from yaml to py
Prompts.load()
LogPrompts.load()

# initializing logger for recording logs
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s %(funcName)s:%(lineno)d] %(message)s',
    level = logging.DEBUG,
    filename = AppConfig.LOG_FILE_PATH
)
logger = logging.getLogger(__name__)

# for creating tables in database
db.create_all_tables()

if __name__ == "__main__":
    logger.info(LogPrompts.SYSTEM_STARTING_INFO)
    print(Prompts.WELCOME_MESSAGE)

    # for user authentication and granting role based access
    auth_obj = AuthViews()
    auth_obj.login()

    db.connection.close()
    print(Prompts.EXIT_MESSAGE)
    logger.info(LogPrompts.SYSTEM_ENDING_INFO)
else:
    logger.debug(LogPrompts.WRONG_FILE_RUN_DEBUG)
