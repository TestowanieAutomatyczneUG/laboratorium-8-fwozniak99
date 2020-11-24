import requests

class Meals:
    def getRandomMeal(self):
        meal = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
        return meal.json()['meals']

    def getMealByName(self, name):
        if type(name) != str:
            raise Exception('Name is not a string')
        meal = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?', {'s': name})
        return meal.json()['meals']

    def getMealByFirstLetter(self, firstLetter):
        if type(firstLetter) != str or len(firstLetter) != 1:
            raise Exception('Not a single letter')
        meal = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?', {'f': firstLetter})
        return meal.json()['meals']

    def getMealById(self, id):
        if type(id) != int:
            raise Exception('Not an integer')
        meal = requests.get('https://www.themealdb.com/api/json/v1/1/lookup.php?', {'i': id})
        return meal.json()['meals']

    def listAllCategories(self):
        meal = requests.get('https://www.themealdb.com/api/json/v1/1/list.php?c=list')
        return meal.json()['meals']

    def listAllIngredients(self):
        meal = requests.get('https://www.themealdb.com/api/json/v1/1/list.php?i=list')
        return meal.json()['meals']

    def filterByMainIngredient(self, ingredient):
        if type(ingredient) != str:
            raise Exception('Ingredient is not a string')
        meal = requests.get('https://www.themealdb.com/api/json/v1/1/filter.php?', {"c": ingredient})
        return meal.json()['meals']


a = Meals()
print(len(a.getMealByName("spaghetti")))