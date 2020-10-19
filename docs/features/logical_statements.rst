Conditionals and Loops
----------------------

The if statement
================

.. code-block:: bash

  var food = "pizza"
  if food == "pizza":
    print("Yammi!")
  end

The if else statement
=====================

.. code-block:: bash

  var food = "sushi"
  if food == "hamburguer":
    print("Tasty!")
  else:
    print("Meeeh")
  end

Chained conditionals
====================

.. code-block:: bash

    var x = 0
    if x < 0:
      print("You need more!")
    elif x > 0:
      print("You need less!")
    else:
      print("Correct!")
    end

Nested conditionals
===================

.. code-block:: bash

  var x = 1
  if x < 0:
    if x < 10:
      print("It is a positive single digit.")
    end
  end


For Loops
=========

The **for loop** will iterate from one number to another or a list. It will go one by one by default, but you can specify the jump value.

- **For Loop with Step 1**

.. code-block:: bash

    for i=0 to 10:
      print(i)
    end

**or**

.. code-block:: bash

    for i in range(0, 10):
      print(i)
    end

- **For Loop with Step 2**

.. code-block:: bash

    for i=0 to 10 step 2:
      print(i)
    end

- **For Loop over a List**

.. code-block:: bash

    for i in ['Iron Man', 'Spiderman', 'Black Widow']:
      print(i)
    end

While Loop
==========

The while loop will loop while the condition is met.

.. code-block:: bash

    var x = 0
    while x < 10:
      print(i)
      var i = i + 1
    end
