MarkovMonster
==============

MarkovMonster is a small library I wrote to understand
using Markov chains to generate text. Should you use it? 
Probably not, but you're welcome to.

Here's an example of how you might::
 
 import MarkovMonster as mm
 
 corpus = 'a_file_full_of.txt'

 # Convert file into an array of words. Optional second
 # argument specifies text encoding and defaults to utf-8
 array_of_words = mm.eat(corpus, 'utf-8')

 # Convert the array to a generator that returns tuples of 
 # the length specified in the second argument. If omitted,
 # the default length value is 3.
 one_step_closer = mm.chew(array_of_words, 3)

 # Returns a dictionary with a key length that is one less
 # than the length of the tuples fed in
 chained_text = mm.digest(one_step_closer)

 # Generate a string of the length in words specified in the 
 # second argument. If omitted, the default length is 20 words.
 mm.vomit(chained_text, 40)

Or::
 
 import MarkovMonster as mm
 
 corpus = 'a_file_full_of.txt'
 
 mm.vomit(mm.digest(mm.chew(mm.eat(corpus), 3)), 100)

