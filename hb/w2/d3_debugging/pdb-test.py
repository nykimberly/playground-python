def greet():
    print("hi")
    print("there")

def my_function():

    import pdb; pdb.set_trace()

    j = 0
    for i in range(5):
        j = j + i
        greet()

    return j 

greet()
my_function()

# Key	Command
# ?	Get help
# l	List code where I am
# p	Print this expression
# pp	Pretty print this expression
# n	Go to next line (step over)
# s	Step into function call
# r	Return from function call
# c	Continue to next breakpoint
# w	Print “frame” (where am I?)
# q	Quit debugger
