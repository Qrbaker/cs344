% Lab 12
% Author: Quentin Baker

% ###A.i###
killer(Butch).
married(Mia,Marsellus).
dead(Zed).
kills(Marsellus,X) :- footMassage(X,Mia).
loves(Mia,X) :- goodDancer(X).
eats(Jules,X) :- nutritious(X) ; tasty(X).

% The first 3 statements are definitions, which are fairly
% straightforward.
%
% The fourth statement is the first instance of *modus
% ponens*; it essentially equates to "Marsellus kills X, given X gives
% Mia a foot massage.
%
% The fifth statement means Mia loves X, given X is a good dancer.
%
% The last statement is a combined modus ponens, stating Jules eats X,
% given X is nutritious, or X is tasty.

% ###A.ii###

wizard(ron).
hasWand(harry).
quidditchPlayer(harry).
wizard(X):-  hasBroom(X),  hasWand(X).
hasBroom(X):-  quidditchPlayer(X).

% 1. wizard(ron). will evaluate as true/yes, because the KB has the
% definition wizard(ron).
%
% 2. witch(ron). will evaluate as false/no, because there is no witch()
% definition, and prolog will always infer non-existant definitions to
% be false.
%
% 3. wizard(hermione). will be false/no because there is no definition
% in the KB that has hermione as a constant.
%
% 4. witch(hermione). will be false/no because there is no witch()
% definition (same as 2).
%
% 5. wizard(harry). will be true/yes, because prolog will evaluate the
% fourth statement, and find that harry has a wand, and additionally
% harry has a broom, because harry is a quidditch player.
%
% 6. wizard(Y). will return Y=ron, and with a ";" will then return
% Y=harry. Any additional semi-colon queries will return false/no.
%
% 7. witch(Y). will return false/no, because there is no witch()
% definition.

% ###B###
% Prolog implements a shortened version of the modus ponens, not in true
% prepositional form. Normally, the full statement in english is "P
% implies Q. P is true, therefore Q must be true." Prolog essentially
% takes this as an axiom, and therefore just lays out "Q, given P."
%
% Using prolog, one possible implementation would be:

true(Y) :- implies(X,Y), true(X).

% You can then define X and Y. If you include true(X) and implies(X,Y)
% in the KB, then Y will be true. Otherwise, it will be false. Below is
% one example:

implies(sunny,sunscreen).
implies(raining,jacket).
true(raining).

% Note that true(jacket) will be true, and true(umbrella) will not be.
% Additionally, true(sunscreen) will be false, because true(sunny) was
% not in the KB.

% ###C###
% Horn clauses are basically the fundamental building blocks of prolog.
% It allows something to be proven through a clause of association with
% only a single "positive literal". In fact, the full definition of the
% modus ponens in B is itself a horn clause!
%
% Horn clauses are themselves valid propositional logic, just a
% well-known case. They are so useful because the result of a horn
% clause itself a horn clause, meaning they can be chained -- this is
% the main power behind prolog; a truth can be inferred from a series of
% definitions this way.

% ###D###
% Prolog has syntatic equivalents to TELL and ASK. You do the equivalent
% of TELL by placing a definition in a knowledge base [e.g.
% wizard(harry)], and the equivalent of ASK by using a statement
% containing a variable, such as wizard(X).
