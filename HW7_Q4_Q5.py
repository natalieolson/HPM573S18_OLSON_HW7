import scipy.stats as stat

SIM_POP_SIZE = 573     # population size of simulated cohorts
TIME_STEPS = 1000        # length of simulation
ALPHA = 0.05             # significance level for calculating confidence intervals
NUM_SIM_COHORTS = 500   # number of simulated cohorts used to calculate prediction intervals

K = 400 #number of successes
n = 573 #number of trials
p = 0.5 #probability of success

# details of a clinical study estimating the mean survival time
OBS_N = 573      # number of patients involved in the study
OBS_MEAN = 10.2    # estimated mean survival time
OBS_PROP = 0.698 #observed proportion of survivorship past 5 years
OBS_HL = 1.5      # half-length
OBS_ALPHA = 0.05   # significance level
# the standard deviation of the mean survival time reported in the clinical study
# assumes that the reported confidence interval in this study is a t-confidence interval
OBS_STDEV = OBS_HL / stat.t.ppf(1 - OBS_ALPHA / 2, OBS_N-1)

# how to sample the posterior distribution of mortality probability
# minimum, maximum and the number of samples for the mortality probablity
POST_L, POST_U, POST_N = 0.05, 0.25, 1000

