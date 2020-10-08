Quickstart
----------
**This document is still a work in progress**

1. Install Python 3.6+.
=======================
Pansy needs Python to run properly. If you don't have python installed then
go to `Python`_ and install the latest version.
Once you have Python setup, you need to clone this repository and open a terminal inside the folder.
Then you must type:


.. code-block:: bash

    C:\Users\...\Pansy > python shell.py


- You should see: 

    ``Pansy>``

You can exit anytime using the command:

.. code-block:: bash

    exit

Now you are ready to start! :smile:

2. How to run Pansy file ?
==========================
Let's imagine you want to run the code that is in the dir: ``examples/HelloWorld/code.pansy``
You just need to use the command:

.. code-block:: bash

    run("examples/HelloWorld/code.pansy")

3. Features
===========
- Assigning variables

.. code-block:: bash

    var x = <value>

- Comments

.. code-block:: bash

    @ This a one line comment

**Data types**

.. note::

    Currently there are 4 data types:

        - Integer
        - Float
        - String
        - List

- **Integer**

.. code-block:: bash

    var x = 1


- **Float**

.. code-block:: bash

    var x = 5.0


- **String**

.. code-block:: bash

    var x = "This is a string"


- **List**

.. code-block:: bash

    var x = [1,2,3]


- **Operations**

::

    Sum (+)
    Subtraction (-)
    Multiplication (*)
    Division (/)
    Int Division (//)
    Remainder (%)

- **Comparators**

::

    Equal (==)
    Inequal (!=)
    Greater than (>)
    Less than (<)
    Greater than or Equal to (>=)
    Less than or Equal to (<=)


.. _`Python`: https://www.python.org/downloads/