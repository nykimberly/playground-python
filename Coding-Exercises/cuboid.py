#Let's learn about list comprehensions! You are given three integers X, Y and Z representing the dimensions of a cuboid along with an integer n. You have to print a list of all possible coordinates given by i, j, k on a 3D grid where the sum of i, j, k is not equal to n. 

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    
lst = [[i, j, k] 
       for i in range(0, x+1) 
       for j in range(0, y+1) 
       for k in range(0, z+1) 
       if i+j+k != n]
print(lst)