#-------------------------------------------------------------------------------
# Name:        cs612-a2
# Description: Assignment 2
#
# Author:      kingrichard2005
#
# Created:     2015-02-03
# Copyright:   (c) kingrichard2005 2015
# Licence:     MIT
#-------------------------------------------------------------------------------
import numpy as np
import unittest
from tempfile import TemporaryFile

class TestHelper():
   # A test helper class

   # default square dimension (10) per assignment reqs
   def __init__(self, rangeOfRandInts = 100, square_dim = 10 ):
      self.aTempFile    = TemporaryFile();
      # create the 10 x 10 array of integers
      self.a2dArr          = np.random.random_integers(rangeOfRandInts, size=(square_dim,square_dim));
      # save the 10 x 10 array of integers to a temp file and keep handle for reference
      self.saveInitializedArraytoATempFile();

   def saveInitializedArraytoATempFile(self):
      try:
         # Writes a bunch of numbers to a temp test file
         np.save(self.aTempFile, self.a2dArr)
         self.aTempFile.seek(0);
      except:
         print "error in writeABunchOfNumbersToAFile(...)"

class DataManager():
    # Class to manage input data
    def __init__( self ):
        self.TwoD           = np.array([[]]);
        self.extractedArray = np.array([[]]);

    def readArrayFromFile( self, aFileObj ):
        try:
            self.TwoD = np.load(aFileObj);
        except:
            raise Exception("error in method1LoadAFileToTwoD(...)");

    def extractSectionOfArray( self, rowIndexesToExtract = [], colIndexesToExtract = [] ):
        try:
            pass;
        except:
            raise Exception("error in extractSectionOfArray(...)");

class TestUM(unittest.TestCase):
    # Data Manager tester
    def setUp(self):
        # Arrange: Create a test helper that provides
        # a file with a bunch of integers
        self.helper = TestHelper();
 
    def test_load_a_file(self):
        # Arrange: Create a DataMananger
        dataManager = DataManager();
        # Act: Read
        dataManager.readArrayFromFile(self.helper.aTempFile); 
        # Assert: The loaded array matches the 10 x 10 array read from a file
        expected    = self.helper.a2dArr;
        result      = dataManager.TwoD;
        self.assertEqual( np.array_equal(expected,result), True );

    def test_extracted_portion_matches_dimensions(self):
        # Arrange: Create a DataMananger
        dataManager = DataManager();
        dataManager.readArrayFromFile(self.helper.aTempFile); 
        # Act: Extract a section of the array
        rowIndexesToExtract = [3, 5, 7, 9];
        colIndexesToExtract = [2, 4, 6, 8];

        # Assert: Extracted section matches expected array dimensions
        expected    = (4,4);
        result      = dataManager.extractedArray.shape;
        self.assertEqual( expected,result );

if __name__ == "__main__":
    #unittest.main();
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestUM));
    #print "testing complete"
    #ts          = TestHelper();
    #dataManager = DataManager();
    #dataManager.method1LoadAFileToOneD(ts.tempTestFile);
    #dataManager.method2CreateTwoD();
    #dataManager.method3SortOneD();
    #dataManager.method4PartitionTwoD();
    #dataManager.method5PlacePartitionsInFiles()
