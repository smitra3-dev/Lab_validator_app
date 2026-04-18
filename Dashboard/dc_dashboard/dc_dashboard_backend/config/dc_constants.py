DC_GROUP_COLS = ["macro", "device", "siteX", "siteY", "Vd"]

DC_CAP_PARAMS = {"Cgs", "Cgd", "Cgg"}
DC_GM_GDS_PARAMS = {"gm", "gds"}
DC_FTFMAX_PARAMS = {"Ft_mean", "Ft", "Fmax", "Fmax_mean"}
DC_GENERIC_EXCLUDE_PARAMS = DC_CAP_PARAMS | DC_GM_GDS_PARAMS | DC_FTFMAX_PARAMS
