"""
    Module containing common methods which are shared across the project.
"""
from datetime import datetime
import hashlib
import logging
import re
import pytz
import maskpass
from tabulate import tabulate

from config.statements.config import Config
from config.query.query_config import QueryConfig
from database.query_executor import QueryExecutor
from utils.validator.user_input_validation import UserInputValidation
from logs.logs_config import LogConfig

logger = logging.getLogger('common')

PASSWORD_PATTERN = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[@#$%&]).{8,}$"

class Common:
    """
        Class containig helper methods to be shared throughout the project.
    """
    def is_admin_registered(self) -> bool:
        """
            Method for checking whether admin is registered in the database who is the first user of the system.
        """
        user_data = QueryExecutor.fetch_data_from_database(
                        QueryConfig.query_for_fetching_emp_id_from_role_and_status,
                        ("admin", "active")
                    )
        if not any(user_data):
            return True
        else:
            return False  
    
    def create_new_password(self, username: str) -> str:
        """
            Method for creating new password for the user following strong password recommendation.
        """
        while True:
            print(Config.change_password_prompt + "\n")
            print(Config.strong_password_requirements_prompt + "\n")
            input_password = maskpass.askpass(
                                prompt = Config.new_password_prompt, 
                                mask="*"
                            )
            is_strong_password = re.match(PASSWORD_PATTERN, input_password)
            if not is_strong_password:
                print(Config.weak_password_input_prompt + "\n")
            else:
                new_password = input_password
                confirm_password = ""
                while True:
                    confirm_password =  maskpass.askpass(
                        prompt = Config.confirm_password_prompt,
                        mask="*"
                    )
                    if new_password != confirm_password:
                        print(Config.password_not_match_prompt + "\n")
                    else:
                        break
                hashed_password = hashlib.sha256(confirm_password.encode('utf-8')).hexdigest()
                QueryExecutor.save_data_in_database(
                    QueryConfig.query_for_updating_default_password,
                    (hashed_password, "permanent", username),
                    Config.password_change_successful_prompt + "\n"
                )
                return

    def view_emp_details(self) -> None:
        """
            Method to display a particular user details.
        """
        emp_email = UserInputValidation.input_email_address()
        data =  QueryExecutor.fetch_data_from_database(
                    QueryConfig.query_for_fetching_emp_id_and_status_from_email,
                    (emp_email, )
                )
        if not any(data):
            print(Config.details_does_not_exist_prompt.format(emp_email))
        else:
            emp_id = data[0][0]
            print(Config.details_for_given_employee_prompt.format(emp_id))
            data =  QueryExecutor.fetch_data_from_database(
                        QueryConfig.query_for_viewing_single_employee_detail,
                        (emp_id, )
                    )
            headers = QueryConfig.employee_detail_header
            self.display_table(data, headers)

    def display_table(self, data: list, headers: list) -> None:
        """
            Method to display data in tabular format using tabulate.
        """
        row_id = [i for i in range(1, len(data) + 1)]
        print(
                tabulate(
                    data,
                    headers,
                    showindex = row_id,
                    tablefmt = "simple_grid"
                )
            )
    
    def get_current_date_and_time(self):
        """
            For recording current date and time.
        """
        time_zone = pytz.timezone('Asia/Kolkata')
        current = datetime.now(time_zone)
        curr_time = current.strftime('%H:%M')
        curr_date = current.strftime('%d-%m-%Y')
        return (curr_date, curr_time)