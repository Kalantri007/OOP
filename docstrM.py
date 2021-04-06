class docstr:
    """
     class for operations on numbers.

    """
    def __init__(self, i):
        return None

    def add(self, num):
        """
        The function to add two Numbers.

        """
        return None


print(docstr.__doc__)  # Class docstring
print ("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
docstr.__init__.__doc__ ="""
        The constructor for Number class.
        This all will show up there
        """

print(docstr.__init__.__doc__)