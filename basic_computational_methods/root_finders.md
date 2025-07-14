# Bisection method
Requires two initial guesses **a** and **b** where the zero has to lie between **a** and **b**.

### Procedure:
1. Start with guesses a and b where you know the root will lie between them.
2. Set a point c which is the midpoint between a and b.
3. Find f(a), f(b) and f(c) respectively. Compare the signs of f(a) and f(c). If the signs are different, the root must be between
a and c, thus set b = c and continue iteratively until your required tolerance is reached and you get the root
4. Else if the signs are same, then the root must lie between c and b and thus, set a = c and proceed iteratively as before.

# Newton's method
Requires a function f(x) and its derivative f'(x)

### Procedure: 
1. Start with a guess x = a, find f(a) and f'(a). 
2. From point-slope form, find a point on the x-axis that interesects with the line passing through (a, f(a)) with slope f'(a). 
3. Let this point be x = b, thus, $b = a - \frac{f(a)}{f'(a)}$. 
4. Repeat the procedure to find another point c and eventually you get closer to the actual root

# Secant method
Requires the function f(x) and two guesses **a** and **b**, _no derivative required_.

### Procedure: 
1. Uses two-point form instead of point slope form by approximating the derivative between the two points.
2. Iteratively find $c = b - \frac{f(b)}{m}$ (or) $c = a - \frac{f(a)}{m}$

