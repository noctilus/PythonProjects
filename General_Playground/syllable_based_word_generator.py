# Import the random module
import random

# Import the enchant module for checking the dictionary
import enchant
d = enchant.Dict("en_US")

# Define the list of common syllables in English
syllables = ["a", "ab", "ac", "ad", "af", "ag", "al", 
             "am", "an", "ap", "ar", "as", "at", "av", "ax", "az",
             "ba", "be", "bi", "bl", "bo", "br", "bu",
             "ca", "ce", "ch", "ci", "cl", "co", "cr", "cu",
             "da", "de", "di", "do", "dr", "du",
             "ea", "eb", "ec", "ed", "ef", "eg", "el", 
             "em", "en", "ep", "er", "es", "et",
             "fa", "fe", "fi", "fl", "fo","ga", "ge" ,
             "gi", "gl", "go", "gr", "gu","ha", "he", "hi", "ho", "hu",
             "ia", "ib", "ic", "id", "ie", "if", "ig", 
             "il", "im", "in", "ip", "ir", "is", "it","ja", "je", 
             "ji", "jo","ka", "ke", "ki", "ko","la", "le", "li", "lo",
             "ma", "me", "mi", "mo","na", "ne", "ni", "no",
              "oa", "ob", "oc", "od" , "oe", "of", 
              "og", "ol", "om", "on", "op", "or", "os", 
              "ot","pa", "pe", "pi", "pl", "po",
              "ra", "re", "ri", "ro","sa", "se", "si", "sk", "sl", "sm", 
              "sn", "so", "sp", "st","ta", "te", "ti", "to",
              "ua", "ub", "uc", "ud" , "ue", "uf", 
              "ug", "ul", "um", "un", "up", "ur", "us", "ut",
              "va", "ve", "vi", "vo", "wa", "we", "wi", "wo","ya", "ye", "yi", "yo",
              "za", "ze", "zi", "zo","ing", "er","i", "y",
              "ter","al","ed","es","e","tion","re","o","oth","ry","de","ver",
              "ex","en","di","bout","com","ple","u","con","per","un","der","tle",
              "ber","ty","num","peo","ble","af","ers","mer","wa","ment","pro",
              "ar","ma","ri","sen","ture","fer","dif",
              "pa","tions","ther","fore","est",
              "fa","la","ei","not","si","ent","ven","ev",
              "ac","ca","fol","ful","na","tain","ning","col",
              "par","dis","ern","ny","cit","po","cal",
              "mu","moth","pic","im","coun","mon","pe",
              "lar","por","fi","bers","sec","ap","stud",
              "ad","tween","gan","bod","tence","ward",
              "hap","nev","ure","mem","ters","cov","ger","nit"]

# Define a function to generate a random name
def generate_name():
  # Initialize an empty name
  name = ""
  # Choose a random length between 2 and 4 syllables
  length = random.randint(7, 8)
  # Loop until the name reaches the desired length
  while len(name) < length:
    # Choose a random syllable from the list
    syllable = random.choice(syllables)
    # Capitalize the first syllable
    if name == "":
      syllable = syllable.capitalize()
    # Add a hyphen between syllables
    
    name += syllable
  # Return the name
  return name

# Generate a random name that does not exist in the dictionary
n=0
name = generate_name()
while d.check(name) or n < 30:
  name = generate_name()
  n+=1
  print(name)