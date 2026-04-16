#validator_flags
def resolve_validation_flags(selected_param):
    """
    Decide whether gm checks, gds checks, or both should run.
    """
    param = str(selected_param).lower()

    run_gm = param == "gm"
    run_gds = param == "gds"

    if not run_gm and not run_gds:
        run_gm = True
        run_gds = True

    return run_gm, run_gds
