import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "K:/SAR_Civil/Encompass Site Investigation/Encompass - Bismarck ND/GIS/Data/TIFF"
outTimes = Times("USGS_1_n47w101.tif",3.28084 )  #meters to feet, (0.3048 feet to meters)
outTimes.save("K:/SAR_Civil/Encompass Site Investigation/Encompass - Bismarck ND/GIS/Data/TIFF/feet/output.tif")  #Name of file at the end.
