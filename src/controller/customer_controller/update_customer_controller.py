"""Module responsible for invoking business logic for updating customer."""

from src.business.customer_business import CustomerBusiness
from src.models.database import db
from src.utils.responses import SuccessResponse
from src.utils.custom_error_handler import custom_error_handler

class UpdateCustomerController:
    """
        Class for invoking business logic for updating customer details.
        ...
        Methods
        -------
        update_customer(): tuple -> method for updating customer data for a particular customer.
    """

    @custom_error_handler
    def update_customer(self, customer_id: str, customer_data: dict) -> tuple:
        """
            Method for updating customer data for a particular customer.
            Parameters -> customer_id: str, customer_data: dict
            Returns -> tuple
        """
        name = customer_data["name"]
        mobile_no = customer_data["mobile_no"]
        vehicle_no = customer_data["vehicle_no"]

        cust_data = (name, mobile_no, vehicle_no)

        customer_business = CustomerBusiness(db)
        customer_business.update_customer_details(customer_id, cust_data)
        return SuccessResponse.jsonify_data("Customer updated successfully."), 200
