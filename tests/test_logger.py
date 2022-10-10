import logging
import unittest  

import sys,os

sys.path.insert(0, '../scripts/')
sys.path.append(os.path.abspath(os.path.join('scripts')))

from log_helper import AppLog


class TestCases(unittest.TestCase):
    def test_logging(self):
        with self.assertLogs() as captured:
            AppLog.get_app_logger()
        self.assertEqual(len(captured.records), 1) 
        self.assertEqual(captured.records[0].getMessage(), "Hello, World!") 