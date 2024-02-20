"""Module having end points related to customer."""

from flask.views import MethodView
from flask_smorest import Blueprint

from src.config.app_config import AppConfig
from src.controller.customer_controller.add_customer_controller import AddCustomerController
from src.controller.customer_controller.get_customers_controller import GetCustomersController
from src.controller.customer_controller.get_individual_customer_controller import GetIndividualCustomerController
from src.controller.customer_controller.update_customer_controller import UpdateCustomerController
from src.controller.customer_controller.delete_customer_controller import DeleteCustomerController
from src.schemas.customer_schema import CustomerSchema, CustomerResponseSchema, CustomerUpdateSchema
from src.utils.route_access import route_access
from src.utils.role_mapping import RoleMapping

blp = Blueprint("customer", __name__ , description="Customer related operations.")


@blp.route("/v1/customers")
class EmployeeOperations(MethodView):
    """
        Class containing various methods applicable to /v1/customers route.
        ...
        Methods
        -------
        POST
        GET
    """
    @blp.doc(parameters = [AppConfig.BLP_DOC_PARAMETERS])
    @blp.arguments(CustomerSchema)
    @blp.response(201, CustomerResponseSchema)
    @route_access((RoleMapping["attendant"], ))
    def post(self, customer_data: dict) -> dict:
        """
            Method for performing post operation customers.
            ...
            On Success -> Follows CustomerResponseSchema and returns success message.
            On Failure -> Returns success = False and error message.
        """
        return AddCustomerController().add_customer(customer_data)

    @blp.doc(parameters = [AppConfig.BLP_DOC_PARAMETERS])
    @blp.response(200, CustomerSchema(many=True))
    @route_access((RoleMapping["attendant"], ))
    def get(self) -> dict:
        """
            Method for performing get operation on customers.
            ...
            On Success -> Follows CustomerSchema and customer related details.
            On Failure -> Returns success = False and error message.
        """
        return GetCustomersController().get_all_customers()


@blp.route("/v1/customers/<string:customer_id>")
class EmployeeIndividualOperations(MethodView):
    """
        Class containing various methods applicable to /v1/customer/{customer_id} route.
        ...
        Methods
        -------
        PUT
        GET
        DELETE
    """
    @blp.doc(parameters=[AppConfig.BLP_DOC_PARAMETERS])
    @blp.arguments(CustomerUpdateSchema)
    @blp.response(200, CustomerResponseSchema)
    @route_access((RoleMapping["attendant"], ))
    def put(self, customer_data: dict, customer_id: str) -> dict:
        """
            Method for performing update operation on a particular customer.
            ...
            On Success -> Follows CustomerResponseSchema and returns success message.
            On Failure -> Returns success = False and error message.
        """
        return UpdateCustomerController().update_customer(customer_id, customer_data)

    @blp.doc(parameters = [AppConfig.BLP_DOC_PARAMETERS])
    @blp.response(200, CustomerSchema)
    @route_access((RoleMapping["attendant"], ))
    def get(self, customer_id: str) -> dict:
        """
            Method for fetching details of a particular customer.
            ...
            On Success -> Follows CustomerSchema and returns a particular customer detail.
            On Failure -> Returns success = False and error message.
        """
        return GetIndividualCustomerController().get_individual_customer(customer_id)

    @blp.doc(parameters = [AppConfig.BLP_DOC_PARAMETERS])
    @blp.response(200, CustomerResponseSchema)
    @route_access((RoleMapping["attendant"], ))
    def delete(self, customer_id: str) -> dict:
        """
            Method for performing delete operation on a particular customer.
            ...
            On Success -> Follows CustomerResponseSchema and returns success message.
            On Failure -> Returns success = False and error message.
        """
        return DeleteCustomerController().delete_customer(customer_id)
