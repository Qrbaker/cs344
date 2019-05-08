% Lab 12 , part 2

% ###A.i###

%bread = bread
% unifies, since by the first definition of unity in chapter 2, two
% constants unify if they are the same atom or number.

%’Bread’  =  bread"
% does NOT unify, since even though prolog does not consider single
% quotes in evaluating atoms, Bread (with a capital B) is not the same
% atom as bread (lowercase b).

%food(X)  =  food(bread)
% unifies, because according to the third definition of unity, complex
% terms unify if the have the same functor [food()] and airty [/1].
% Then, by definition *2*, the variable X will be instantiated to the
% atom, so the only variable instantiation will be compatible.

%food(bread,X)  =  food(Y,sausage)
% unifies. X will be instantiated to sausage, and Y will be instantiated
% to bread. Then, by definition *3*, food(bread,sausage) can unified
% with food(sausage,bread).

%meal(food(bread),X)  =  meal(X,drink(beer))
% This is a doozy, but in the end does not unify. This is because X will
% be instantiated to drink(beer) to attempt to satisfy the unification,
% but then the second complex term will be
% meal(drink(beer),drink(beer)), which fails definition 3 for unity.

% (Although, I know a few people that might try to argue two beers is
% a meal...)

% ###A.ii###

% KB from the text:
%house_elf(dobby).
%witch(hermione).
%witch('McGonagall').
%witch(rita_skeeter).
%magic(X):-  house_elf(X).
%magic(X):-  wizard(X).
%magic(X):-  witch(X).

%magic(house_elf)
% This is not satisfied, because house_elf does not directly associate
% or unify with wizard(X) or witch(X).

%wizard(harry)
% This is not satisfied because harry is never associated with any
% complex term, nor unified with any variable.

%magic(wizard)
% wizard in this instance is seen as an atom rather than a complex term,
% so magic(wizard) will try to find house_elf(wizard), wizard(wizard),
% or witch(wizard) and fail.

%magic('McGonagall')
% this is actually NOT satisfied, because of the fact that prolog will
% run through the list of modus ponens for magic and fail at wizard(X)
% which is not defined.

%magic(Hermione)
% This query is satisfied, but not how one would expect. Prolog
% understands terms with capital letters to be variables, and therefore
% interprets the query magic(Hermione) as "Who is magic?" and returns
% 'dobby'. Using the ";" operator will dutifully return the rest of the
% defined magical people, hermione, 'McGonagall', and rita_skeeter.
% Here is a rough search tree:
%
%  ?- magic(Hermione)
%  Hermione = _G1
%  ?- house_elf(_G1);wizard(_G1);witch(_G1)
%  _G1 = dobby ->
%        house_elf(dobby) ->
%        magic(dobby) -> TRUE
%
% Using ";" will then just internally ask prolog to set _G1 to the next
% atom it knows, hermione, and so on...


% These issues can be fixed. First, we should use the OR chaining
% property, or use different variables for each definition of magic().

house_elf(dobby).
witch(hermione).
witch('McGonagall').
witch(rita_skeeter).

magic(X):-  house_elf(X); wizard(X); witch(X).

% Then, we should initialize wizard() with some term, or remove it.

wizard(harry).

% Finally, we just need to structure our queries with the understanding
% of how prolog determines what variables are, and use quotes, so ask
% magic('Hermione').

% ###B###
% Prolog relies on unification as the primary tool for inference.
% By unifiying values, prolog methodically eleminates statements until
% the query is satisfied, or it cannot find a series of unifications to
% equal the query.
%
% Per https://athena.ecs.csus.edu/~logicp/unification-resolution.html:
% Prolog uses resolution within horn clauses to help infer ultimate
% queries. Here's a basic example:

a:- b.
c:- b, x, y.

% The process of resolution converts c to "c:- a, x, y".





