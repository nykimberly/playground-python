import os
import sys
import user
import builtins as b

# change to correct directory
os.chdir(os.path.join(os.environ['HB'], 'd1_project-organization'))

# create fake input handler
def fake_input(prompt):
    sys.stdout.write(prompt)
    v = _inputs.pop(0)
    print(v)
    return v

b.input = fake_input

_inputs = ["Kimberly", "Kimby"]

user.greet_user()
user.greet_user()
