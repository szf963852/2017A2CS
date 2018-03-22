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
	F is X+2.