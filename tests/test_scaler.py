import unittest
import numpy as np
import sys
import os

# Test dosyası scaler klasörünü bulabilsin diye sys.path ayarı yapıyoruz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scaler.standard_scaler import MyStandardScaler

class TestMyStandardScaler(unittest.TestCase):
    """
    MyStandardScaler sınıfını test etmek için birim testler.
    """

    def setUp(self):
        """
        Her testten önce çalışacak.
        Yeni bir MyStandardScaler nesnesi oluşturuyoruz.
        """
        self.scaler = MyStandardScaler()

    def test_fit(self):
        """
        fit() metodunun doğru şekilde ortalama ve standart sapma hesaplayıp hesaplamadığını test eder.
        """
        X = np.array([[1], [2], [3]])
        self.scaler.fit(X)

        expected_mean = np.array([2.0])
        expected_std = np.array([0.81649658])  # doğru standart sapma

        # Normal assertEqual yerine array karşılaştırması yapıyoruz
        np.testing.assert_array_almost_equal(self.scaler.mean_, expected_mean, decimal=5)
        np.testing.assert_array_almost_equal(self.scaler.std_, expected_std, decimal=5)

    def test_transform(self):
        """
        transform() metodunun veriyi doğru şekilde standardize ettiğini test eder.
        """
        X = np.array([[1], [2], [3]])
        self.scaler.fit(X)
        scaled_data = self.scaler.transform(X)

        expected_scaled = np.array([[-1.22474487], [0.0], [1.22474487]])

        np.testing.assert_array_almost_equal(scaled_data, expected_scaled, decimal=5)

    def test_fit_transform(self):
        """
        fit_transform() metodunun fit ve transform işlemlerini doğru şekilde birleştirip birleştirmediğini test eder.
        """
        X = np.array([[1], [2], [3]])
        scaled_data = self.scaler.fit_transform(X)

        expected_scaled = np.array([[-1.22474487], [0.0], [1.22474487]])

        np.testing.assert_array_almost_equal(scaled_data, expected_scaled, decimal=5)

if __name__ == '__main__':
    unittest.main()
