
"""
alguns mapas estavam com valos FCELL precisei forca-los para inteiro, e remove os FCELL
"""

import grass.script as grass
from grass.script import raster as grassR
import os
import string
import glob
import re
import fnmatch

list_tot=grass.mlist_grouped ('rast', pattern='*Bin*') ['PERMANENT']

for i in list_tot:
    grass.run_command("g.region",rast=i)
    if not "int" in i :
        print i
        grass.run_command("g.remove",flags="f",rast=i)
    #expressao2=i+"_int=int("+i+")"
    #grass.mapcalc(expressao2, overwrite = True, quiet = True)        
