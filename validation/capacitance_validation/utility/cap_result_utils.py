#cap_result_utils.py

def build_cap_result(param, keys, status, comment, color, noise="NA"):
    return {
        "param": param,
        "keys": keys,
        "status": status,
        "noise": noise,
        "comment": comment,
        "color": color,
    }


def append_cap_result(results, param, keys, status, comment, color, noise="NA"):
    results.append(
        build_cap_result(
            param=param,
            keys=keys,
            status=status,
            comment=comment,
            color=color,
            noise=noise,
        )
    )
