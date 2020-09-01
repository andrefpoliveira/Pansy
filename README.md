# Pansy
My own programming language, currently under development

How to start
============
You need to have ```Python 3.6+``` installed. If you haven't, go to [Python](https://www.python.org/downloads/) and install the latest version.

Once you have Python setup, you need to clone this repository and open a terminal inside the folder. Then you must type:
```
C:\Users\...\Pansy > python shell.py
```

You should see:
```
Pansy> 
```

You can exit anytime using the command:
```
Pansy> exit
```
Now you are ready to start! :smile:

Features
========
#### Assigning variables
```var x = <value>```

#### Comments
```@ This a one line comment```

#### Data types
Currently there are 4 data types: ```Integer```, ```Float```, ```String``` and ```List```.

##### Integer
```var x = 1```

##### Float
```Pansy> var x = 5.0```

##### String
```var x = "This is a string"```

##### List
```var x = [1,2,3]```

#### If Statements
```
var x = 0
if x < 0:
  print("You need more!")
elif x > 0:
  print("You need less!")
else:
  print("Correct!")
```

#### For Loops
```
for i=0 to 10:
  print(i)
end
```

```
for i=0 to 10 step 2:
  print(i)
end
```

#### While Loop
```
var x = 0
while x < 10:
  print(i)
  var i = i + 1
end
```

#### Functions
```
func double(n) {
  var n = n * 2
  return n
}
```

Pansy comes with some built-in functions (more on the way :wink:):
* ```print(arg)``` - Prints ```arg``` on the screen
* ```input()``` - Waits for the input of the user
* ```is_number(arg)``` - Returns 1 (True) if ```arg``` is a number or 0 (False) if not
* ```is_string(arg)``` - Returns 1 (True) if ```arg``` is a string or 0 (False) if not
* ```is_list(arg)``` - Returns 1 (True) if ```arg``` is a list or 0 (False) if not
* ```is_function(arg)``` - Returns 1 (True) if ```arg``` is a function or 0 (False) if not
* ```append(arg1, arg2)``` - Appends ```arg2``` to the list ```arg1```
* ```pop(arg1, arg2)``` - Pops the element at the index ```arg2``` of the list ```arg1```
* ```extend(arg1, arg2)``` - Joins to lists together
* ```get(arg1, arg2)``` - Gets the element at the index ```arg2``` of the list ```arg1```
* ```run(arg)``` - Runs a program from a file with the extension ```.pansy```
* ```len(arg)``` - Returns the length of the string ```arg```
* ```to_str(arg)``` - Transforms ```arg``` to a string if possible
* ```to_int(arg)``` - Transforms ```arg``` to a integer if possible
* ```to_float(arg)``` - Transforms ```arg``` to a float if possible
