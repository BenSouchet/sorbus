# Rouge Highlighter token test - Name Exception
try:
    test = 42
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not assign integer to variable.")
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
