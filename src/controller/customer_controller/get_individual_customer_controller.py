"""Module responsible for invoking business logic to get details of individual customer."""

from src.business.customer_business import CustomerBusiness
from src.models.database import db
from src.utils.responses import SuccessResponse
from src.utils.custom_error_handler import custom_error_handler


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
            Parameter -> customer_id: str
            Return type -> tuple
        """
        customer_business_obj = CustomerBusiness(db)
        customer_business_obj.get_individual_customer(customer_id)
        return SuccessResponse.jsonify_data("Customer data fetched successfully."), 200
