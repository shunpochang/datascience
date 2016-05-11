# Get success count needed, limited trials remaining, and success rate.
min_success = x;
total_trial = y;
success_rate = p;
chance_occurrence = 0;
# Binomial probabilities to hit the at least the mininum need of success.
for (i = min_success: total_trial) 
    {chance_occurrence += dbinom(i, total_trial, success_rate);}
chance_occurrence
