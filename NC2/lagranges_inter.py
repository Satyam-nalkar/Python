def lagrange_interpolation(x, y, value):
    n = len(x)
    result = 0.0
    
    # Lagrange interpolation formula
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (value - x[j]) / (x[i] - x[j])
        result += term
    
    return result




x = [5, 6, 9, 11]
y = [12,13,14,16]

val = 10
ans = lagrange_interpolation(x, y, val)
print(f"Interpolated value at x = {val} is {ans:.4f}")
