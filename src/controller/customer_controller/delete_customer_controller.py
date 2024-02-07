"""Module responsible for invoking business logic for deleting a customer."""

from src.business.customer_business import CustomerBusiness
from src.models.database import db
from src.utils.responses import SuccessResponse
from src.utils.custom_error_handler import custom_error_handler

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
            Parameter -> customer_id: str
            Return type -> tuple
        """
        customer_business_obj = CustomerBusiness(db)
        customer_business_obj.deactivate_customer(customer_id)
        return SuccessResponse.jsonify_data("Customer deleted successfully."), 200
