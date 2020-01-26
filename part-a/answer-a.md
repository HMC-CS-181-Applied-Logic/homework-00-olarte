## Part a

### Describe what the code in `z3-test.py` is doing in a paragraph or two.

 z3-test tries to see if a logical propsition can be true. We define variables by types, and z3 will attempt to find a combination of those variables that would make the propisition true. If it finds one, it will print 'sat' along with a new line giving a solution to the logical propisition. Otherwise, if z3 can't find a solution, it will print 'unsat'.