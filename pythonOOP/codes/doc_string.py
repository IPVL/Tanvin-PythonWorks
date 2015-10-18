#! /usr/bin/env python

__author__ = "Panthotanvir"
__license__ = "whatever"
__docformat__ = 'rst and '

# must say class name convention and function name convention
# Class names should normally use the CapWords convention. 
# Function names should be lowercase, with words separated by underscores as necessary to improve readability. 
# Use one leading underscore only for non-public methods and instance variables
class MainClass(object):
    """This docstring is for class documentation

    The first line is brief explanation. The main idea is to document
    the class and methods's arguments with 

    - Method name and its parameters 
   
    - and to provide sections such as **Example** using the double commas syntax::

          :Example:

          followed by a blank line !

      followed by a blank line

    - Finally special sections such as **See Also**, **Warnings**, **Notes**
      use the sphinx syntax (*paragraph directives*)::

          .. seealso:: blabla
          .. warnings also:: blabla
          .. note:: blabla
          .. todo:: blabla

    .. note::
        There are many other directives such as versionadded, versionchanged,
        rubric, centered, ... See the sphinx documentation for more details.

    Here below is the results of the :func:`function1` docstring.

    """

    def method_with(self, arg1, arg2, arg3):
        """This docstring is for method documentation
        returns (arg1 / arg2) + arg3

        This is a longer explanation

        Then, you need to provide optional subsection in this order (just to be
        consistent and have a uniform documentation. Nothing prevent you to
        switch the order):

          - parameters using ``:param <name>: <description>``
          - type of the parameters ``:type <name>: <description>``
          - returns using ``:returns: <description>``
          - examples (doctest)

        :Example:

        >>> import template
        >>> a = template.MainClass1()
        >>> a.function1(1,1,1)
        2

        .. note:: can be useful to emphasize
            important feature
        .. seealso:: :class:`MainClass2`
        .. warning:: arg2 must be non-zero.
        .. todo:: check that arg2 is non zero.
        """
        return arg1/arg2 + arg3




if __name__ == "__main__":
   print "Its working"
   print MainClass.__doc__
   print MainClass.method_with.__doc__