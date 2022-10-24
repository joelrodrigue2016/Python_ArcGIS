def raster_mosaic_combination(path):
    import arcpy
    from arcpy import env
    path = "C:\\Users\\joel.rodriguez\\Downloads\\test"
    env.workspace = path
    arcpy.Mosaic_management(



        
    #tiff files, Make sure that they follow this pattern
    "file1.tif; file2.tif;  file4.tif;  file5.tif;  file6.tif",


            ##===========================================================================================================================================
            ##Mosaic
            ##Usage: Mosaic_management inputs;inputs... target {LAST | FIRST | BLEND | MEAN | MINIMUM | MAXIMUM} {FIRST | REJECT | LAST | MATCH} 
            ##                         {background_value} {nodata_value} {NONE | OneBitTo8Bit} {mosaicking_tolerance}  
            ##                         {NONE | STATISTIC_MATCHING | HISTOGRAM_MATCHING 
            ##                         | LINEARCORRELATION_MATCHING}

            ## if not sure leave this configuration the way it is
            
            ##===========================================================================================================================================
            



    #tiff file target raster
    "file3.tif","LAST","FIRST","0","9","","","")


          


    print("Done")

def main():
    try:
        path = "C:\\Users\\joel.rodriguez\\Downloads\\test"
        raster_mosaic_combination(path)
    except Exception as e:
        print(e)

if __name__ =="__main__":
    main()
