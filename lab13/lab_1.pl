%Exercise 13, Part 1
%Author: Quentin Baker

% ###A.i###
directlyIn(katarina, olga).
directlyIn(olga, natasha).
directlyIn(natasha, irina).

in(X,Y) :- directlyIn(X,Y); directlyIn(X,C), in(C,Y).

% ###A.ii###
tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).

listtran([],[]).
listtran([G|A],[E|B]):- tran(G,E), listtran(A,B).

% Uses the Head|Tail functionality of the "|". Recursively translates
% the list tails until empty, in which case the base statement [],[]
% is evaluated.

% ###B###
% Sure, just use the modus ponens statement with values, then state the
% truth of one by declaring it.

mortal :- human.

human.
% Now, if you evaluate ?- mortal. you will get "true".


