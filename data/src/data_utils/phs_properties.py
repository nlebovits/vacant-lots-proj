from classes.featurelayer import FeatureLayer
from constants.services import PHS_LAYERS_TO_LOAD


def phs_properties(primary_featurelayer):
    phs_properties = FeatureLayer(
        name="PHS Properties", esri_rest_urls=PHS_LAYERS_TO_LOAD
    )

    red_cols_to_keep = [
        "BRT_ID",
        "COMM_PARTN"
    ]

    phs_properties = phs_properties.gdf[red_cols_to_keep]

    rename_columns = {
    "BRT_ID": "opa_id",
    "COMM_PARTN": "phs_partner_agency"
    }

    phs_properties.rename(columns=rename_columns, inplace=True)

    primary_featurelayer.gdf = primary_featurelayer.gdf.merge(
        phs_properties, how="left", on="opa_id"
    )

    primary_featurelayer.gdf["phs_partner_agency"].fillna("None", inplace=True)

    return primary_featurelayer
