# Write a function that takes in a string of one or more words, and returns the
# same string, but with all five or more letter words reversed (Just like the name of
# this Kata). Strings passed in will consist of only letters and spaces. Spaces will be
# included only when more than one word is present.

# Examples:

# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
# spinWords( "This is a test") => returns "This is a test"
# spinWords( "This is another test" )=> returns "This is rehtona test"

def spin_words(sentence):
    result = list()
    for word in sentence.split(" "):
        if len(word) > 4:
            word = word[::-1]
            result.append(word)
        else:
            result.append(word)
    print(' '.join(map(str, result)))
   

# spin_words("Hey fellow warriors")
# spinWords( "This is a test") => returns "This is a test"
spin_words( "or in one Just takes or letter more only string more and be will Write will words" )
