"""
a rewriting of the zen of python
by jack allan
"""
# ......................................................... Imports
import pyttsx3
import time
# ......................................................... Function
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[7].id)
rate = engine.getProperty("rate")
# engine.setProperty("rate", rate - 10)
    
def doc_title():
    t = "python yang: a rewriting of the zen of python, by jack allan"
    print(t.title())
    print()

def python_yang():
    t = doc_title()
    p_y_statements = ["ugly is as captivating as beautiful",
                      "if explicitness is impassable, be implicit",
                      "complex is details to a big picture simplicity",
                      "complicated is a simple misexecution of complexity",
                      "nested has dimension, dimensionality is alluring",
                      "density means more to explore (or be overwhelmed by)",
                      "readability does count, but don't sacrifice on potency",
                      "special cases update the rules",
                      "default practicality sounds purely corporate",
                      "errors are proof that you're trying something new",
                      "amplify the errors and filter",
                      "an educated guess is one step removed from ambiguity",
                      "if there were only one way to do it, nothing would be done; but do it the way that yields the most progress and excitement",
                      "now is better than never, unless now is globally destructive",
                      "if the implementation is hard to explain, ask yourself: am i familiar enough with the implementation to be in the position to explain?",
                      "good ideas can be difficult to explain, especially new implementations...have patience.",
                      "a name is a type of idea too"]
    for count, statement in enumerate(p_y_statements):
        print("{}\t{}".format(f'{count:02d}', statement.upper()))
        engine.say("Python Yang Doctrine Number {}...\t{}".format(count, statement.upper()))
        engine.runAndWait()
# ......................................................... On run, Export, Import       
if __name__ == "__main__":
    python_yang()
