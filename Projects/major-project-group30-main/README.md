# Group 30 Major Project
Please read this file in order to understand our code, as well as how to operate it
## Sprint 1 Code

###### Description
The code for sprint was written in Java. Generally for the code we made we does not have any inputs. Since our code uses a matrix, we wanted to make it 
more convenient rather than having to put in a whole 10 x 10 matrix as an input. We allow the user to edit the matrix in the code to whatever they want. 

This is what the matrix in the code looks like:

```
char[][] matrix = 
        {
	    {'S', '1', '1', '1', '1', '1', '1', '1', '1', '1'},
	    {'1', '1', '1', '1', 'F', '1', '1', '1', '1', '1'},
	    {'1', '1', '1', '1', '1', '1', '1', 'K', '1', '1'},
            {'1', '1', 'E', '1', '1', '1', '1', '1', '1', '1'},
            {'1', '1', '1', '1', '1', '1', '1', '1', '1', '1'},
            {'1', 'F', '1', '1', 'D', '1', '1', '1', '1', '1'},
            {'1', '1', '1', '1', '1', '1', '1', '1', '1', '1'},
            {'1', '1', '1', '1', '1', '1', 'X', '1', '1', '1'},
            {'1', 'Y', '1', '1', '1', '1', '1', '1', '1', '1'},
            {'1', '1', '1', '1', '1', '1', '1', '1', 'Y', '1'}
	    };
```

The matrix can be editted in anyway including size, as well as components. The point 'S' is the starting point and all other points that are not '1' 
are destination points. This matrix would be inputted into another method called distanceMatrix() which will calulate a another matrix that will calculate
all combinations of distances between each point. the matrix calculated from the above matrix is as follows: 

```
0   5   9   5   6   9   13  9   17   
5   0   4   4   7   4   8   10  12   
9   4   0   6   9   6   6   12  8   
5   4   6   0   3   4   8   6   12   
6   7   9   3   0   3   7   3   11   
9   4   6   4   3   0   4   6   8   
13  8   6   8   7   4   0   6   4   
9   10  12  6   3   6   6   0   8   
17  12  8   12  11  8   4   8   0  

```

The above matrix would represent every combination of distances from and to each point. 
Row 1 shows the distance from S to all the other destinations, and Row 2 does the same for the second destination point and so on. 

This matrix will then be inputted into a method called minRoute() which will traverse this matrix and find the shortest distance, and add all of them up. And this will give you the shortest distance to reach all the routes. 

The output of this is as follows:

```
Minimum Cost is : 37
```
So in the original matrix, you would be able to reach all of the destination points in at least 37 moves. The condition to this is that you can only move up down left or right. 

To run the code simply alter the matrix to what you want, and run it normally on the terminal.

## Sprint 2 Code

###### Description 

