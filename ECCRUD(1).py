from pymongo import MongoClient

from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations Animal collection in MongoDB """

    def __init__(self,username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:51019/?authMechanism=DEFAULT&authSource=AAC' % (username, password))
        self.database = self.client['AAC']
        
# Complete this create method to implement the C in CRUD.
    def create(self, insertdata):
        if insertdata is not None:
            self.database.animals.insert(insertdata)  # data should be dictionary
            return True# prints True on screen data was inserted


# Create method to implement the R in CRUD. 
    def read(self, readdata):
        if readdata is not None:
            result = self.database.animals.find(readdata)  # lookup should be dictionary  
            return result
        else:
            error = 'Error, no results found.'
            return error

# Update in CRUD.
    def update(self,finddata, newdata):
        #Storing user values and creating local
        searchRecord = finddata
        updateRecord = newdata

    # if else for updating
        if newdata is not None:
            changeResult = self.database.find_one_and_update(finddata, newdata)
            return changeResult
        else:
            error = 'Error, no results updated'
            return error
#Delete in Crud
    def delete(self, animalRecord):
    
        # Get deletion record
        if animalRecord is not None:
            deleteRecord = self.database.animals.delete_one(animalRecord)
            return deleteRecord
        else:
            return("Deletion failed")
#readall
    def readall(self,readalldata):
        if readalldata is not None:
            finddata = self.database.animals.find(readalldata)
            return finddata
        else:
            return("Haha")    