# Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately
# he is not good in maths. Can you help him to find out, how many cakes he could bake
# considering his recipes?

# Write a function cakes(), which takes the recipe (object) and the available
# ingredients (also an object) and returns the maximum number of cakes Pete
# can bake (integer). For simplicity there are no units for the amounts
# (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that
# are not present in the objects, can be considered as 0.

# Examples:
# # must return 2
# cakes({flour: 500, sugar: 200, eggs: 1}, {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
# # must return 0
# cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})

def cakes(recipe, available):
    # recipe and available objects are dictionaries
    # access name of dict entry and compare with received
    possible_units = list()
    if len(recipe) > len(available):
        print("len")
        # return 0
    else:
        for key in recipe:
            if key in available:
                qtty = available[key] / recipe[key]
                if available[key] / recipe[key] < 1:
                    return 0
                else:
                    possible_units.append(qtty)

    return max(possible_units)

    # print(type(recipe))

    # print(type(available))


# # must return 2
cakes({"flour": 500, "sugar": 200, "eggs": 1}, {
      "flour": 500, "sugar": 1200, "eggs": 5, "milk": 200})
# # must return 0
# cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, {sugar: 500, flour: 2000, milk: 2000})
