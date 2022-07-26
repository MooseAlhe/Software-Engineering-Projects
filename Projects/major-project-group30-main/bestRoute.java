import java.util.ArrayList;
import java.util.List;

public class bestRoute 
{
	
     public static void main(String args[])
     {
         //change matrix to whatever desired. Origin is S which is starting point and all other chars that are not 1 are destination points
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
        int[][] distance = distMatrix(matrix);

        minRoute(distance);

            
    }
    static void minRoute(int[][] matrix) //take distance matrix as an input
    {
        int sum = 0;
        int counter = 0;
        int j = 0, i = 0;
        int min = Integer.MAX_VALUE;
        List<Integer> list = new ArrayList<>();
 
        list.add(0);
        int[] route = new int[matrix.length];
        //this loop traverses through the matrix to see the min distance to the next point, and so on
        while (i < matrix.length && j < matrix[i].length) 
        {
 
            if (counter >= matrix[i].length - 1) 
            {
                break;
            }
 
            if (j != i && !(list.contains(j))) 
            {
                if (matrix[i][j] < min) 
                {
                    min = matrix[i][j];
                    route[counter] = j + 1;
                }
            }
            j++;
 
            if (j == matrix[i].length) 
            {
                sum += min;
                min = Integer.MAX_VALUE;
                list.add(route[counter] - 1);
                j = 0;
                i = route[counter] - 1;
                counter++;
            }

        }
 
        System.out.print("Minimum Cost is : ");
        System.out.println(sum);
    }
    static int[][] distMatrix(char[][] matrix)
    {
        int counter = 0;
        ArrayList<Node> coord = new ArrayList<Node>();
        //This nested loop will traverse the enitre matrix and find destination points, and put them in an array list of coordinates
        for (int i = 0; i < matrix.length; i++)
        {
            for (int j = 0; j < matrix[i].length; j++)
            {
                if (matrix[i][j] != '1')
                {
                    coord.add(new Node(j,i));
                    counter++;
                }
                    
            }
        }

        int[][] distance = new int[counter][counter];
        //this nested loop will take the coordinates, and calculate all the possible distances between them and create a new matrix 
        //with all the possible distanced from each point 
        for(int i = 0; i < coord.size(); i++)
        {
            Node n1 = coord.get(i);
            for (int j = 0; j < coord.size(); j++)
            {
                Node n2 = coord.get(j);
                distance[i][j] = Math.abs(n1.x - n2.x) + Math.abs(n1.y - n2.y);
                System.out.print(distance[i][j] + "   ");
            }             
            System.out.println();
        }
        return distance; 
    }
}
class Node 
{
    int x;
    int y;
    
    Node(int x, int y) 
    {
        this.x = x;
        this.y = y;
    }
}
