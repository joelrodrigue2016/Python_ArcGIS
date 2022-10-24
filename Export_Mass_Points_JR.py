#Function
def export_mass_points(infc,outfile ):
    
    # Import system modules
    import sys, string, os, arcgisscripting, shutil, fileinput
    gp = arcgisscripting.create()



    #********Set the necessary product code
    gp.SetProduct("ArcView")
    #gp.Workspace = r"c:\testing"
    gp.checkoutextension("3D")
    gp.toolbox = "3D"

    #Open output text file
    txtfile = open(outfile, "w")

    #********Create search cursor
    rows = gp.SearchCursor(infc)
    row = rows.Next()
    #********Enter while loop for each catchment or feature/row
    while row:
        feat = row.shape
        zval = row.grid_code
        pnt = feat.getpart()
        txtfile.write (str(pnt.x) + "," + str(pnt.y) + "," + str(zval) + "\n")
        row = rows.Next()
    txtfile.close()
    del gp
    del rows
    print("Done")
    
#running file through the main function

def main():
    #cathring any exceptions
    try:
        #shapefile name and location
        infc = "K:/SAR_Civil/048028040 - Encompass Rehab Hospital - UVA/GIS/Data/AOI/points_two_areas.shp"
        #output of text file
        outfile = "K:/SAR_Civil/048028040 - Encompass Rehab Hospital - UVA/GIS/Data/AOI/poi2nts_two_areas.txt"
        export_mass_points(infc,outfile)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
