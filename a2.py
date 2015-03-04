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
      self.tempTestFile    = TemporaryFile();
      self.a2dArr          = np.random.random_integers(rangeOfRandInts, size=(square_dim,square_dim));
      self.writeABunchOfNumbersToATempFile();

   def writeABunchOfNumbersToATempFile(self):
      try:
         # Writes a bunch of numbers to a temp test file
         np.save(self.tempTestFile, self.a2dArr)
         self.tempTestFile.seek(0);
      except:
         print "error in writeABunchOfNumbersToAFile(...)"

class DataManager():
    # Assignment 1 class
    def __init__( self ):
        self.TwoD = [[]];

    def method1LoadAFileToTwoD( self, aFileObj ):
        try:
            self.TwoD = np.load(aFileObj);
        except:
            print "error in method1LoadAFileToTwoD(...)";

class TestUM(unittest.TestCase):
    # Data Manager tester
    def setUp(self):
        # Arrange: Create a test helper that provides
        # a file with a bunch of integers
        self.ts = TestHelper();
 
    def test_method1_load_a_file(self):
        # Arrange:
        # Act: 
        # Assert:
        expected = True;
        result   = False;
        self.assertEqual( expected,result) 

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