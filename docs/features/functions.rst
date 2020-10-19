Functions
---------

A function is a block of code that is only executed when it is called.
You can pass data into a function and a function can return data aswell.

Function definition
===================

.. code-block:: bash

    func double(n) {
        var n = n * 2
        return n
    }

Calling a function
==================

.. code-block:: bash

    Pansy> double(5)
    @ 10

Arguments
=========

You can pass information inside a function.
Taking the function **double** presented before:

.. code-block:: bash

    Pansy> double(2)
    @ 4

    Pansy> double(4)
    @ 8

You can also define **optional** arguments:

.. code-block:: bash

    func hey(firstName, age=18) {
        print("Hey! I'm " + firstName + " and I'm " + to_str(age) + " years old!")
    }

*firstName* is a mandatory argument. However, age isn't. This means that you don't need to pass a value for it. It will have a predefined value.
There are two ways of calling this function:

.. code-block:: bash

    Pansy> hey("John")
    Hey! I'm John and I'm 18 years old!

    Pansy> hey("John", age=35)
    Hey! I'm John and I'm 35 years old!