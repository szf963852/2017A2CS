capitalCity(paris).
capitalCity(berlin).
capitalCity(cairo).

father(F, C) :- 
	male(F), parent(F, C).

ancestor(A, B) :- 
	parent(A, B).

ancestor(A, B) :- 
	parent(A, X), ancestor(X, B).

writeList ([]).
writeList([HiTJ) :-write (H), nl, writeList (T). 