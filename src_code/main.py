#main.py
#Created by Danielle Gunning
#The purpose of this code is to read a vector spatial data and return a geodataframe object,
# show vector spatial data, attribute table, row by row in the console,
# project vector spatial data from geographic coordinate system to a desired projected coordinate system
# save the output (projected layer) as shapefile to the output folder in your repository


import geopandas as gpd

#Steps are per pseudocode document

# Step 1 – Assign file path locations
FILEPATH_IN = r'C:\Users\danie\Downloads\Play_Equipment_75428547491116019\PLAY_EQUIPMENT.shp'
FILEPATH_OUT = r'C:\Users\danie\OneDrive\Documents\VSCode_output'

# Step 2 – Function to import source data and check for errors
def importSourceData():
    try:
        global geodata #Set as a global variable so this can be used in other functions
        geodata = gpd.read_file(FILEPATH_IN)
        return geodata
    except Exception as Error:
        print( "***************************ERROR********************* \n There is an error readng the file.\n Make sure the file exists, is not open and the filepath is correct.\n", Error)

# Step 3 – Function to show coordinate system of source data
def showSourceDataCoordinates():
    try:
        print("Coordinate Reference System:", geodata.crs)
    except Exception as Error:
        print( "***************************ERROR********************* \n There is an error showing the CRS of the file.\n Please make sure file has been imported and has a defined CRS.\n", Error)

#Step 4 – Display headings and first 5 rows of source data
def displayHeadingsandRowData():
    print(geodata.columns)
    print(geodata.head())

#Step 5 – Function to check that geometry fields are float data type
def checkCoordinateDataType():
    
    for index, row in geodata.iterrows():
        if isinstance(row.geometry.x, float) and isinstance(row.geometry.y, float):
            None
        else:
            print("Coordinates are not the correct data type")
       

#Step 6 – Function to set target CRS, reproject shapefile to new CRS
def setCRSandReproject(EPSG = 7856): 
    try: 
        global geodata #Reset as a global variable because the reprojected data replaces the original geodata
        geodata = geodata.to_crs(epsg=EPSG)
        print(f"File successfully reprojected to EPSG:{EPSG}")
    except Exception as Error:
        print( "***************************ERROR********************* \n There is an error reproecting the dataset.\n ", Error)
#Step 7 - save as new shapefile and check for errors
def saveAsShapefile():
    try:
        fulloutputPathWithFileName = FILEPATH_OUT + "\\" + "Play_Equipment_Reprojection_MGA_Zone56.shp" 
        geodata.to_file(fulloutputPathWithFileName, driver="ESRI Shapefile")
        print("File successfully saved")
    except Exception as Error:
        print( "***************************ERROR********************* \n There is an error saving the file.\n ", Error)

#Step 8 – Invoke all functions 
if __name__ == "__main__":
    importSourceData()
    showSourceDataCoordinates()
    displayHeadingsandRowData()
    checkCoordinateDataType()
    setCRSandReproject()
    saveAsShapefile()
