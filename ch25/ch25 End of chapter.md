

> ##chapter 25
> ###Godfrey Shang Option 1
> ###End of chapter question
> #### question 1
> #####(a) iteration only repeat some codes over and over again but recursion means the subroutine calls itself to break the problem down.
> #####(b) adv: the code will be shorter as we only need to consider the unit problem.  dis: use a lot addresses
> ####question 2
> #####(a) a definition includes itself.
> #####(b)
Call number|Procedure call|Exponent = 0|Result
---|---|---|---
1|Power(2,4)|*False*|2*Power(2,3)
2|Power(2,3)|*False*|2*Power(2,2)
3|Power(2,2)|*False*|2*Power(2,1)
4|Power(2,1)|*False*|2*Power(2,0)
5|Power(2,0)|*True*|1
(4)|Power(2,1)|*False*|2*1
(3)|Power(2,2)|*False*|2*2
(2)|Power(2,3)|*False*|4*2
(1)|Power(2,4)|*False*|8*2
>#####(c)
>
>#####(e)
```pseudocode
FUNCTION Power(Base : INTEGER, Exponent : INTEGER) RETURNS INTEGER
Result = 1
WHILE Exponent > 0
	Result = Result * Base
	Exponent = Exponent - 1 
ENDWHILE
RETURN Result
ENDFUNCTION
```
>#####(f)(i) use less addresses
>#####(f)(ii) write less codes
> ####question 3
> #####(a)(i) 4th line is base case
> #####(a)(ii) 6th line is general case

>####**3(b)**
Call Variable | Procedure call | (n=1) or (n=0)| Result 
--- | --- | --- | --- | ---
1 | Fibonacci(4) | False | Fibonacci(3) + Fibonacci(2) |  
2 | Fibonacci(3) | False | Fibonacci(2) + Fibonacci(1) |  
3 | Fibonacci(2) | False | Fibonacci(1)+Fibonacci(0£© |  
4 | Fibonacci(1) | True | 1 | 
5 | Fibonacci(0) | True | 1 | 
4 | Fibonacci(1) | True | 1 | 
(3)|   |   | 2 |
(2)|||3
7 | Fibonacci(2) | False | Fibonacci(1) |  
8 | Fibonacci(1) | True | 1 |
9 | Fibonacci(0) | True | 1 |
(7) |  |  | 2 | 
(1)|||5
