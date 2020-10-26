Built-in Functions
------------------

**Pansy comes with some built-in functions (more on the way 😉). They are listed in alphabetical order**

.. list-table::
    :widths: 15 15 15 15 15
    :header-rows: 1

    * - 
      -
      - Built-in Functions
      -
      -
    * - `abs ( )`_
      - `append ( )`_
      - `extend ( )`_
      - `fact ( )`_
      - `frequency ( )`_
    * - `get ( )`_
      - `has_key ( )`_
      - `imports ( )`_
      - `input ( )`_
      - `is_function ( )`_
    * - `is_list ( )`_
      - `is_number ( )`_
      - `is_prime ( )`_
      - `is_string ( )`_
      - `len ( )`_
    * - `max ( )`_
      - `min ( )`_
      - `oct ( )`_
      - `pop ( )`_
      - `print ( )`_
    * - `range ( )`_
      - `run ( )`_
      - `set ( )`_
      - `slice ( )`_
      - `sort ( )`_
    * - `split_char ( )`_
      - `to_float ( )`_
      - `to_int ( )`_
      - `to_str ( )`_
      -

abs(*x*)
========
Return the absolute value of a number. The argument must be an integer or a floating point number.

.. code-block:: bash

    Pansy> abs(10)
    @ 10

.. code-block:: bash

    Pansy> abs(-5)
    @ 5

.. code-block:: bash

    Pansy> abs(7.0)
    @ 7.0

append(*list*, *object*)
========================
Returns nothing. Appends *object* to the *list*.

.. code-block:: bash

    Pansy> var l = []
    Pansy> append(list, 1)
    Pansy> print(l)
    [1]

extend(*list1*, *list2*)
========================
Returns nothing. Joins 2 *lists* together.

.. code-block:: bash

    Pansy> var list1 = [1]
    Pansy> var list2 = [2]
    Pansy> extend(list1, list2)
    Pansy> print(list1)
    [1, 2]

fact(*x*)
=========
Returns the factorial of a number. The argument must be a positive integer or zero.

.. code-block:: bash

    Pansy> var f = fact(5)
    Pansy> print(f)
    120

frequency(*string*, *c*)
========================
Returns the number of times a character *c* appears in the string *string*.

.. code-block:: bash

    Pansy> var x = frequency("ababa", "a")
    Pansy> print(x)
    3

get(*list*, *x*)
====================
Returns the element on the *list* at the index *x*. The index must be an integer that can be negative.

.. code-block:: bash

    Pansy> var l = ["apple", "banana"]
    Pansy> var first = get(l, 0)
    Pansy> var last = get(l, -1)
    Pansy> print(first)
    apple
    Pansy> print(last)
    banana

has_key(*dict*, *key*)
======================
Returns *True* if the dictionary has the key given, otherwise, returns *False*.

.. code-block:: bash

    Pansy> var d = {"name": "Andre"}
    Pansy> has_key(d, "name")
    @ True

    Pansy> has_key(d, "age")
    @ False

imports(*path*, *name*)
=======================
Returns nothing. Imports the functions and variables found on another file with the extension **.pansy**.

.. code-block:: bash

    Pansy> imports("examples/HelloWorld/code.pansy")

The functions and variables inside this file can be accessed using the following syntax:

.. code-block:: bash

    Pansy> imports("code.pansy", "module")
    Pansy> module.function()


input()
=======
Returns a string with the input given by the user.

.. code-block:: bash
    
    Pansy> var x = input()
    @ If you type "Ok"
    
    Pansy> print(x)
    Ok

is_function(*object*)
=====================
Returns *True* if the object given is a function, otherwise, returns *False*.

.. code-block:: bash

    Pansy> var x = 0
    Pansy> is_function(input)
    @ True

    Pansy> is_function(x)
    @ False

is_list(*object*)
=================
Returns *True* if the object given is a list, otherwise, returns *False*.

.. code-block:: bash

    Pansy> var x = []
    Pansy> is_function(input)
    @ False

    Pansy> is_function(x)
    @ True

is_number(*object*)
===================
Returns *True* if the object given is a number, otherwise, returns *False*.

.. code-block:: bash

    Pansy> var x = 0
    Pansy> is_function(input)
    @ False

    Pansy> is_function(x)
    @ True

is_prime(*number*)
==================
Returns *True* is the *number* given is prime, otherwise, returns *False*.

.. code-block:: bash

    Pansy> print(is_prime(10))
    @ False

    Pansy> print(is_prime(5))
    @ True

is_string(*object*)
===================
Returns *True* if the object given is a string, otherwise, returns *False*.

.. code-block:: bash

    Pansy> var x = "this is a string"
    Pansy> is_function(input)
    @ False

    Pansy> is_function(x)
    @ True

len(*list*)
===========
Return the length of the given list.

.. code-block:: bash

    Pansy> var l = [1, 2, 3, 4]
    Pansy> var x = len(l)
    Pansy> print(x)
    4

max(*number1*, *number2*)
=========================
Returns the biggest of the two numbers given.

.. code-block:: bash

    Pansy> max(10, 1)
    @ 10

    Pansy> max(2, 2)
    @ 2

min(*number1*, *number2*)
=========================
Returns the smallest of the two numbers given.

.. code-block:: bash

    Pansy> max(10, 1)
    @ 1

    Pansy> max(2, 2)
    @ 2

oct(*x*)
========
Returns the octal representation of a number *x*.

.. code-block:: bash

    Pansy> var x = oct(10)
    Pansy> print(x)
    0o12

pop(*list*, *x*)
================
Returns and removes from the *list* the element at the index *x*. The index can be a negative number.

.. code-block:: bash

    Pansy> var l = [1, 2, 3]
    Pansy> var x = pop(l, 0)
    Pansy> var m = pop(l, -1)
    Pansy> print(x)
    1
    Pansy> print(m)
    3
    Pansy> print(l)
    [2]

print(*object*)
===============
Returns nothing. Prints on the screen the representation of the *object*

.. code-block:: bash

    Pansy> print("Hello!")
    Hello!

range(*begin*, *end*)
=====================
Returns a list with numbers from *begin* until *end-1*.

.. code-block:: bash

    Pansy> var x = range(1, 10)
    Pansy> print(x)
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

run(*path*)
===========
Returns nothing. Executes a program file with the extension **.pansy**.

.. code-block:: bash

    Pansy> run("examples/HelloWorld/code.pansy")
    Hello World!

set(*struct*, *key*, *value*)
=============================
Returns nothing. The *struct* can be a *List* or a *Dictionary*. If it is a *List*, the *key* must be an integer (an *index*). If it is a *Dictionary*, 
the *key* must be a string.

.. code-block:: bash

    Pansy> var l = [1, 2, 3, 4]
    Pansy> set(l, 0, 10)
    Pansy> print(l)
    [10, 2, 3, 4]

.. code-block:: bash

    Pansy> var d = {}
    Pansy> set(d, "name", "Andre")
    Pansy> print(d)
    {"name": "Andre"}

slice(*string*, *begin*, *end*)
===============================
Returns a copy of the string given but starting at the index *begin* and ending at the index *end-1*.

.. code-block:: bash

    Pansy> var s = slice("abcdefgh", 2, 5)
    Pansy> print(s)
    cde

sort(*list*)
============
Return a new sorted list from the items in *list*. The argument *list* must contain only numbers.

.. code-block:: bash

    Pansy> var l = [1, 4, 2, 6, 10]
    Pansy> print(sort(l))
    [1, 2, 4, 6, 10]

split_char(*s*, *c*)
====================
Returns a list which the result of splitting a string *s* using a separator *c*.

.. code-block:: bash

    Pansy> var l = split_char("Hey my name is Andre Oliveira", " ")
    Pansy> print(l)
    [Hey, my, name, is, Andre, Oliveira]

to_float(*x*)
=============
Return a floating point number constructed from a number or string *x*.

.. code-block:: bash

    Pansy> print(to_float("1"))
    1.0

    Pansy> print(to_float(5))
    5.0

to_int(*x*)
=============
Return an integer constructed from a floating point number or string *x*.

.. code-block:: bash

    Pansy> print(to_int("1"))
    1

    Pansy> print(to_int(5.0))
    5

to_str(*x*)
=============
Return a string constructed from a number *x*.

.. code-block:: bash

    Pansy> print(to_str(1))
    1

    Pansy> print(to_str(5.0))
    5.0




.. _`abs ( )`: #abs-x
.. _`append ( )`: #append-l-o
.. _`extend ( )`: #extend-list1-list2
.. _`fact ( )`: #fact-x
.. _`frequency ( )`: #frequency-string-c
.. _`get ( )`: #get-list-x
.. _`has_key ( )`: #has-key-dict-key
.. _`imports ( )`: #imports-path-name
.. _`input ( )`: #input
.. _`is_function ( )`: #is-function-object
.. _`is_list ( )`: #is-list-object
.. _`is_number ( )`: #is-number-object
.. _`is_prime ( )`: #is-prime-number
.. _`is_string ( )`: #is-string-object
.. _`len ( )`: #len-list
.. _`max ( )`: #max-number1-number2
.. _`min ( )`: #min-number1-number2
.. _`oct ( )`: #oct-x
.. _`pop ( )`: #pop-list-x
.. _`print ( )`: #print-object
.. _`range ( )`: #range-begin-end
.. _`run ( )`: #run-path
.. _`set ( )`: #set-struct-key-value
.. _`slice ( )`: #slice-string-begin-end
.. _`sort ( )`: #sort-list
.. _`split_char ( )`: #split-char-s-c
.. _`to_float ( )`: #to-float-x
.. _`to_int ( )`: #to-int-x
.. _`to_str ( )`: #to-str-x
