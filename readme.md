# Vehicle Parking Management System
A console based python application designed to efficiently monitor and manage vehicle parking in a parking lot.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Folder Structure](#folder-structure)
- [UML Diagrams](#uml-diagrams)

## Introduction
This is a python console application built as a minor project for my undergoing internship at _**Watchguard Technologies, Noida.**_
This project contains functionalities to simplify the booking process of vehicle parking and helps in effective management of customer data. Customers can book a parking slot based on their vehicle type by getting the help of an attendant. Staff or attendant acts as an intermediator between customer and the management system.

## Features
This project offers below mentioned functionalities and features:

- User authentication and role-based access as admin or attendant.
- Interactive interface.
- Maintaining confidentiality of user credentials through hashing.
- Logging and monitoring.
- Input validations using Regex.
- Exception Handling.
- Clean code with proper folder structure.
- Classes following single responsibility principles.
- Maintained different files for prompts and input statements showing uniformity.

## Getting Started
To run the project in your system, you have to perfrom following steps:

```bash
# Clone the repository using following git command
git clone https://github.com/Aayushi2302/Minor-Project---Vehicle-Parking-Management-System

# Install project dependencies using
python -m pipenv install

# To run the project, use the following command
pipenv run python .\src\app.py
```

## Folder Structure
```bash
|   .coverage
│   .gitignore
│   logs.log
│   Pipfile
│   Pipfile.lock
│   pytest.ini
│   readme.md
│   vehicle_parking_management_requirements.pdf
│
├───.vscode
│      
├───diagrams
│       
├───htmlcov
│       
├───src
│   │   app.py
│   │   __init__.py
│   │
│   ├───config
│   │   │   app_config.py
│   │   │   query.py
│   │   │   regex_pattern.py
│   │   │   __init__.py
│   │   │
│   │   ├───log_prompts
│   │   │       log_prompts.py
│   │   │       log_prompts.yaml
│   │   │       __init__.py
│   │   │
│   │   └───prompts
│   │           prompts.py
│   │           prompts.yaml
│   │           __init__.py
│   │
│   ├───controller
│   │   │   admin_controller.py
│   │   │   auth_controller.py
│   │   │   employee_controller.py
│   │   │   __init__.py
│   │   │
│   │   └───parking_controller
│   │           parking_slot.py
│   │           parking_status.py
│   │           slot_booking.py
│   │           vehicle_type.py
│   │           __init__.py
│   │
│   ├───models
│   │       database.py
│   │       parking_management.db
│   │       __init__.py
│   │
│   ├───utils
│   │   │   common_helper.py
│   │   │   decorators.py
│   │   │   __init__.py
│   │   │
│   │   └───input_validator
│   │           parking_controller_validator.py
│   │           user_controller_validator.py
│   │           __init__.py
│   │
│   └───views
│       │   admin_views.py
│       │   auth_views.py
│       │   employee_views.py
│       │   __init__.py
│       │
│       └───parking_views
│               parking_slot_views.py
│               parking_status_views.py
│               slot_booking_views.py
│               vehicle_type_views.py
│               __init__.py
│
└───tests
    │   __init__.py
    │
    ├───test_controller
    │   │   test_admin_controller.py
    │   │   test_auth_controller.py
    │   │   test_employee_controller.py
    │   │   __init__.py
    │   │
    │   └───test_parking_controller
    │           test_parking_slots.py
    │           test_parking_status.py
    │           test_slot_booking.py
    │           test_vehicle_type.py
    │           __init__.py
    │
    ├───test_utils
    │   │   test_common_helper.py
    │   │   test_error_handler.py
    │   │   __init__.py
    │   │
    │   └───test_input_validator
    │           test_parking_controller_validator.py
    │           test_user_controller_validator.py
    │           __init__.py
    │
    └───test_views
        │   test_admin_views.py
        │   test_auth_views.py
        │   test_employee_views.py
        │   __init__.py
        │
        └───test_parking_views
                test_parking_slot_views.py
                test_parking_status_views.py
                test_slot_booking_views.py
                test_vehicle_type_views.py
                __init__.py
```

## UML Diagrams
- [Class Diagram](diagrams/class_diagram.png)
- [Database Schema](diagrams/db_schema.png)
- [Flow Diagram](diagrams/flow_diagram.jpg)
- [Use Case Diagram](diagrams/use_case_diagram.png)