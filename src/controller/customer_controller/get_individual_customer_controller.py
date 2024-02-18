"""Module responsible for invoking business logic to get details of individual customer."""

from business.customer_business import CustomerBusiness
from models.database import db
from utils.responses import SuccessResponse
from utils.custom_error_handler import custom_error_handler


class GetIndividualCustomerController:
    """
        Class for invoking business logic for getting details of individual customer.
        ...
        Methods
        -------
        get_individual_customer(): tuple -> method for  getting details of individual customer.
    """

    @custom_error_handler
    def get_individual_customer(self, customer_id: str) -> tuple:
        """
            Method for  getting details of individual customer.
            Parameters -> customer_id: str
            Returns -> tuple
        """
        customer_business = CustomerBusiness(db)
        data = customer_business.get_individual_customer_details(customer_id)
        return SuccessResponse.jsonify_data("Customer data fetched successfully.", data), 200
