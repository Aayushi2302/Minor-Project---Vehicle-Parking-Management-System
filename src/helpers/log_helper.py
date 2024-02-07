from flask import g
import logging

def get_request_id():
    return g.request_id