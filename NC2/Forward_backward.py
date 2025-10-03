

class NewtonInterpolation:
    def__init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)
        self.table = self.forward_difference_table()



def forward_difference_table(self):
    n = self.n
    table = [[0 for i in range(n)] for j in range(n)]
    
    
    for i in range(n):
        table[i][0] = self.y[i]



    # calculate forward differences
    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = table[i+1][j-1] - table[i][j-1]
    
    return table




def print_table(x, table):
    n = len(x)
    print("Forward Difference Table:")
    for i in range(n):
        row = [f"{x[i]:<5}"]
        for j in range(n - i):
            row.append(f"{table[i][j]:<8.4f}")
        print("  ".join(row))
    print()





def newton_forward_interpolation(x, y, value):
    n = len(x)
    h = x[1] - x[0] 
    table = forward_difference_table(x, y)
    
    print_table(x, table)
    
    u = (value - x[0]) / h
    result = table[0][0]
    term = 1
    for i in range(1, n):
        term *= (u - (i-1))
        result += (term * table[0][i]) / factorial(i)
    return result

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)




x = [2, 3, 4, 5]
y = [14.5, 16.3, 17.5, 18]

val = 5   
ans = newton_forward_interpolation(x, y, val)
print(f"Interpolated value at x = {val} is {ans:.4f}")






# Newton backward interpolation
def newton_backward_interpolation(x, y, value):
    n = len(x)
    h = x[1] - x[0]   
    table = forward_difference_table(x, y)   
    
    print_table(x, table)
    
    u = (value - x[-1]) / h  
    result = table[n-1][0]   
    term = 1
    
    for i in range(1, n):
        term *= (u + (i-1))   
        result += (term * table[n-i-1][i]) / factorial(i)
    return result



x = [24,28,32,36,40]
y = [28.06 ,30.19 ,32.75 ,34.94 ,40]

val = 33  
ans = newton_backward_interpolation(x, y, val)
print(f"Backward Interpolated value at x = {val} is {ans:.4f}")
