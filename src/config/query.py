"""Module for storing queries of the project."""

from config.prompts.prompts import Prompts

Prompts.load()

class TableHeader:
    """This class contains all the table headers for displaying tables using tabulate."""
    EMPLOYEE_DETAIL_HEADER = (
        Prompts.EMP_ID_HEADER,
        Prompts.NAME_HEADER,
        Prompts.AGE_HEADER,
        Prompts.GENDER_HEADER,
        Prompts.MOBILE_NO_HEADER,
        Prompts.EMAIL_ADDRESS_HEADER,
        Prompts.USERNAME_HEADER,
        Prompts.ROLE_HEADER,
        Prompts.STATUS_HEADER
    )
    CUSTOMER_DETAIL_HEADER = (
        Prompts.CUSTOMER_ID_HEADER,
        Prompts.NAME_HEADER,
        Prompts.MOBILE_NO_HEADER,
        Prompts.VEHICLE_NO_HEADER,
        Prompts.VEHICLE_TYPE_NAME_HEADER
    )
    PARKING_SLOT_DETAIL_HEADER = (
        Prompts.PARKING_SLOT_NO_HEADER,
        Prompts.VEHICLE_TYPE_HEADER,
        Prompts.STATUS_HEADER
    )
    SLOT_BOOKING_DETAIL_HEADER = (
        Prompts.CUSTOMER_ID_HEADER,
        Prompts.NAME_HEADER,
        Prompts.MOBILE_NO_HEADER,
        Prompts.VEHICLE_NO_HEADER,
        Prompts.VEHICLE_TYPE_HEADER,
        Prompts.BOOKING_ID_HEADER,
        Prompts.PARKING_SLOT_NO_HEADER,
        Prompts.IN_DATE_HEADER,
        Prompts.IN_TIME_HEADER,
        Prompts.OUT_DATE_HEADER,
        Prompts.OUT_TIME_HEADER,
        Prompts.HOURS_HEADER,
        Prompts.CHARGES_HEADER
    )
    VEHICLE_TYPE_DETAIL_HEADER = (
        Prompts.VEHICLE_TYPE_ID,
        Prompts.VEHICLE_TYPE_NAME_HEADER,
        Prompts.PRICE_PER_HOUR
    )
    VEHICLE_TYPE_HEADER = (Prompts.VEHICLE_TYPE_NAME_HEADER, )

class QueryConfig:
    """This class contains all the queries of the project.""" 

    # queries for authentication table
    AUTHENTICATION_TABLE_CREATION = """
        CREATE TABLE IF NOT EXISTS authentication(
            emp_id TEXT PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT,
            password_type TEXT DEFAULT "default"
        )
    """
    CREATE_EMPLOYEE_CREDENTIALS = """
        INSERT INTO authentication(
            emp_id,
            username,
            password,
            role
        ) VALUES(?, ?, ?, ?)
    """
    FETCH_EMPLOYEE_CREDENTIALS = """
        SELECT password, role, password_type
        FROM authentication INNER JOIN employee
        ON authentication.emp_id = employee.emp_id
        WHERE authentication.username = ? and employee.status = ?
    """
    FETCH_AUTHENTICATION_TABLE = "SELECT * FROM authentication"
    FETCH_DEFAULT_PASSWORD_FROM_EMPID = """
        SELECT password_type, password FROM authentication
        WHERE emp_id = ?
    """
    FETCH_EMPID_FROM_USERNAME = """
        SELECT emp_id FROM authentication
        WHERE username = ?
    """
    FETCH_EMPID_FROM_ROLE_AND_STATUS = """
        SELECT authentication.emp_id FROM authentication
        INNER JOIN employee ON
        authentication.emp_id = employee.emp_id
        WHERE authentication.role = ? and employee.status = ?
    """
    UPDATE_DEFAULT_PASSWORD = """
        UPDATE authentication SET password = ?, 
        password_type = ? WHERE username = ?
    """
    UPDATE_EMPLOYEE_CREDENTIAL_FROM_EMP_ID = """
        UPDATE authentication SET 
        {} = ? WHERE emp_id = ?
    """

    # queries for employee table
    EMPLOYEE_TABLE_CREATION = """
        CREATE TABLE IF NOT EXISTS employee(
            emp_id TEXT PRIMARY KEY,
            name TEXT,
            age INTEGER,
            gender TEXT,
            mobile_no TEXT UNIQUE,
            email_address TEXT UNIQUE,
            status TEXT DEFAULT "active",
            FOREIGN KEY(emp_id) REFERENCES authentication(emp_id) ON DELETE CASCADE
        )
    """
    CREATE_EMPLOYEE_DETAILS = """
        INSERT INTO employee(
            emp_id,
            name,
            age,
            gender,
            mobile_no,
            email_address
        ) VALUES(?, ?, ?, ?, ?, ?)
    """
    FETCH_EMP_ID_FROM_EMAIL = """
        SELECT emp_id FROM employee
        WHERE email_address = ?
    """
    FETCH_EMP_ID_STATUS_AND_ROLE_FROM_EMAIL = """
        SELECT employee.emp_id, status, role FROM employee
        INNER JOIN authentication ON
        employee.emp_id = authentication.emp_id
        WHERE employee.email_address = ?
    """
    UPDATE_EMPLOYEE_DETAIL_FROM_EMP_ID = """
        UPDATE employee SET 
        {} = ? WHERE emp_id = ?
    """
    VIEW_EMPLOYEE_DETAIL = """
        SELECT employee.emp_id, name, age, gender, mobile_no, email_address, username, role, status
        FROM employee INNER JOIN authentication ON
        employee.emp_id = authentication.emp_id
        WHERE authentication.role <> "admin"
    """
    VIEW_SINGLE_EMPLOYEE_DETAIL = """
        SELECT employee.emp_id, name, age, gender, mobile_no, email_address, username, role, status
        FROM employee INNER JOIN authentication ON
        employee.emp_id = authentication.emp_id
        WHERE authentication.username = ?
        ORDER BY employee.name ASC
    """

    # queries for vehicle_type table
    VEHICLE_TYPE_TABLE_CREATION = """
        CREATE TABLE IF NOT EXISTS vehicle_type(
            type_id TEXT PRIMARY KEY,
            type_name TEXT UNIQUE,
            price_per_hour REAL
        )
    """
    CREATE_VEHICLE_TYPE ="""
        INSERT INTO vehicle_type(
            type_id,
            type_name,
            price_per_hour
        ) VALUES(?, ?, ?)
    """
    FETCH_VEHICLE_TYPE = "SELECT * FROM vehicle_type ORDER BY type_name ASC"
    FETCH_PRICE_PER_HOUR_FROM_TYPE_ID = """
        SELECT price_per_hour FROM vehicle_type
        WHERE type_id = ?
    """
    FETCH_VEHICLE_TYPE_ID_FROM_TYPE_NAME = """
        SELECT type_id FROM vehicle_type
        WHERE type_name = ?
    """
    UPDATE_VEHICLE_TYPE_DETAIL_FROM_TYPE_ID = """
        UPDATE vehicle_type SET
        {} = ? WHERE type_id = ?
    """

    # queries for parking_slot table
    PARKING_SLOT_TABLE_CREATION = """
        CREATE TABLE IF NOT EXISTS parking_slot(
            parking_slot_no TEXT PRIMARY KEY,
            type_id TEXT,
            status TEXT DEFAULT "vacant",
            FOREIGN KEY(type_id) REFERENCES vehicle_type(type_id) ON DELETE CASCADE
        )
    """
    CREATE_PARKING_SLOT = """
        INSERT INTO parking_slot(
            parking_slot_no,
            type_id
        ) VALUES(?, ?)
    """
    FETCH_PARKING_SLOT_DETAIL_FROM_PARKING_SLOT_NO = """
        SELECT * FROM parking_slot
        WHERE parking_slot_no = ?
    """
    FETCH_STATUS_FROM_PARKING_SLOT_NUMBER = """
        SELECT status FROM parking_slot
        WHERE parking_slot_no = ?
    """
    FETCH_PARKING_SLOT_NO_FOR_BOOKING = """
        SELECT parking_slot_no FROM parking_slot
        WHERE type_id = ? and status = ?
    """
    UPDATE_PARKING_SLOT_DETAIL_FROM_PARKING_SLOT_NO = """
        UPDATE parking_slot SET 
        {} = ? WHERE parking_slot_no = ?
    """
    VIEW_PARKING_SLOT_DETAIL = """
        SELECT parking_slot_no, type_name, status
        FROM parking_slot INNER JOIN vehicle_type ON
        parking_slot.type_id = vehicle_type.type_id
        ORDER BY parking_slot.parking_slot_no ASC
    """
    DELETE_PARKING_SLOT_FROM_PARKING_SLOT_NO = """
        DELETE FROM parking_slot
        WHERE parking_slot_no = ?
    """
    # queries for customer table
    CUSTOMER_TABLE_CREATION = """
        CREATE TABLE IF NOT EXISTS customer(
            customer_id TEXT PRIMARY KEY,
            name TEXT,
            mobile_no TEXT UNIQUE,
            vehicle_no TEXT UNIQUE,
            type_id TEXT,
            FOREIGN KEY(type_id) REFERENCES vehicle_type(type_id) ON DELETE CASCADE
        )
    """
    CREATE_CUSTOMER = """
        INSERT INTO customer(
            customer_id,
            name,
            mobile_no,
            vehicle_no,
            type_id
        ) VALUES (?, ?, ?, ?, ?)
    """
    FETCH_CUSTOMER_ID_AND_TYPE_ID_FROM_VEHICLE_NO = """
        SELECT customer_id, type_id FROM customer
        WHERE vehicle_no = ?
    """
    UPDATE_CUSTOMER_DETAIL = """
        UPDATE customer SET
        {} = ? WHERE customer_id = ?
    """
    VIEW_CUSTOMER_DETAIL = """
        SELECT customer_id, name, mobile_no, vehicle_no, type_name
        FROM customer INNER JOIN vehicle_type ON
        customer.type_id = vehicle_type.type_id
        ORDER BY customer.name ASC
    """

    # queries for slot_booking table
    SLOT_BOOKING_TABLE_CREATION = """
        CREATE TABLE IF NOT EXISTS slot_booking(
            booking_id TEXT PRIMARY KEY,
            customer_id TEXT,
            parking_slot_no TEXT,
            in_date TEXT,
            in_time TEXT,
            out_date TEXT,
            out_time TEXT DEFAULT "XX:XX",
            hours REAL DEFAULT 0.0,
            charges REAL DEFAULT 0.0,
            FOREIGN KEY(customer_id) REFERENCES customer(customer_id) ON DELETE CASCADE,
            FOREIGN KEY(parking_slot_no) REFERENCES parking_slot(parking_slot_no) ON DELETE CASCADE
        )
    """
    CREATE_SLOT_BOOKING = """
        INSERT INTO slot_booking(
            booking_id,
            customer_id,
            parking_slot_no,
            in_date,
            in_time,
            out_date
        ) VALUES(?, ?, ?, ?, ?, ?)
    """
    FETCH_BOOKING_DETAIL_FROM_CUSTOMER_ID = """
        SELECT booking_id, out_time FROM slot_booking 
        WHERE customer_id = ?
    """
    FETCH_BOOKING_DETAIL_FROM_BOOKING_ID = """
        SELECT * FROM slot_booking 
        WHERE booking_id = ?
    """
    FETCH_DETAIL_FOR_VACATING_PARKING_SLOT = """
        SELECT booking_id, parking_slot_no, in_date, in_time, out_time FROM slot_booking INNER JOIN customer
        ON slot_booking.customer_id = customer.customer_id 
        WHERE customer.vehicle_no = ?
    """
    FETCH_TYPE_ID_FROM_BOOKING_ID = """
        SELECT type_id
        FROM slot_booking INNER JOIN customer
        ON slot_booking.customer_id = customer.customer_id
        WHERE slot_booking.booking_id = ?
    """
    FETCH_CURRENT_DATE_RECORD = """
        SELECT customer.customer_id, name, mobile_no, vehicle_no, type_name, 
        booking_id, parking_slot_no, in_date, in_time, out_date, out_time, hours, charges 
        FROM customer INNER JOIN vehicle_type
        ON customer.type_id=vehicle_type.type_id
        INNER JOIN slot_booking ON
        customer.customer_id=slot_booking.customer_id
        WHERE in_date = ?
    """
    FETCH_CURRENT_YEAR_RECORD = """
        SELECT customer.customer_id, name, mobile_no, vehicle_no, type_name, 
        booking_id, parking_slot_no, in_date, in_time, out_date, out_time, hours, charges 
        FROM customer INNER JOIN vehicle_type
        ON customer.type_id=vehicle_type.type_id
        INNER JOIN slot_booking ON
        customer.customer_id=slot_booking.customer_id
        WHERE in_date LIKE ?
    """
    FETCH_OUT_TIME_FROM_CUSTOMER_ID = """
        SELECT out_time FROM slot_booking
        WHERE customer_id = ?
    """
    UPDATE_SLOT_BOOKING_DETAIL = """
        UPDATE slot_booking SET
        {} = ? WHERE booking_id = ?
    """
    UPDATE_DETAIL_FOR_VACATIG_PARKING_SLOT = """
        UPDATE slot_booking SET
        out_date = ?, out_time = ?, hours = ?, charges = ?
        WHERE booking_id = ?
    """
    VIEW_SLOT_BOOKING_DETAIL = """
        SELECT customer.customer_id, name, mobile_no, vehicle_no, type_name, 
        booking_id, parking_slot_no, in_date, in_time, out_date, out_time, hours, charges 
        FROM customer INNER JOIN vehicle_type
        ON customer.type_id=vehicle_type.type_id
        INNER JOIN slot_booking ON
        customer.customer_id=slot_booking.customer_id
    """
