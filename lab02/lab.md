*note: This document is formatted in markdown syntax. If you want it to look nice, try using a markdown reader :D*

# Lab 02 Responses #
Written by: Quentin Baker

## Exercise 2.1 ##
1.	Both local search algorithms solve the problem
2.	Both algorithms finish at essentially the same time
3.	The starting position does not matter in this instance, as there are no local maxima for an algorithm to get “stuck”
    at.
4.	The step value in this case could cause an algorithm to “overshoot” if very large, or produce a number with some
    small floating-point errors if very small.
5.  exp_schedule() defines the "annealing Schedule" that affects how likely the search is to "jump" to another possible
    location, a likelihood that decreases over time.

## Exercise 2.2 ##
1.  With the sine function, the Hill-climbing solution fails to find the correct solution, while Simulated annealing
    sometimes works. This is because the sine function generates lots of local maxima, or "peaks" that the hill-climbing
    alogorithm is going to get stuck on unless it happens to be on the correct hill at the beginning. If the annealing
    schedule is set with good parameters, then annealing can find the maximum.
2.  Yes! If the starting value places the algorithms on the biggest "hill", they will both succeed.
3.  The delta affects the Simulated annealing, but generally not hill-climbing. This again falls back to the underlying
    algorithms; simulated annealing will jump farther distances with bigger deltas. This may help it, but can also
    hinder it if the delta is too large.
4.  Simulated annealing, while not always entirely right, nearly always gets closer than Hill-climbing, or at least
    matches it.

## Exercise 2.3 ##
1.  Both algorithms perform better, but Simulated annealing is now nearly-perfect (tested with 10 restarts). This is
    because with restarts, simulated annealing more likely to jump to the "correct" hill in a given run. Hill-climbing
    still has the issue of always getting stuck on whatever "hill" it starts on, but with enough restarts will have a
    decent chance of getting the right result.
2.  Averages:
        - Hill-climbing:        15.8
        - Simulated Annealing:  20.6
3.  As seen by the averages, Simulated Annealing is in general getting closer to the correct answer overall. This means
    that it will likely be more successful with a smaller amount of restarts compared to Hill-climbing and will not need
    to cover as much of the search space.

## Exercise 2.4 ##
1.  I think beam search makes the most sense for simulated annealing, as it will have multiple random jumps to choose
    the best from, instead of just one binary "is this random option better?" choice. This is essentially an
    implementation of ["stochastic beam search"](https://en.wikipedia.org/wiki/Beam_search#Variants)
2.  I feel this question is highly variable and depended upon factors such as available memory, storage, and processor
    speed. You could maintain a *very* large number of solutions given average space and time constraints today.
3.  I would change the position of my for() loop in the Random-restart simulated annealing search to occur at the point
    where the algorithm decides to jump or not, and calculate the value of *n* number of jumps. I would then select the
    best value that is greater than my current value. If no values chosen are greater, I wouldn't jump at all.
