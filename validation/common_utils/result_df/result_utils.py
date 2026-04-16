def add_result(results, param, keys, message, color, section=None, detail=None):
    item = {
        "param": param,
        "keys": keys,
        "message": message,
        "color": color,
    }

    if section is not None:
        item["section"] = section
    if detail is not None:
        item["detail"] = detail

    results.append(item)
