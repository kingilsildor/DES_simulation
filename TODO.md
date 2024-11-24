Queuing theory tells us that for FIFO scheduling the average waiting times are shorter for an
M/M/n queue and a system load ρ and processor capacity μ than for a single M/M/1 queue
with the same load characteristics (and thus an n-fold lower arrival rate). Of course, ρ must be
less than one, but the experiment only becomes interesting when ρ is not much less than one.

# Steps
1. Prove that a M/M/n has a shorter waiting time than a M/M/1 queue.
    1. Do this for $n=1$.
    2. $n=2$.
    3. $n$ in a generic case.
2. Test this using code by writing a DES program.
    1. Test the statistical significance.
3. Compare it with another type of job sceduling (smallest job priority).
4. Do if for different values of X where X is a service time distribution (i.e. M/X/n or M/X/1).
5. Write a report about it.
