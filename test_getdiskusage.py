import unittest
import getdiskusage
class TestGetDiskUsage(unittest.TestCase):

    def test_valid_check_valid_folder_path(self):
        self.assertEqual(getdiskusage.check_valid_folder_path("/data"), True)

    def test_invalid_check_valid_folder_path(self):
        self.assertEqual(getdiskusage.check_valid_folder_path("test.py"), False)

    def test_valid_getdisksizeinfo(self):
        response=getdiskusage.getdisksizeinfo('/opt')
        self.assertEqual('files' in response, True)

    def test_invalid_getdisksizeinfo(self):
        response=getdiskusage.getdisksizeinfo('test.txt')
        self.assertEqual(response, None)

if __name__ == '__main__':
    unittest.main()