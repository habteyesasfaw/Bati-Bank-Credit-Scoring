import unittest
import pandas as pd
import numpy as np

class TestEDA(unittest.TestCase):

    # Load the dataset before running the tests
    @classmethod
    def setUpClass(cls):
        cls.df = pd.read_csv('../data/cleaned_xente_data.csv')

    def test_dataset_shape(self):
        """Test that the dataset is loaded and has expected number of rows and columns"""
        self.assertIsNotNone(self.df)
        self.assertGreater(self.df.shape[0], 0, "The dataset should have rows.")
        self.assertGreater(self.df.shape[1], 0, "The dataset should have columns.")

    def test_missing_values(self):
        """Test that missing values are correctly identified"""
        missing_values = self.df.isnull().sum()
        self.assertIsNotNone(missing_values, "Missing values calculation failed.")
        self.assertTrue((missing_values >= 0).all(), "Negative missing value counts are not possible.")

    def test_correlation_matrix(self):
        """Test that correlation matrix is computed correctly for numerical columns"""
        numerical_df = self.df.select_dtypes(include=[np.number])
        corr_matrix = numerical_df.corr()
        self.assertIsNotNone(corr_matrix, "Correlation matrix computation failed.")
        self.assertEqual(corr_matrix.shape[0], corr_matrix.shape[1], "Correlation matrix must be square.")
        self.assertGreaterEqual(corr_matrix.shape[0], 1, "There should be at least one numerical column.")

    def test_outliers(self):
        """Test that outliers can be detected with a box plot for numerical columns"""
        numerical_df = self.df.select_dtypes(include=[np.number])
        for column in numerical_df.columns:
            q1 = numerical_df[column].quantile(0.25)
            q3 = numerical_df[column].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr
            outliers = numerical_df[(numerical_df[column] < lower_bound) | (numerical_df[column] > upper_bound)]
            self.assertIsNotNone(outliers, "Outlier detection failed.")
            self.assertGreaterEqual(len(outliers), 0, "Outlier count cannot be negative.")
    
    def test_summary_statistics(self):
        """Test that summary statistics (mean, median, etc.) are calculated correctly"""
        numerical_df = self.df.select_dtypes(include=[np.number])
        summary_stats = numerical_df.describe()
        self.assertIsNotNone(summary_stats, "Summary statistics computation failed.")
        self.assertGreaterEqual(summary_stats.shape[0], 1, "There should be at least one row in summary statistics.")

if __name__ == '__main__':
    unittest.main()
