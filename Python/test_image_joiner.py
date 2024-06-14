import unittest
import os
from PIL import Image
from Python.image_joiner import join_images

class TestJoinImages(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a temporary directory for test images
        os.makedirs('./test_images', exist_ok=True)

        # Create some test images
        cls.image_left_path = './test_images/test_left.png'
        cls.image_right_path = './test_images/test_right.png'
        cls.image_jpg_path = './test_images/test.jpg'
        cls.image_png_path = './test_images/test.png'

        img = Image.new('RGB', (100, 100), color = 'red')
        img.save(cls.image_left_path)

        img = Image.new('RGB', (200, 100), color = 'blue')
        img.save(cls.image_right_path)

        img = Image.new('RGB', (100, 100), color = 'green')
        img.save(cls.image_jpg_path, "JPEG")

        img.save(cls.image_png_path, "PNG")

    @classmethod
    def tearDownClass(cls):
        # Clean up test images
        os.remove(cls.image_left_path)
        os.remove(cls.image_right_path)
        os.remove(cls.image_jpg_path)
        os.remove(cls.image_png_path)
        os.rmdir('./test_images')

    def test_join_images_valid(self):
        result = join_images(self.image_left_path, self.image_right_path, separation=10, border=5, background='white')
        self.assertIsInstance(result, Image.Image)
        self.assertEqual(result.size, (320, 110))  # (100+200+10+2*5, 100+2*5)

    def test_join_images_with_resizing(self):
        result = join_images(self.image_left_path, self.image_right_path, separation=10, border=5, 
                             new_width_left=50, new_height_left=50, new_width_right=50, new_height_right=50, 
                             background='black')
        self.assertIsInstance(result, Image.Image)
        self.assertEqual(result.size, (120, 60))  # (50+50+10+2*5, 50+2*5)

    def test_join_images_invalid_path(self):
        with self.assertRaises(FileNotFoundError):
            join_images('invalid_path_left.png', self.image_right_path, separation=10)
        with self.assertRaises(FileNotFoundError):
            join_images(self.image_left_path, 'invalid_path_right.png', separation=10)

    def test_join_images_invalid_format(self):
        invalid_image_path = './test_images/test.txt'
        with open(invalid_image_path, 'w') as f:
            f.write("This is not an image.")
        
        with self.assertRaises(ValueError):
            join_images(invalid_image_path, self.image_right_path, separation=10)
        
        with self.assertRaises(ValueError):
            join_images(self.image_left_path, invalid_image_path, separation=10)
        
        os.remove(invalid_image_path)

    def test_join_images_different_heights(self):
        image_tall = './test_images/test_tall.png'
        img = Image.new('RGB', (100, 200), color = 'green')
        img.save(image_tall)

        result = join_images(self.image_left_path, image_tall, separation=10, border=5, background='white')
        self.assertIsInstance(result, Image.Image)
        self.assertEqual(result.size, (220, 210))  # (100+100+10+2*5, 200+2*5)

        os.remove(image_tall)

    def test_join_images_no_border(self):
        result = join_images(self.image_left_path, self.image_right_path, separation=10, background='none')
        self.assertIsInstance(result, Image.Image)
        self.assertEqual(result.size, (310, 100))  # (100+200+10, 100)

    def test_join_images_different_formats(self):
        result = join_images(self.image_jpg_path, self.image_png_path, separation=10, border=5, background='white')
        self.assertIsInstance(result, Image.Image)
        self.assertEqual(result.size, (220, 110))  # (100+100+10+2*5, 100+2*5)

    def test_join_images_black_background(self):
        result = join_images(self.image_left_path, self.image_right_path, separation=10, border=5, background='black')
        self.assertIsInstance(result, Image.Image)
        self.assertEqual(result.size, (320, 110))  # (100+200+10+2*5, 100+2*5)

if __name__ == '__main__':
    unittest.main()


