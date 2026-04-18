##filters/filter_utils.py
def to_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return [v for v in value if v is not None and v != ""]
    return [value]


def make_options(values):
    return [{"label": str(v), "value": v} for v in values]


def keep_valid(selected, valid_values):
    selected_list = to_list(selected)
    valid_set = set(valid_values)
    return [v for v in selected_list if v in valid_set]
