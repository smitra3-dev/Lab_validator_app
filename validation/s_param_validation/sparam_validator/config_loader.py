#config loader 
from .sparam_config import SPARAM_CONFIG


def load_sparam_config(config=None):
    """
    Load default S-parameter config and apply user overrides.
    """
    cfg = dict(SPARAM_CONFIG)
    if config:
        cfg.update(config)
    return cfg
