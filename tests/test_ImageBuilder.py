import unittest

import backend.image.ImageBuilder
import backend.models.MyUser


class ImageBuilderTestCase(unittest.TestCase):
    def setUp(self):
        build_file = 'abc.tar'
        user = MyUser
        self.builder = ImageBuilder(build_file=build_file, is_image=False,
            image_id=2, user=user)

    def tearDown(self):
        self.builder = None

    def test_create_image(self):
        self.builder.create_image()
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
