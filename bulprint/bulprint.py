r'''
bulprint
this is print (with time)
easier to print with time
it's just a project for 'main.py'
in __init__: use in file python (.py)
in __main__: use in terminal/cmd (or file .sh/.cmd/.bat)
'''
import __init__, __main__
path = {
    'init': __init__.__file__,
    'main': __main__.__file__,
    'bulprint': __file__,
    'id': id((__init__.__file__, __main__.__file__, __file__))
}
docstr = {
    'init': __init__.__doc__,
    'main': __main__.__doc__,
    'bulprint': __doc__,
    'id': id((__init__.__doc__, __main__.__doc__, __doc__))
}
with open(__file__) as f:
    fr = f.read()
with open(__init__.__file__) as f:
    fri = f.read()
with open(__main__.__file__) as f:
    frm = f.read()
code = {
    'init': fri,
    'main': frm,
    'bulprint': fr,
    'id': id((fri, frm, fr))
}
cache = {
'init': [int(str(id(str(__init__) + __init__.__file__ + fri + __init__.__doc__ + str(dir(__init__)))), 36)],
'main': [int(str(id(str(__main__) + __main__.__file__ + frm + __main__.__doc__ + str(dir(__main__)))), 36)],
'bulprint': [int(str(id(__name__ + __file__ + fr + __doc__ + str(dir(__builtins__)))), 36)],
'id': id(([int(str(id(str(__init__) + __init__.__file__ + fri + __init__.__doc__ + str(dir(__init__)))), 36)], [int(str(id(str(__main__) + __main__.__file__ + frm + __main__.__doc__ + str(dir(__main__)))), 36)], [int(str(id(__name__ + __file__ + fr + __doc__ + str(dir(__builtins__)))), 36)]))
}
del fri
del frm
del fr
del __main__
del __init__
try:
    del f
except NameError:
    pass