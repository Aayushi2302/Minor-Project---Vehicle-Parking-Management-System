"""Module responsible for invoking business logic for deleting a customer."""

from business.customer_business import CustomerBusiness
from models.database import db
from utils.responses import SuccessResponse
from utils.custom_error_handler import custom_error_handler


class DeleteCustomerController:
    """
            Class for invoking business logic for deleting customers.
            ...
            Methods
            -------
            delete_customer(): tuple -> method taking customer id and sending it to business layer.
        """

    @custom_error_handler
    def delete_customer(self, customer_id: str) -> tuple:
        """
            Method taking customer id and sending it to business layer to delete.
            Parameters -> customer_id: str
            Returns -> tuple
        """
        customer_business = CustomerBusiness(db)
        customer_business.deactivate_customer(customer_id)
        return SuccessResponse.jsonify_data("Customer deleted successfully."), 200
