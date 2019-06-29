import unittest
from src.locations import dict_location
from src.calc_location import get_distance

class test_calc_location(unittest.TestCase):
    def test_get_distance(self):
        given = get_distance(36, 125, -587, dict_location['location_a'])
        self.assertEqual(754.8708498809581, given, 'fail test_get_sqrt_144')



if __name__ == '__main__':
    unittest.main()
