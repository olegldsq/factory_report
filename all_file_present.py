import unittest
import pathlib as pl

class TestCase(unittest.TestCase):
    def test_f1(self):
        path = pl.Path("workers_list.txt")
        self.assertTrue(path.is_file())
        self.assertTrue(path.parent.is_dir())

    def test_f2(self):
        path = pl.Path("roles_list.txt")
        self.assertTrue(path.is_file())
        self.assertTrue(path.parent.is_dir())

    def test_f3(self):
        path = pl.Path("monthly_report.txt")
        self.assertTrue(path.is_file())
        self.assertTrue(path.parent.is_dir())