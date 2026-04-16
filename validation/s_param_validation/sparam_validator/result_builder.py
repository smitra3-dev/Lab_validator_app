# result builder 
def build_validation_result(param, keys, message, color):
    """
    Standardized result dictionary builder.
    """
    return {
        "param": param,
        "keys": keys,
        "message": message,
        "color": color,
    }
