exec(open("../settings/yaml_variables.py").read())
import pickle

# STUDY AREA
study_area_fp = f"../data/study_area_polygon/{study_area}/study_area_polygon.gpkg"

# MUNICIPALITIES
muni_polygons_fp = f"../data/municipalities/{study_area}/raw/municipalities.gpkg"
muni_pop_fp = f"../data/municipalities/{study_area}/raw/muni_pop.csv"

# OSM filepaths
osm_processed_fp = f"../data/osm/{study_area}/processed/"

osm_graph_fp = osm_processed_fp + "osm_graph.graphml"
osm_graph_simplified_fp = osm_processed_fp + "osm_simplified_graph.graphml"

osm_edges_fp = osm_processed_fp + "osm_edges.parquet"
osm_nodes_fp = osm_processed_fp + "osm_nodes.parquet"
osm_edges_simplified_fp = osm_processed_fp + "osm_edges_simplified.parquet"
osm_nodes_simplified_fp = osm_processed_fp + "osm_nodes_simplified.parquet"

osm_edges_joined_fp = osm_processed_fp + "osm_edges_joined.parquet"
osm_nodes_joined_fp = osm_processed_fp + "osm_nodes_joined.parquet"
osm_edges_simplified_joined_fp = (
    osm_processed_fp + "osm_edges_simplified_joined.parquet"
)
osm_nodes_simplified_joined_fp = (
    osm_processed_fp + "osm_nodes_simplified_joined.parquet"
)

osm_grid_fp = osm_processed_fp + "grid.parquet"
osm_intrinsic_grid_fp = (
    f"../results/osm/{study_area}/data/grid_results_intrinsic.pickle"
)

osm_intrinsic_fp = f"../results/osm/{study_area}/data/intrinsic_analysis.json"

osm_meta_fp = osm_processed_fp + "osm_meta.json"

osm_results_fp = f"../results/osm/{study_area}/"

osm_results_static_maps_fp = f"../results/osm/{study_area}/maps_static/"
osm_results_inter_maps_fp = f"../results/osm/{study_area}/maps_interactive/"
osm_results_plots_fp = f"../results/osm/{study_area}/plots/"
osm_results_data_fp = f"../results/osm/{study_area}/data/"

# Reference filepaths
ref_processed_fp = f"../data/reference/{study_area}/processed/"

ref_graph_fp = ref_processed_fp + "ref_graph.graphml"
ref_graph_simplified_fp = ref_processed_fp + "ref_simplified_graph.graphml"

ref_edges_fp = ref_processed_fp + "ref_edges.parquet"
ref_nodes_fp = ref_processed_fp + "ref_nodes.parquet"
ref_edges_simplified_fp = ref_processed_fp + "ref_edges_simplified.parquet"
ref_nodes_simplified_fp = ref_processed_fp + "ref_nodes_simplified.parquet"

ref_edges_joined_fp = ref_processed_fp + "ref_edges_joined.parquet"
ref_nodes_joined_fp = ref_processed_fp + "ref_nodes_joined.parquet"
ref_edges_simplified_joined_fp = (
    ref_processed_fp + "ref_edges_simplified_joined.parquet"
)
ref_nodes_simplified_joined_fp = (
    ref_processed_fp + "ref_nodes_simplified_joined.parquet"
)

ref_grid_fp = ref_processed_fp + "grid.parquet"
ref_intrinsic_grid_fp = (
    f"../results/reference/{study_area}/data/grid_results_intrinsic.pickle"
)

ref_intrinsic_fp = f"../results/reference/{study_area}/data/intrinsic_analysis.json"

ref_results_fp = f"../results/reference/{study_area}/"

ref_results_static_maps_fp = f"../results/reference/{study_area}/maps_static/"
ref_results_inter_maps_fp = f"../results/reference/{study_area}/maps_interactive/"
ref_results_plots_fp = f"../results/reference/{study_area}/plots/"
ref_results_data_fp = f"../results/reference/{study_area}/data/"

# COMPARE DATA FILEPATH
compare_processed_fp = f"../data/compare/{study_area}/processed/"

# COMPARE RESULTS FILEPATHS
compare_results_fp = f"../results/reference/{study_area}/"

compare_results_static_maps_fp = f"../results/compare/{study_area}/maps_static/"
compare_results_inter_maps_fp = f"../results/compare/{study_area}/maps_interactive/"
compare_results_plots_fp = f"../results/compare/{study_area}/plots/"
compare_results_data_fp = f"../results/compare/{study_area}/data/"

# POPULATION RASTER FILEPATHS
pop_fp_1 = f"../data/population/{study_area}/raw/GHS_POP_E2020_GLOBE_R2022A_54009_100_V1_0_R3_C19/GHS_POP_E2020_GLOBE_R2022A_54009_100_V1_0_R3_C19.tif"
pop_fp_2 = f"../data/population/{study_area}/raw/GHS_POP_E2020_GLOBE_R2022A_54009_100_V1_0_R3_C20/GHS_POP_E2020_GLOBE_R2022A_54009_100_V1_0_R3_C20.tif"

pop_processed_fp = "../data/population/dk/processed/"

# ANALYSIS FILEPATHS
compare_analysis_fp = f"../results/compare_analysis/{study_area}/"
osm_analysis_fp = f"../results/osm_analysis/{study_area}/"
ref_analysis_fp = f"../results/ref_analysis/{study_area}/"

compare_analysis_plots_fp = compare_analysis_fp + "plots/"
compare_analysis_data_fp = compare_analysis_fp + "data/"

osm_analysis_plots_fp = osm_analysis_fp + "plots/"
osm_analysis_data_fp = osm_analysis_fp + "data/"

ref_analysis_plots_fp = ref_analysis_fp + "plots/"
ref_analysis_data_fp = ref_analysis_fp + "data/"
