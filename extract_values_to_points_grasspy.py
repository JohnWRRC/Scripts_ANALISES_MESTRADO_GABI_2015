import grass.script as grass
from grass.script import raster as grassR
import os
import string
import glob
import re
import fnmatch



lista_rasters_maps_old=grass.mlist_grouped ('rast', pattern='*Bin*') ['PERMANENT']

lista_vect_maps_old=grass.mlist_grouped ('vect', pattern='*id_2*') ['PERMANENT']

for i in lista_vect_maps_old: 
        check="id2_"+i[40:41]

        for a in lista_rasters_maps_old:
                if "FRAG60m_mata_clump_AreaHA" in a:
                        if check in a:
                                grass.run_command('g.region',rast=a)
                                grass.run_command('v.what.rast', vector=i,raster=a, column="FG060")
                
                
                if "FRAG120m_mata_clump_AreaHA" in a:
                        if check in a:
                                grass.run_command('g.region',rast=a)
                                grass.run_command('v.what.rast', vector=i,raster=a, column="FG120")                
   
                if "patch_clump_mata_limpa_AreaHA" in a:
                        if check in a:
                                grass.run_command('g.region',rast=a)
                                grass.run_command('v.what.rast', vector=i,raster=a, column="PATCH")   
   
   
   
   
   
                                
lista_rasters_maps_new=grass.mlist_grouped ('rast', pattern='*segment*') ['PERMANENT']
lista_vect_maps_new=grass.mlist_grouped ('vect', pattern='*10SP*') ['PERMANENT']
   
   
for i in lista_vect_maps_new:
        format=i[36:38]
        format=format.replace("_","")
        format="00"+format
        format=format[-2:]
        check="FID_"+format
        for a in lista_rasters_maps_new:
                if check in a:
                        if "FRAG60m_mata_clump_AreaHA" in a:
                                                      
                                grass.run_command('g.region',rast=a)
                                grass.run_command('v.what.rast', vector=i,raster=a, column="FG060")                        
                        
                        
                        if "FRAG120m_mata_clump_AreaHA" in a:
                                if check in a:
                                        grass.run_command('g.region',rast=a)
                                        grass.run_command('v.what.rast', vector=i,raster=a, column="FG120")                
                                   
                        if "patch_clump_mata_limpa_AreaHA" in a:
                                if check in a:
                                        grass.run_command('g.region',rast=a)
                                        grass.run_command('v.what.rast', vector=i,raster=a, column="PACTH")                        

 