"""Module responsible for invoking business logic for adding a new customer."""

from src.business.customer_business import CustomerBusiness
from src.models.database import db
from src.utils.custom_error_handler import custom_error_handler
from src.utils.responses import SuccessResponse


class AddCustomerController:
    """
            Class for invoking business logic for registering customers.
            ...
            Methods
            -------
            add_customer(): tuple -> method taking customer data and sending it to business layer.
        """

    @custom_error_handler
    def add_customer(self, customer_data: dict) -> tuple:
        """
            Method taking customer data and sending it to business layer to save.
            Parameters -> customer_data: dict
            Returns -> tuple
        """
        name = customer_data["name"]
        mobile_no = customer_data["mobile_no"]
        vehicle_no = customer_data["vehicle_no"]
        type_name = customer_data["vehicle_type_name"]

        cust_data = (name, mobile_no, vehicle_no)

        customer_business = CustomerBusiness(db)
        customer_business.register_customer(cust_data, type_name)

        return SuccessResponse.jsonify_data("Customer created successfully."), 200
