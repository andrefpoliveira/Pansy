# Pansy

My own programming language. It's under development :wink:

Index
=====
* [Getting Started](https://github.com/andrefpoliveira/Pansy/blob/master/README.md#getting-started)
* [Features](https://github.com/andrefpoliveira/Pansy/blob/master/README.md#features)
  * [Primitive Data Types](https://github.com/andrefpoliveira/Pansy/blob/master/README.md#primitive-data-types)
  * [Operators](https://github.com/andrefpoliveira/Pansy/blob/master/README.md#operators)
  * [Comparators](https://github.com/andrefpoliveira/Pansy/blob/master/README.md#comparators)
  * [Variables](https://github.com/andrefpoliveira/Pansy/blob/master/README.md#variables)
  * [If Statements](https://github.com/andrefpoliveira/Pansy/blob/master/README.md#if-statements)
  * [For and While Loops](https://github.com/andrefpoliveira/Pansy/blob/master/README.md#for-and-while-loops)

Getting Started
===============
To run this language you must have ```Python 3.7+``` installed.  
To check your python version, open the Command Line and type:

```
python --version
```

Clone this repository and open the Command Line inside the folder.  
Now you can start the Pansy Shell by typing the command:  

```
python shell.py
```

You should see something like the following:

```
Pansy> 
```

Now you can start using using my language :smile:

To close the shell program you just have to send a ```q```:
```
Pansy> exit
```

Features
==========
### Primitive Data Types
Pansy currently supports the following data type:
* ```Integer```
* ```Float```

### Operators
Pansy currently supports the following operations: ```Sum```, ```Subtraction```, ```Multiplication```, ```Division```, ```Int Division``` and ```Power```  
Respects the priority of the operators and recognizes the usage of the left and right parenteses (```(``` and ```)```)

#### Sum
```
Pansy> 5 + 3
8
```
#### Subtraction
```
Pansy> 7 - 5
2
```
#### Multiplication
```
Pansy> 1 * 3
3
```
#### Division
```
Pansy> 10 / 2
5.0
```
#### Int Division
```
Pansy> 5 // 2
2
```
#### Power
```
Pansy> 3 ^ 2
9
```
#### More complex operations
```
Pansy> 6 + 2 * 2
10

Pansy> (6 + 2) * 2
16
```

### Comparators
Pansy supports comparasions: ```Equal```, ```Not Equal```, ```Less than```, ```Greater than```, ```Less than or Equal```, ```Greater than or Equal```, ```And```, ```Or``` and ```Not```  

```True = 1``` and ```False = 0```
#### Equal
```
Pansy> 5 == 5
1
```
#### Not Equal
```
Pansy> 5 != 5
0
```
#### Less than
```
Pansy> 5 < 5
0
```
#### Greater than
```
Pansy> 5 > 2
1
```
#### Less than or Equal
```
Pansy> 5 <= 5
1
```
#### Greater than or Equal
```
Pansy> 5 >= 6
0
```
#### And
```
Pansy> 1 == 1 and 2 == 2
1
```
#### Or
```
Pansy> 1 != 1 or 2 != 2
0
```
#### Not
```
Pansy> not 1 == 1
0
```

Variables
=========
You can store values on variables following the syntax:
```
Pansy> var x = 10        # Stores 10
Pansy> var y = 5.0       # Stores 5.0
Pansy> var c = 1==1      # Stores 1
```

If Statements
=============
Pansy currently supports one liner ```if``` conditions:
```
Pansy> if 2 == 2 then 101
101

Pansy> if 2 == 1 then 123 else 249
249

Pansy> if 2 == 0 then 1 elif 2 == 2 then 2 else 3
2

Pansy> if 2 == 0 then 123
# Nothing prints
```

For and While Loops
===================
Pansy currently supports one liner ```for``` and ```while``` loops:

#### For
```
Pansy> var result = 1
1
Pansy> for i = 1 to 6 then var result = result * i
Pansy> result
Pansy> 120

Pansy> var result = 1
1
Pansy> for i = 5 to 0 step -1 then var result = result * i
Pansy> result
Pansy> 120
```

#### While
```
Pansy> var i = 0
Pansy> while i < 100 then var i = i + 1
Pansy> i
100
```