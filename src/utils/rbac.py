from functools import wraps

def role_based_access(allowed_roles: tuple):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["usr"] not in allowed_roles:
                abort(403, message="You don't have permission to access this functionality.")
            else:
                return func(*args, **kwargs)
        return inner
    return wrapper