import unittest
import pandas as pd
import numpy as np

class TestEDA(unittest.TestCase):

    def setUp(self):
        """Set up the test data and initialize before every test"""
        # Simulated test dataset for unit tests
        data = {
            'TransactionId': ['T1', 'T2', 'T3'],
            'Amount': [100, 200, 150],
            'CustomerId': ['C1', 'C2', 'C3'],
            'Age': [30, np.nan, 25],
            'TransactionDate': ['2021-01-01', '2021-01-02', '2021-01-03']
        }
        self.df = pd.DataFrame(data)

    def test_data_loading(self):
        """Test if the data is loaded correctly"""
        # Check if the dataset is a DataFrame
        self.assertIsInstance(self.df, pd.DataFrame)
        # Check if the DataFrame has the expected number of rows and columns
        self.assertEqual(self.df.shape, (3, 5))

    def test_missing_values(self):
        """Test for missing values"""
        # Check for missing values
        missing_values = self.df.isnull().sum()
        # Assert if Age has 1 missing value
        self.assertEqual(missing_values['Age'], 1)
        # Check other columns have no missing values
        self.assertEqual(missing_values['Amount'], 0)
        self.assertEqual(missing_values['TransactionId'], 0)

    def test_numerical_columns(self):
        """Test selecting only numerical columns"""
        # Select only numerical columns
        numerical_df = self.df.select_dtypes(include=[np.number])
        # Check if only numerical columns (Amount, Age) are selected
        self.assertListEqual(list(numerical_df.columns), ['Amount', 'Age'])
        # Verify that the shape is correct (3 rows, 2 numerical columns)
        self.assertEqual(numerical_df.shape, (3, 2))

    def test_correlation_matrix(self):
        """Test correlation matrix for numerical columns"""
        numerical_df = self.df.select_dtypes(include=[np.number])
        # Calculate the correlation matrix
        corr_matrix = numerical_df.corr()
        # Check if the correlation matrix is a DataFrame
        self.assertIsInstance(corr_matrix, pd.DataFrame)
        # Correlation matrix should have 2 columns (for Amount and Age)
        self.assertEqual(corr_matrix.shape, (2, 2))
        # Ensure diagonal is 1 (self-correlation)
        np.testing.assert_array_equal(np.diag(corr_matrix.values), [1.0, 1.0])

    def test_data_types(self):
        self.assertEqual(self.df['TransactionId'].dtype, object)
        # Assert that Amount is an integer/float
        self.assertTrue(np.issubdtype(self.df['Amount'].dtype, np.number))
        # Assert that TransactionDate is an object (string) or datetime
        self.assertEqual(self.df['TransactionDate'].dtype, object)

if __name__ == '__main__':
    unittest.main()
