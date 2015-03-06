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
   def __init__(self, upperIntRangeLim = 100, square_dim = 10 ):
      self.aTempFile    = TemporaryFile();
      # create the 10 x 10 array of integers
      self.a2dArr          = np.arange(0, upperIntRangeLim).reshape(square_dim,square_dim);
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
        self.normalizedTwoD = np.array([[]]);
        self.extractedArray = np.array([[]]);

    def readArrayFromFile( self, aFileObj ):
        try:
            self.TwoD = np.load(aFileObj);
        except:
            raise Exception("error in method1LoadAFileToTwoD(...)");

    def extractSectionOfTwoDArray( self, rowIndexesToExtract = [], colIndexesToExtract = [] ):
       # Extract a section of the DataManager's internal 2D numpy array using a row/column 
       # filter mask
        try:
           rowAxisNdx      = 0;
           columnAxisNdx   = 1;
           # Build a row filter mask
           row_filter_mask = np.array( [True if i in rowIndexesToExtract else False for i in range(0, int(self.TwoD.shape[rowAxisNdx]))] );
           # Build a column filter mask
           col_filter_mask = np.array( [True if i in colIndexesToExtract else False for i in range(0, int(self.TwoD.shape[columnAxisNdx]))] );

           # split
           subSection          = self.TwoD[ row_filter_mask ];
           self.extractedArray = subSection[:,col_filter_mask];
        except:
            raise Exception("error in extractSectionOfArray(...)");

    def normalizeTwoDArray( self, a = 1.0, b = 0.0, normAxis = 0 ):
        '''
        Normalizes numpy array values to be between arbitrary points 'a' and 'b' 
        along specified 'normaxis' using generalized feature scaling method.
        ref:
        http://en.wikipedia.org/wiki/Normalization_%28statistics%29#Examples
        '''
        try:
            mins                = np.min(self.TwoD, axis=normAxis);
            maxs                = np.max(self.TwoD, axis=normAxis);
            range               = maxs - mins;
            self.normalizedTwoD = a + ((self.TwoD - mins ) * (b - a) / range);
        except:
            raise Exception("error in normalizeTwoDArray(...)");

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
        # Arrange: Create a DataMananger with loaded data
        dataManager = DataManager();
        dataManager.readArrayFromFile(self.helper.aTempFile); 
        # Act: Extract a section of the array
        rowIndexesToExtract = [3, 5, 7, 9];
        colIndexesToExtract = [2, 4, 6, 8];
        dataManager.extractSectionOfTwoDArray(rowIndexesToExtract, colIndexesToExtract);
        # Assert: Extracted section matches expected array dimensions
        expected    = (4,4);
        result      = dataManager.extractedArray.shape;
        self.assertEqual( expected,result );

    def test_twod_normalization(self):
        # Arrange: Create a DataMananger with loaded data and extracted subarray
        dataManager = DataManager();
        dataManager.readArrayFromFile(self.helper.aTempFile); 
        rowIndexesToExtract = [3, 5, 7, 9];
        colIndexesToExtract = [2, 4, 6, 8];
        dataManager.extractSectionOfTwoDArray(rowIndexesToExtract, colIndexesToExtract);
        # Act: Normalize extracted array
        dataManager.normalizeTwoDArray();
        # Assert: All normalized values are between 0 and 1
        expected    = True;
        result      = [ True if (0.0 <= i <= 1.0) else False for i in np.ravel(dataManager.normalizedTwoD)];
        result      = True if (result.count(False) == 0) else False;
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
