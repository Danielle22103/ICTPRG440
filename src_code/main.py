#main.py
#Created by Danielle Gunning
#The purpose of this code is to read a vector spatial data and return a geodataframe object,
# show vector spatial data, attribute table, row by row in the console,
# project vector spatial data from geographic coordinate system to a desired projected coordinate system
# save the output (projected layer) as shapefile to the output folder in your repository


import geopandas as gpd #imported geopandas from python library to use working with geospatial data.

#Steps are per my pseudocode document

# Step 1 – Assign file path locations
FILEPATH_IN = r'C:\Users\danie\Downloads\Play_Equipment_75428547491116019\PLAY_EQUIPMENT.shp' #filepath of source data file. 
print(type(FILEPATH_IN)) #Prints data type of source data. Should be <class 'str'>
FILEPATH_OUT = r'C:\Users\danie\OneDrive\Documents\VSCode_output' #folder filepath of output shapefile data. String datatype.
print(type(FILEPATH_OUT)) #prints data type of output folder filepath. Should be <class 'str'>


# Step 2 – Function to import source data and check for errors
def importSourceData(): 
    try:
        global geodata #Set as a global variable so this can be used in other functions
        geodata = gpd.read_file(FILEPATH_IN) #reads the source data and loads it as a geodataframe
        print(type(geodata)) #prints the datatype of the geodataframe. Should be <class 'geopandas.geodataframe.GeoDataFrame'>
        return geodata #returns the loaded geodataframe
    except Exception as Error:  #returns an error if the source data input cannot be read. 
                                #This can be due to the file not existing, file corruption, the wrong filepath address, or if the file 
                                #is being used and is locked.
        print( "***************************ERROR********************* \n" +
              "There is an error readng the file.\n " + 
              "Make sure the file exists, is not open and the filepath is correct.\n", Error)


# Step 3 – Function to show coordinate system of source data
def showSourceDataCoordinates(): 
    try:
        print("Coordinate Reference System:", geodata.crs)  #This prints text within the quotation and the coodinate reference system of the source data
    except Exception as Error: #If the GeoDataFrame hasn't been loaded or the CRS is undefined, an error message is displayed.
        print( "***************************ERROR********************* \n" +
              "There is an error showing the CRS of the file.\n" + 
              "Please make sure file has been imported and has a defined CRS.\n", Error)

#Step 4 – Display headings and first 5 rows of source data
def displayHeadingsandRowData(): 
    print(geodata.columns) # Lists all column headers in the attribute table.
    print(type(geodata.columns)) #Prints the data type of the geodata columns. ( dtype='object'))
    print(geodata.head()) #Displays the first 5 rows within the attribute table within the geodataframe
    print(type(geodata.head)) #Prints the datatype of the attribute table (the geodataframe). (<class 'geopandas.geodataframe.GeoDataFrame'>)


#Step 5 – Function to check that geometry fields are float data type: 
def checkCoordinateDataType(): 
    for index, row in geodata.iterrows():   #interates through each row in the geodataframe, the index relates to the row numeber. 
                                            #The row prints the value of that row
         
        if isinstance(row.geometry.x, float) and isinstance(row.geometry.y, float): #checks the X and Y geometry fields are floats
            pass #if both the values of the X and Y data ARE floats, do nothing
        else:
            print("Coordinates are not the correct data type") #print the qoute if there is arow with incorrect (float) data types.
        #print(type(row.geometry.x)) this would print every row of the X cooridnates with the datatype
        #print(type(row.geometry.y)) rhis would print every row of the Y coordinate with the datatype
       

#Step 6 – Function to set target CRS, reproject shapefile to new CRS
def setCRSandReproject(EPSG = 7856): #parameter is the EPSG of GDA2020 MGA Zone 56
    try: 
        global geodata #Reset as a global variable because the reprojected data replaces the original geodata
        geodata = geodata.to_crs(epsg=EPSG) # Reprojects the data to the specified EPSG code
        print(f"File successfully reprojected to EPSG:{EPSG}") #prints the quote and the EPSG parameter set within the function title
    except Exception as Error: #If the reprojection fails, prints the comment within the qoutation and the error
        print( "***************************ERROR********************* \n There is an error reproecting the dataset.\n ", Error)


#Step 7 - save as new shapefile and check for errors
def saveAsShapefile(): 
    try:
        fulloutputPathWithFileName = FILEPATH_OUT + "\\" + "Play_Equipment_Reprojection_MGA_Zone56.shp" 
        #Combines the FILEPATH_OUT folder path with the new filename
        geodata.to_file(fulloutputPathWithFileName, driver="ESRI Shapefile") #Saves the reprojected geodata to the specified location in ESRI Shapefile format
        print("File successfully saved") #prints commonet witihn qoutation 
    except Exception as Error: #if there is an error saving the file, print comments within quotation and the error
        print( "***************************ERROR********************* \n There is an error saving the file.\n ", Error)

#Step 8 – Invoke all functions 
if __name__ == "__main__": #this is the main exection block
    #functions are loaded in the sequence below
    importSourceData()
    showSourceDataCoordinates()
    displayHeadingsandRowData()
    checkCoordinateDataType()
    setCRSandReproject()
    saveAsShapefile()
