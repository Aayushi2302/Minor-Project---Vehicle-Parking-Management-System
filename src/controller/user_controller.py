import logging

from config.prompts.prompts import Prompts
from config.query import QueryConfig
from models.database import db
from utils.common_helper import CommonHelper

logger = logging.getLogger(__name__)

class UserController:

     def view_user_details(self, username: str):
        """
            Method to display a particular user details.
            Parameter -> self, username
            Return type -> None
        """
        logger.info("Viewing individual employee details.")
        print(Prompts.DETAILS_FOR_GIVEN_EMPLOYEE.format(username))
        emp_data =  db.fetch_data_from_database(
                        QueryConfig.VIEW_SINGLE_EMPLOYEE_DETAIL,
                        (username, )
                    )

        keys = ["employee_id", "name", "age", "gender", "mobile_no", "email", "username", "role", "status"]
        json_response = CommonHelper.jsonify_data(emp_data, keys)
        print(json_response)
        return json_response
