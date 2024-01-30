import os

RoleMapping = {
    "ADMIN" : os.getenv("ADMIN_ROLE"),
    "ATTENDANT" : os.getenv("EMPLOYEE_ROLE")
}
