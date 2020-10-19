Quickstart
----------
**This document is still a work in progress**

Install Python 3.6+.
====================
Pansy needs Python to run properly. If you don't have python installed then
go to `Python`_ and install the latest version.
Once you have Python setup, you need to clone this repository and open a terminal inside the folder.
Then you must type:


.. code-block:: bash

    C:\Users\...\Pansy> python shell.py


- You should see: 

    ``Pansy>``

You can exit anytime using the command:

.. code-block:: bash

    exit

Now you are ready to start! 😀

How to run a Pansy file ?
=========================
Let's imagine you want to run the code that is in the directory: ``examples/HelloWorld/code.pansy``. 
You just need to use the command:

.. code-block:: bash

    Pansy> run("examples/HelloWorld/code.pansy")

You can also execute your code from outside the Pansy shell:

.. code-block:: bash

    C:\Users\...\Pansy> pansy.py examples/HelloWorld/code.pansy

Data types
==========

.. note::

    Currently there are 4 data types:

        - **Integer**
        - **Float**
        - **String**
        - **List**
        - **Dictionaries**

Assigning variables
===================

.. code-block:: bash

    var x = <value>

- **Integer**

.. code-block:: bash

    var i = 1


- **Float**

.. code-block:: bash

    var f = 5.0


- **String**

.. code-block:: bash

    var s = "This is a string"


- **List**

.. code-block:: bash

    var lst = [1,2,3]

- **Dictionaries**

.. code-block:: bash

    var dict = {"key": value}

Comments
========

.. code-block:: bash

    @ This is a one line comment

    @/ This is a
       multiple line comment /@

Number Operations
=================

- **Sum**

.. code-block:: bash

    Pansy> 5 + 2
    @ 7

- **Subtraction**

.. code-block:: bash

    Pansy> 5 - 2
    @ 3

- **Multiplication**

.. code-block:: bash

    Pansy> 5 * 2
    @ 10

- **Division**

.. code-block:: bash

    Pansy> 5 / 2
    @ 2.5

- **Int Division**

.. code-block:: bash

    Pansy> 5 // 2
    @ 2

- **Remainder**

.. code-block:: bash

    Pansy> 5 % 2
    @ 1

- **Power**

.. code-block:: bash

    Pansy> 5 ^ 2
    @ 25

Comparisons
===========

There are 6 comparisons operators in Pansy. They all have the same priority (which is higher than that of the `Boolean operations`_).

.. list-table::
    :widths: 15 15
    :header-rows: 1

    * - Operation
      - Meeting
    * - ==
      - Equal
    * - !=
      - Not equal
    * - <
      - Strictly less than
    * - >
      - Strictly greater than
    * - <=
      - Less than or equal
    * - >=
      - Greater than or equal

Boolean operators
=================
All the boolean operators have the same priority.

.. list-table::
    :widths: 15 15
    :header-rows: 1

    * - Operation
      - Result
    * - x or y
      - *if x is false, then y, else x*
    * - x and y
      - *if x is false, then x, else y*
    * - not x
      - *if x is False, then True, else False*


.. _`Python`: https://www.python.org/downloads/
.. _`Boolean operations`: #boolean-operators