from validation.Gm_Gds_validation.config_rule_utils.column_config import GM_GDS_COLUMN_CONFIG
from validation.Gm_Gds_validation.config_rule_utils.numeric_config import GM_GDS_NUMERIC_CONFIG
from validation.Gm_Gds_validation.config_rule_utils.vth_config import GM_GDS_VTH_CONFIG
from validation.Gm_Gds_validation.config_rule_utils.frequency_split_config import GM_GDS_FREQUENCY_SPLIT_CONFIG
from validation.Gm_Gds_validation.config_rule_utils.gm_gds_rule_config import GM_GDS_RULE_CONFIG


GM_GDS_CONFIG = {
    **GM_GDS_COLUMN_CONFIG,
    **GM_GDS_NUMERIC_CONFIG,
    **GM_GDS_VTH_CONFIG,
    **GM_GDS_FREQUENCY_SPLIT_CONFIG,
    **GM_GDS_RULE_CONFIG,
}
