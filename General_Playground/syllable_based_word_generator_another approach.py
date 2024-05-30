import random

# Lists of syllables to create alien-like names
syllables = [
    "zor", "gla", "vex", "quar", "plor", "thex", "dril", "snor", "krox", "ypt",
    "slith", "fryn", "flor", "glip", "snik", "tork", "kwor", "xyl", "shor", "thun",
    "blip", "clon", "krel", "splor", "skra", "gron", "plix", "thrum", "blor", "snex"]

# Generate random alien names
num_names = 5  # Change this to generate a different number of names
random_names = set()

while len(random_names) < num_names:
    name = ''.join(random.sample(syllables, random.randint(2, 3)))
    random_names.add(name)

# Print the generated alien names
for name in random_names:
    print(name)