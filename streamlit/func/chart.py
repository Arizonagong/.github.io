import matplotlib as map
import numpy as np
import matplotlib.pyplot as plt
from func.model import sample_dist_cal

def sample_dist_chart(n,num,sample,sample_mean_stack,sample_mean_print_pre,n_bins):
    # X axis value for the sample dist
    x1=sample
    # X axis value for the sampling dist
    x2=sample_mean_stack
    x3=sample_mean_print_pre
    
    # Plotting
    fig, ax = plt.subplots(3, 1, figsize=(14, 7), sharex=True)
        ## Plot 1. One Tail Testing: Lower Tail
    ax[0].hist(x1, n_bins, histtype='bar', stacked=True, rwidth=0.9, color="red")
    ax[0].set_ylim(0, n*0.5)
    ax[0].set_xlim(40000,65000)
    ax[0].axvline(x = x2[len(x2)-1], color = 'b')
    ax[0].text(x2[len(x2)-1],n*0.1/2,f'{x2[len(x2)-1]}',rotation=90)
        ## Plot 2.
        ## In order to highlight the newly added value: create one plot with previous values, create another with new values
    ax[1].hist(x2,
            n_bins, 
            histtype='barstacked', 
            stacked=True, 
            rwidth=0.9,
            color="red")
    ax[1].hist(x3,
            n_bins, 
            histtype='barstacked', 
            stacked=True, 
            rwidth=0.9,
            color="blue")
    ax[1].set_ylim(0, num*0.25)
    ax[1].axvline(x = sum(x2)/len(x2), color = 'r')
    ax[1].text(sum(x2)/len(x2),n*0.1, f'{sum(x2)/len(x2)}',rotation=90, color='w')
    return x1, x2, fig