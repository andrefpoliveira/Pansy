# Pancy

My own programming language. It's under development :wink:

Index
=====
* [Getting Started](https://github.com/andrefpoliveira/Pancy/blob/master/README.md#getting-started)
* [Features](https://github.com/andrefpoliveira/Pancy/blob/master/README.md#features)
  * [Primitive Data Types](https://github.com/andrefpoliveira/Pancy/blob/master/README.md#primitive-data-types)
  * [Operators](https://github.com/andrefpoliveira/Pancy/blob/master/README.md#operators)
  * [Comparators](https://github.com/andrefpoliveira/Pancy/blob/master/README.md#comparators)
  * [Variables](https://github.com/andrefpoliveira/Pancy/blob/master/README.md#variables)

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
Pancy> 
```

Now you can start using using my language :smile:

To close the shell program you just have to send a ```q```:
```
Pancy> exit
```

Features
==========
### Primitive Data Types
Pancy currently supports the following data type:
* ```Integer```
* ```Float```

### Operators
Pancy currently supports the following operations: ```Sum```, ```Subtraction```, ```Multiplication```, ```Division```, ```Int Division``` and ```Power```  
Respects the priority of the operators and recognizes the usage of the left and right parenteses (```(``` and ```)```)

#### Sum
```
Pancy> 5 + 3
8
```
#### Subtraction
```
Pancy> 7 - 5
2
```
#### Multiplication
```
Pancy> 1 * 3
3
```
#### Division
```
Pancy> 10 / 2
5.0
```
#### Int Division
```
Pancy> 5 // 2
2
```
#### Power
```
Pancy> 3 ^ 2
9
```
#### More complex operations
```
Pancy> 6 + 2 * 2
10

Pancy> (6 + 2) * 2
16
```

### Comparators
Pancy supports comparasions: ```Equal```, ```Not Equal```, ```Less than```, ```Greater than```, ```Less than or Equal```, ```Greater than or Equal```, ```And```, ```Or``` and ```Not```  

```True = 1``` and ```False = 0```
#### Equal
```
Pancy> 5 == 5
1
```
#### Not Equal
```
Pancy> 5 != 5
0
```
#### Less than
```
Pancy> 5 < 5
0
```
#### Greater than
```
Pancy> 5 > 2
1
```
#### Less than or Equal
```
Pancy> 5 <= 5
1
```
#### Greater than or Equal
```
Pancy> 5 >= 6
0
```
#### And
```
Pancy> 1 == 1 and 2 == 2
1
```
#### Or
```
Pancy> 1 != 1 or 2 != 2
0
```
#### Not
```
Pancy> not 1 == 1
0
```

Variables
=========
You can store values on variables following the syntax:
```
Pancy> var x = 10        # Stores 10
Pancy> var y = 5.0       # Stores 5.0
Pancy> var c = 1==1      # Stores 1
```
