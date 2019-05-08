% Lab 12, section 3

% From the script, this is the gist of Bedevere's reasoning:
% 1. Witches burn.
% 2. Wood also burns.
% 3. Wood floats.
% 4. Ducks also float.
% 5. If something weighs as much as a duck, it will float.
%
% Generalizing the fifth point, if two things weight the same, and one
% of them floats, then they are made of wood.

witch(X):- burns(X).

burns(X):- wooden(X).

wooden(X):- floats(X).

floats(duck).

floats(X):- weighsTheSame(X,Y),floats(Y).

weighsTheSame(suspect,duck).

% If you evaluate witch(suspect), prolog will return true.

% Note that the following is NOT considered for if a suspect is a witch:
scalesAreFair(false).
