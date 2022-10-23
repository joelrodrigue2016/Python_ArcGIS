"""When using natural neighbors interpolation, consider specifying a sampling distance that's equal to or above half of
the average point spacing of the data points in the surface.

When using the Interpolate Vertices Only option, features with vertices that fall outside the data area of the surface
will not be part of the output unless the input surface is a raster and the nearest neighbor interpolation method is
 being used."""

def Shape_interpolation(path, shapefile1, lidar_file, shapefile2):
    # Import system modules
    import arcpy
    from arcpy.sa import InterpolateShape

    # Check out the ArcGIS Spatial Analyst extension license
    arcpy.CheckOutExtension("Spatial")

    # Set the analysis environments
    arcpy.env.workspace = path

    # Set the local variables
    inFeatureClass = shapefile1
    inSurface = lidar_file
    OutFeatureClass = shapefile2
    """Specifies the interpolation method that will be used to determine elevation values for the output features.
     The available options depend on the surface type being used.

    BILINEAR—Determines the value of the query point using bilinear interpolation. This is the default when the input
     is a raster surface.
    
    NEAREST—Determines the value of the query point using nearest neighbor interpolation. When this method is used,
    surface values will only be interpolated for the input feature's vertices. This option is only available for a raster 
    surface.
    
    LINEAR— Default interpolation method for TIN, terrain, and LAS dataset. It obtains elevation from the plane defined 
    by the triangle that contains the XY location of a query point.
    
    NATURAL_NEIGHBORS— Obtains elevation by applying area-based weights to the natural neighbors of a query point.
    
    CONFLATE_ZMIN— Obtains elevation from the smallest z-value found among the natural neighbors of a query point.
    
    CONFLATE_ZMAX— Obtains elevation from the largest z-value found among the natural neighbors of a query point.
    
    CONFLATE_NEAREST— Obtains elevation from the nearest value among the natural neighbors of a query point.
    
    CONFLATE_CLOSEST_TO_MEAN— Obtains elevation from the z-value that is closest to the average of all the natural 
    neighbors of a query point."""

    method = "NEAREST"

    # Execute the tool
    InterpolateShape(inSurface, inFeatureClass, OutFeatureClass, 15, 1, method, True)
    print("Done")


def main():
    try:
        path = "C:/Users/Joel/Documents/pyqgis/test_delete interpolation tool"
        # shapefile containing the data
        shapefile1 = "points.shp"
        # LAS Dataset Layer; Mosaic Layer; Raster Layer; Terrain Layer; TIN Layer; Image Service
        lidar_file = "USGS_OPR_FL_Peninsular_FDEM_2018_D19_DRRA_DEM478097.tif"
        # just give a name to the shapefile and it will create it with the name given
        shapefile2 = "points4.shp"
        # running the function
        Shape_interpolation(path, shapefile1, lidar_file, shapefile2)

    except Exception as e:
        # exception error
        print(e)


if __name__ == "__main__":
    main()
