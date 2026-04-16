###validator 

from validation.common_utils.numeric_utils.conversion_num_series import safe_num
from validation.common_utils.dataframe_operation.df_generalize_name import pick_existing_column
from validation.common_utils.dataframe_operation.df_copy import to_pandas
from .Ft_check import validate_ft_vs_x
from .Fmax_check import validate_fmax_vs_x
from .Ft_Fmax_ratio_check import validate_ft_fmax_ratio


def validate_ft_fmax(groups, selected_param=None, x_axis="Vg"):
    results = []

    ft_names = ["Ft_mean", "Ft", "ft", "ft_mean"]
    fmax_names = ["Fmax", "Fmax_mean", "fmax", "fmax_mean"]

    for keys, group in groups:
        gpdf = to_pandas(group)

        if gpdf.empty:
            continue

        x_col = pick_existing_column(gpdf, [x_axis])
        ft_col = pick_existing_column(gpdf, ft_names)
        fmax_col = pick_existing_column(gpdf, fmax_names)

        if x_col is None:
            continue

        x = safe_num(gpdf[x_col])

        if selected_param in ft_names and ft_col is not None:
            y_ft = safe_num(gpdf[ft_col])
            score, checks = validate_ft_vs_x(x, y_ft, axis_name=x_axis)

            for section, detail, color in checks:
                results.append({
                    "keys": keys,
                    "param": ft_col,
                    "section": section,
                    "message": "PASS" if color == "green" else ("WARN" if color == "orange" else "FAIL"),
                    "detail": detail,
                    "color": color,
                })

            if fmax_col is not None:
                y_fmax = safe_num(gpdf[fmax_col])
                _, r_checks = validate_ft_fmax_ratio(y_ft, y_fmax)

                for section, detail, color in r_checks:
                    results.append({
                        "keys": keys,
                        "param": "Ft/Fmax Ratio",
                        "section": section,
                        "message": "PASS" if color == "green" else ("WARN" if color == "orange" else "FAIL"),
                        "detail": detail,
                        "color": color,
                    })

        elif selected_param in fmax_names and fmax_col is not None:
            y_fmax = safe_num(gpdf[fmax_col])
            y_ft = safe_num(gpdf[ft_col]) if ft_col is not None else None

            _, checks = validate_fmax_vs_x(x, y_fmax, ft_y=y_ft, axis_name=x_axis)

            for section, detail, color in checks:
                results.append({
                    "keys": keys,
                    "param": fmax_col,
                    "section": section,
                    "message": "PASS" if color == "green" else ("WARN" if color == "orange" else "FAIL"),
                    "detail": detail,
                    "color": color,
                })

            if y_ft is not None:
                _, r_checks = validate_ft_fmax_ratio(y_ft, y_fmax)

                for section, detail, color in r_checks:
                    results.append({
                        "keys": keys,
                        "param": "Ft/Fmax Ratio",
                        "section": section,
                        "message": "PASS" if color == "green" else ("WARN" if color == "orange" else "FAIL"),
                        "detail": detail,
                        "color": color,
                    })

    return results
