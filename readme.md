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
|   .gitignore
|   Pipfile
|   Pipfile.lock
|   readme.md
|   vehicle_parking_management_requirements.pdf
|
+---diagrams
|       class_diagram.png
|       db_schema.png
|       flow_diagram.jpg
|       use_case_diagram.png
|
\---src
    |   app.py
    |
    +---config
    |       menu.py
    |       prompts.py
    |       query.py
    |
    +---controller
    |   |   admin_controller.py
    |   |   employee_controller.py
    |   |
    |   \---handler
    |           admin_handler.py
    |           customer_update_handler.py
    |           employee_handler.py
    |           employee_update_handler.py
    |
    +---database
    |       db_connector.py
    |       parking_management.db
    |       query_executor.py
    |
    +---logs
    |       logs.txt
    |       log_config.py
    |
    +---parking_manager
    |       parking_charges.py
    |       parking_slots.py
    |       parking_status.py
    |       slot_booking.py
    |       vehicle_type.py
    |
    \---utils
        |   authentication.py
        |   common.py
        |   regex_pattern.py
        |
        \---validator
                parking_manager_input_validation.py
                user_input_validation.py
```

## UML Diagrams
- [Class Diagram](diagrams/class_diagram.png)
- [Database Schema](diagrams/db_schema.png)
- [Flow Diagram](diagrams/flow_diagram.jpg)
- [Use Case Diagram](diagrams/use_case_diagram.png)