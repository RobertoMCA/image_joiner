import unittest
import os
from rpy2 import robjects
from rpy2.robjects.packages import importr
from rpy2.robjects import r

class TestRImageJoiner(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a temporary directory for test images
        os.makedirs('./test_images', exist_ok=True)

        # Create some test images
        image_left_path = './test_images/test_left.png'
        image_right_path = './test_images/test_right.png'

        img = r('magick::image_blank(100, 100, "red")')
        r('magick::image_write')(img, path=image_left_path)

        img = r('magick::image_blank(100, 100, "blue")')
        r('magick::image_write')(img, path=image_right_path)

    @classmethod
    def tearDownClass(cls):
        # Clean up test images
        os.remove('./test_images/test_left.png')
        os.remove('./test_images/test_right.png')
        os.rmdir('./test_images')

    def test_join_images(self):
        r('source("R/image_joiner.R")')
        result = r('join_images("./test_images/test_left.png", "./test_images/test_right.png", separation=10, border=5, background="white")')
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
