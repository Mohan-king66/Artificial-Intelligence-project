% Base case: The sum of integers from 1 to 0 is 0
sum_upto(0, 0).

% Recursive case: Sum for N > 0
sum_upto(N, Sum) :-
    N > 0,
    N1 is N - 1,
    sum_upto(N1, Sum1),
    Sum is Sum1 + N.

