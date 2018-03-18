male(john).
male(jack).
male(bill).

female(mary).
female(kris).
female(elisabeth).

parent(bill, mary).
parent(kris, bill).
parent(kris, mary).



/*  Rule  */

brother(X,Y) :-
	male(X),
	parent(Z,X),
	parent(Z,Y).


sister(X,Y) :-
	female(X),
	parent(Z,X),
	parent(Z,Y).


son(X,Y) :-
	male(X),
	parent(X,Y).

daughter(X,Y) :-
	female(X),
	parent(X,Y).

married(X,Y):-
	parent(X,Z),
	parent(Y,Z).

ancestor(X,Y):-
	parent(X,Z),
	
	
	