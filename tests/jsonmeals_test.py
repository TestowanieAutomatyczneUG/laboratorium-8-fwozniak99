import unittest
from src.sample.jsonmeals import Meals


class TestMeals(unittest.TestCase):
    def setUp(self):
        self.temp = Meals()

    def test_getRandomMeal(self):
        self.assertEqual(type(self.temp.getRandomMeal()), list)

    def test_getMealByName(self):
        self.assertEqual(self.temp.getMealByName('spaghetti')[0]['strMeal'], 'Spaghetti Bolognese')

    def test_getMealById(self):
        self.assertEqual(self.temp.getMealById(52772)[0]['strArea'], 'Japanese')

    def test_getMealByFirstLetter(self):
        self.assertEqual(self.temp.getMealByFirstLetter('K')[0]['strCategory'], 'Lamb')

    def test_listAllCategories(self):
        categories = [{'strCategory': 'Beef'}, {'strCategory': 'Breakfast'}, {'strCategory': 'Chicken'},
                      {'strCategory': 'Dessert'}, {'strCategory': 'Goat'}, {'strCategory': 'Lamb'},
                      {'strCategory': 'Miscellaneous'}, {'strCategory': 'Pasta'}, {'strCategory': 'Pork'},
                      {'strCategory': 'Seafood'}, {'strCategory': 'Side'}, {'strCategory': 'Starter'},
                      {'strCategory': 'Vegan'}, {'strCategory': 'Vegetarian'}]
        self.assertEqual(self.temp.listAllCategories(), categories)

    def test_listAllIngredients(self):
        chicken = {'idIngredient': '1', 'strIngredient': 'Chicken', 'strDescription': 'The chicken is a type of domesticated fowl, a subspecies of the red junglefowl (Gallus gallus). It is one of the most common and widespread domestic animals, with a total population of more than 19 billion as of 2011. There are more chickens in the world than any other bird or domesticated fowl. Humans keep chickens primarily as a source of food (consuming both their meat and eggs) and, less commonly, as pets. Originally raised for cockfighting or for special ceremonies, chickens were not kept for food until the Hellenistic period (4th–2nd centuries BC).\r\n\r\nGenetic studies have pointed to multiple maternal origins in South Asia, Southeast Asia, and East Asia, but with the clade found in the Americas, Europe, the Middle East and Africa originating in the Indian subcontinent. From ancient India, the domesticated chicken spread to Lydia in western Asia Minor, and to Greece by the 5th century BC. Fowl had been known in Egypt since the mid-15th century BC, with the "bird that gives birth every day" having come to Egypt from the land between Syria and Shinar, Babylonia, according to the annals of Thutmose III.', 'strType': None}
        self.assertEqual(self.temp.listAllIngredients()[0], chicken)

    def test_filterByMainIngredient(self):
        self.assertEqual(self.temp.filterByMainIngredient('Chicken')[0]['strMeal'], 'Brown Stew Chicken')

    def test_getMealByIdNone(self):
        self.assertEqual(self.temp.getMealById(1), None)

    def test_getMealByNameLen(self):
        self.assertEqual(len(self.temp.getMealByName('spaghetti')), 2)

    def test_getMealByNameException(self):
        with self.assertRaises(Exception):
            self.temp.getMealByName(444)

    def test_getMealByFirstLetterException(self):
        with self.assertRaises(Exception):
            self.temp.getMealByFirstLetter('abc')

    def test_getMealByIdException(self):
        with self.assertRaises(Exception):
            self.temp.getMealById(False)

    def test_filterByMainIngredientException(self):
        with self.assertRaises(Exception):
            self.temp.filterByMainIngredient(333)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
