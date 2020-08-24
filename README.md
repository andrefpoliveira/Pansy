# Pancy

My own programming language. It's under development :wink:

Index
=====
* [Getting Started](https://github.com/andrefpoliveira/Pancy/blob/master/README.md#getting-started)
* [Features](https://github.com/andrefpoliveira/Pancy/blob/master/README.md#features)
  * [Primitive Data Types](https://github.com/andrefpoliveira/Pancy/blob/master/README.md#primitive-data-types)
  * [Operators](https://github.com/andrefpoliveira/Pancy/blob/master/README.md#operators)

Getting Started
===============
To run this language you must have ```Python 3.7+``` installed.  
To check your python version, open the Command Line and type:

```
python --version
```

Clone this repository and open the Command Line inside the folder.  
Now you can start the Pancy Shell by typing the command:  

```
python shell.py
```

You should see something like the following:

```
Pancy > 
```

Now you can start using using my language :smile:

To close the shell program you just have to send a ```q```:
```
Pancy > q
```

Features
==========
### Primitive Data Types
Pancy currently supports the following data type:
* ```Integer```
* ```Float```
### Operators
Pancy currently supports the following operations: ```Sum```, ```Subtraction```, ```Multiplication```, ```Division``` and ```Power```  
Respects the priority of the operators and recognizes the usage of the left and right parenteses (```(``` and ```)```)
#### Sum
```
Pancy > 5 + 3
8
```
#### Subtraction
```
Pancy > 7 - 5
2
```
#### Multiplication
```
Pancy > 1 * 3
3
```
#### Division
```
Pancy > 10 / 2
5.0
```
#### Power
```
Pancy > 3 ^ 2
9
```
#### More complex operations
```
Pancy > 6 + 2 * 2
10

Pancy > (6 + 2) * 2
16
```
