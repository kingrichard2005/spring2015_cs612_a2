#!/usr/bin/python2.7
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

class Homework2():
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

    def get_ten_by_ten_array(self):
        try:
            pass;
        except:
            raise Exception ("error in get_ten_by_ten_array()");

    def get_selected_row_indicies(self, selected_row_indicies = [], section = []):
        try:
            rowAxisNdx      = 0;
            # Build a row filter mask
            row_filter_mask = np.array( [True if i in selected_row_indicies else False for i in range(0, int(section.shape[rowAxisNdx]))] );
            return section[ row_filter_mask ];
        except:
            raise Exception ("error in get_selected_row_indicies(...)");

    def get_selected_column_indicies(self, selected_column_indicies = [], section = []):
        try:
            columnAxisNdx   = 1;
            # Build a column filter mask
            col_filter_mask = np.array( [True if i in selected_column_indicies else False for i in range(0, int(self.TwoD.shape[columnAxisNdx]))] );
            return section[:,col_filter_mask];
        except:
            raise Exception ("error in get_selected_column_indicies(...)");

    def get_subarray( self, selected_row_indicies = [], selected_column_indicies = [] ):
        '''
           Extract a section of the DataManager's internal 2D numpy array using a row/column 
           filter mask.
        '''
        try:
           section             = self.get_selected_row_indicies( selected_row_indicies, self.TwoD );
           self.extractedArray = self.get_selected_column_indicies(selected_column_indicies, section = section)
           return self.extractedArray;
        except:
            raise Exception("error in extractSectionOfArray(...)");

    def get_normalized_array( self, a = 1.0, b = 0.0, normAxis = 0 ):
        '''
        Normalizes numpy array values to be between arbitrary points 'a' and 'b' 
        along specified 'normaxis' using generalized feature scaling method.
        ref:
        http://en.wikipedia.org/wiki/Normalization_%28statistics%29#Examples
        '''
        try:
            mins                = np.min(np.ravel(self.TwoD), axis=normAxis);
            maxs                = np.max(np.ravel(self.TwoD), axis=normAxis);
            range               = maxs - mins;
            self.normalizedTwoD = a + ((self.TwoD - mins ) * (b - a) / range);
            self.normalizedTwoD = np.round(self.normalizedTwoD, decimals = 2);
        except:
            raise Exception("error in normalizeTwoDArray(...)");

    def get_mean(self, array):
        '''
            This function gets the array and returns the mean of all elements
            You must use the built_in function of mean to do this question
        '''
        try:
            theMean = np.mean(array);
            return theMean;
        except:
            raise Exception("");

    def get_ten_by_ten_median(self, array):
        '''
            This function gets the array and returns the median of all elements
            You must use the built_in function of median to do this question
        '''
        try:
            theMedian = np.median(self.TwoD);
            return theMedian;
        except:
            raise Exception("error in get_ten_by_ten_median");

    def get_ten_by_ten_standard_deviation(self, array):
        '''
            This function gets the array and returns the standard deviation of all elements
            You must use the built_in function of standard deviation to do this question
        '''
        try:
            theStdDev = np.std(array);
            return theStdDev;
        except:
            raise Exception("error in get_ten_by_ten_standard_deviation");

class TestSequenceFunctions(unittest.TestCase):
    # Data Manager tester
    def setUp(self):
        # Arrange: Create a test helper that provides
        # a file with a bunch of integers
        self.helper = TestHelper();
 
    def test_get_ten_by_ten(self):
        # Arrange: Create a Homework2 class object
        homework2 = Homework2();
        # Act: get 10 x 10 array
        homework2.readArrayFromFile(self.helper.aTempFile); 
        # Assert: 10 x 10 array expected
        expected = np.array([[ 0,  1,  2,  3,  4,  5,  6, 7,  8,  9],
                     [10, 11, 12, 13, 14, 15, 16,17, 18, 19],
                     [20, 21, 22, 23, 24, 25, 26,27, 28, 29],
                     [30, 31, 32, 33, 34, 35, 36,37, 38, 39],
                     [40, 41, 42, 43, 44, 45, 46,47, 48, 49],
                     [50, 51, 52, 53, 54, 55, 56,57, 58, 59],
                     [60, 61, 62, 63, 64, 65, 66,67, 68, 69],
                     [70, 71, 72, 73, 74, 75, 76,77, 78, 79],
                     [80, 81, 82, 83, 84, 85, 86,87, 88, 89],
                     [90, 91, 92, 93, 94, 95, 96,97, 98, 99]])
        result      = homework2.TwoD;
        print "test_get_ten_by_ten result:\n{0}".format(result);
        self.assertEqual( np.array_equal(expected,result), True );

    def test_get_selected_row_indidicies(self):
        # Arrange: Create a DataMananger with loaded data
        dataManager = Homework2();
        dataManager.readArrayFromFile(self.helper.aTempFile); 
        #Act: Get selected row indicies
        rowIndexesToExtract = [3, 5, 7, 9];
        result = dataManager.get_selected_row_indicies(selected_row_indicies = rowIndexesToExtract, section = dataManager.TwoD);
        # Assert: Extracted section matches expected array dimensions
        expected    = (4,10);
        result      = result.shape;
        self.assertEqual( expected,result );

    def test_get_selected_col_indidicies(self):
        # Arrange: Create a DataMananger with loaded data
        dataManager = Homework2();
        dataManager.readArrayFromFile(self.helper.aTempFile); 
        #Act: Get selected column indicies
        rowIndexesToExtract = [3, 5, 7, 9];
        colIndexesToExtract = [2, 4, 6, 8];
        rowSection          = dataManager.get_selected_row_indicies(selected_row_indicies = rowIndexesToExtract, section = dataManager.TwoD);
        colsection          = dataManager.get_selected_column_indicies( selected_column_indicies = colIndexesToExtract, section = rowSection );
        # Assert: Extracted section matches expected array dimensions
        expected    = (4,4);
        result      = colsection.shape;
        self.assertEqual( expected,result );
      
    def test_select_rows_and_columns_by_arrays(self):
        # Arrange: Create a DataMananger with loaded data
        dataManager = Homework2();
        dataManager.readArrayFromFile(self.helper.aTempFile); 
        # Act: Extract a section of the array
        rowIndexesToExtract = [3, 5, 7, 9];
        colIndexesToExtract = [2, 4, 6, 8];
        subArray = dataManager.get_subarray(rowIndexesToExtract, colIndexesToExtract);
        # Assert: Extracted section matches expected array dimensions
        expected    = (4,4);
        result      = subArray.shape;
        print "test_extracted_portion_matches_dimensions original:\n{0}\nSubArray\n{1}".format(dataManager.TwoD, subArray);
        self.assertEqual( expected,result );

    def test_normalize_between_0_1(self):
        # Arrange: Create a DataMananger with loaded data and extracted subarray
        dataManager = Homework2();
        dataManager.readArrayFromFile(self.helper.aTempFile); 
        rowIndexesToExtract = [3, 5, 7, 9];
        colIndexesToExtract = [2, 4, 6, 8];
        dataManager.get_subarray(rowIndexesToExtract, colIndexesToExtract);
        # Act: Normalize extracted array
        a = 1.0;
        b = 0.0;
        dataManager.get_normalized_array(a = a, b = b);
        # Assert: All normalized values are between 0 and 1
        expected    = True;
        result      = [ True if (b <= i <= a) else False for i in np.ravel(dataManager.normalizedTwoD)];
        result      = True if (result.count(False) == 0) else False;
        print "test_normalize_between_0_1 original:\n{0}\nnormalized between 0 and 1\n{1}".format(dataManager.TwoD, dataManager.normalizedTwoD);
        self.assertEqual( expected,result );

    def test_get_ten_by_ten_mean(self):
        #Arrange:Create homework2 class object
        #Create the object
        #call the appropriate functions to get a 10x10 array
        dataManager = Homework2();
        dataManager.readArrayFromFile(self.helper.aTempFile); 
        
        #Act: get the mean of the ten_by_ten
        mean = dataManager.get_mean(dataManager.TwoD);

        #Assert: Verify the resulting mean
        expected = np.mean( np.ravel( dataManager.TwoD ) );

        if mean == expected:
            #if the expected value and the result are the same then print the mean on the screen
            print "mean is {0}".format(mean);

        self.assertEqual(mean, expected);

    def test_get_ten_by_ten_median(self):
        #Arrange:Create homework2 class object
        #Create the object
        #call the appropriate functions to get a 10x10 array
        dataManager = Homework2();
        dataManager.readArrayFromFile(self.helper.aTempFile); 

        #This function gets the array and returns the median of all elements
        #You must use the built_in function of median to do this question
        #Act: get the median of the ten_by_ten
        median = dataManager.get_ten_by_ten_median(dataManager.TwoD);

        #Assert: Verify the resulting median
        expected = np.median( np.ravel( dataManager.TwoD ) );

        if median == expected:
            #if the expected value and the result are the same then print the median on the screen
            print "median is {0}".format(median);

        self.assertEqual(median, expected);

    def test_get_ten_by_ten_standard_deviation(self):
        #Arrange:Create homework2 class object
        #Create the object
        #call the appropriate functions to get a 10x10 array
        dataManager = Homework2();
        dataManager.readArrayFromFile(self.helper.aTempFile); 
        
        #Act: get the standard deviation of the ten_by_ten
        stddev = dataManager.get_ten_by_ten_standard_deviation( np.ravel(dataManager.TwoD) );

        #Assert: Verify the resulting standard deviation
        expected = np.std( np.ravel( dataManager.TwoD ) );

        #if the expected value and the result are the same then print the standard deviation on the screen
        if stddev == expected:
            #if the expected value and the result are the same then print the median on the screen
            print "standard deviation is {0}".format(stddev);

        self.assertEqual(stddev, expected);

if __name__ == "__main__":
    #unittest.main();
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions));
    print "testing complete";
