import arcpy
from arcpy import env
arcpy.env.workspace=r"E:\data_2015\___john\Gabi_mapeamento_2015_05_d28\Shp_Paisagens_point\Pontos_vwhat_merge_join_split"

fc=arcpy.ListFeatureClasses()
dropFields = ["cat_"]
for i in fc:
    arcpy.DeleteField_management(i.replace('.shp',""),dropFields)
    
    
    
arcpy.env.workspace=r"F:\data\john_pc2\Gabriele\PONTOS\points_join_input_vwhat_split"

fc=arcpy.ListFeatureClasses()
dropFields = ["cat_"]
for i in fc:
    arcpy.DeleteField_management(i.replace('.shp',""),dropFields)