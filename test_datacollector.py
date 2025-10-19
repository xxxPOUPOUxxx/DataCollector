# test_datacollector.py
"""
Tests for DataCollector module.
"""

import unittest
from datacollector import DataCollector

class TestDataCollector(unittest.TestCase):
    """Test cases for DataCollector class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DataCollector()
        self.assertIsInstance(instance, DataCollector)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DataCollector()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
