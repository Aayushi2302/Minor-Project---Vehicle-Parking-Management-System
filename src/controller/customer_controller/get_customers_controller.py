"""Module responsible for invoking business logic to get all existing customers."""

from src.business.customer_business import CustomerBusiness
from src.models.database import db
from src.utils.responses import SuccessResponse
from src.utils.custom_error_handler import custom_error_handler


class GetCustomersController:
    """
            Class for invoking business logic for getting all customer details.
            ...
            Methods
            -------
            get_all_customers(): tuple -> method getting customer data from business layer.
        """

    @custom_error_handler
    def get_all_customers(self) -> tuple:
        """
            Method getting customer data for all customers from business layer.
            Parameters -> None
            Returns -> tuple
        """
        customer_business = CustomerBusiness(db)
        response = customer_business.get_all_customers()
        return SuccessResponse.jsonify_data("Customers fetched successfully.", response), 200
