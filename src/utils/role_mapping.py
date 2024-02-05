import os

RoleMapping = {
    "admin" : os.getenv("ADMIN_ROLE"),
    "attendant" : os.getenv("ATTENDANT_ROLE")
}
