#validator_config
from validation.Gm_Gds_validation.config_rule_utils.gm_gds_config import GM_GDS_CONFIG


def build_gm_gds_config(config=None):
    """
    Build runtime config for gm/gds validation.
    """
    cfg = dict(GM_GDS_CONFIG)

    if config:
        cfg.update(config)

    return cfg
