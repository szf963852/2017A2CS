even(N) :- 0 is mod(N,2).
odd(N) :- not(even(N)).

factorial(1,1).
factorial(N,F):-
	M is N - 1,
	factorial(M,X),
	F is N*X.

bunnyEars(0,0).
bunnyEars(N,F):-
	M is N - 1,
	bunnyEars(M,X),
	F is X+2.


fibonacci(0,0).
fibonacci(1,1).
fibonacci(N,F):-
	M is N - 1,
	fibonacci(M,X),
	L is N - 2,
	fibonacci(L,Y),
	F is X+Y.

bunnyEars(0,0).
bunnyEars(N,F):-
	M is N - 1,
	bunnyEars(M,X),
	A is M mod 2,
	F is X+2+A.

triangle(0,0).
triangle(1,1).
triangle(X,Y):-
	Z is X-1,
	triangle(Z,T),
	Y is T+X.

sumdigits(0,0).
sumdigits(X,Y):-
	Z is X//10,
	sumdigits(Z,S),
	L is X mod 10,
	Y is S+L.

count7(0,0).
count7(X,Y):-
	Z is X//10,
	B is X mod 10,
	count7(Z,S),
	Y is S+B//7-B//8.