#cap_selection.py

def resolve_selected_capacitances(params, supported_caps):
    if params is None:
        return list(supported_caps)

    if isinstance(params, str):
        params = [params]

    return [p for p in supported_caps if p in params]
