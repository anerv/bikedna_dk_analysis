
import yaml

with open(r"../config.yml") as file:

    parsed_yaml_file = yaml.load(file, Loader=yaml.FullLoader)

    # Settings for plot resolution
    plot_res = parsed_yaml_file["plot_resolution"]

    # Settings for study area
    study_area = parsed_yaml_file["study_area"]
    area_name = parsed_yaml_file["area_name"]
    study_crs = parsed_yaml_file["study_crs"]

    # Settings for reference data
    reference_name = parsed_yaml_file["reference_name"]
#     # Settings for OSM data
#     bicycle_infrastructure_queries = parsed_yaml_file["bicycle_infrastructure_queries"]
#     osm_bicycle_infrastructure_type = parsed_yaml_file[
#         "osm_bicycle_infrastructure_type"
#     ]
#     simplify_tags_queries = parsed_yaml_file["simplify_tags_queries"]
    
#     osm_way_tags = parsed_yaml_file["osm_way_tags"]

#     # Settings for reference data
#     reference_geometries = parsed_yaml_file["reference_geometries"]
#     bicycle_bidirectional = parsed_yaml_file["bidirectional"]
#     ref_bicycle_infrastructure_type = parsed_yaml_file[
#         "ref_bicycle_infrastructure_type"
#     ]
#     reference_id_col = parsed_yaml_file["reference_id_col"]
      

#     grid_cell_size = parsed_yaml_file["grid_cell_size"]

#     existing_tag_dict = parsed_yaml_file["existing_tag_analysis"]
#     incompatible_tags_dict = parsed_yaml_file["incompatible_tags_analysis"]

# study_area_poly_fp = (
#     f"../../data/study_area_polygon/{study_area}/study_area_polygon.gpkg"
# )
# reference_fp = f"../../data/reference/{study_area}/processed/reference_data.parquet"
