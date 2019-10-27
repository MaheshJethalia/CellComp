# "Grid Search" Approach:
#       Create sine waves with unknown amp, per, shift_h and shift_v in combinatorial manner
#       and align families to minimize loss across the entire dataset - plot the best fit!

import numpy as np
from Sine_Wave_Alignments.Approach_Custom_Sine_Wave.Design_Custom_Sine_Wave_Function \
    import DesignCustomSineWave, PrepareFamilyList

file = "/Volumes/lowegrp/Data/Kristina/MDCK_WT_Pure/generation_2_families.txt"
family_list = PrepareFamilyList(file=file, how_many_gen=2)

"""
# Call the function for single sine wave with pre-defined hyperparameters:
amp, per, shift_v = 4.59, 11.75, 17.71
print ("Calculating for amp = {}, per = {}, shift_v = {}".format(amp, per, shift_v))
best_model_mse = DesignCustomSineWave(family_list=family_list, how_many_gen=3, amp=amp, per=per, shift_h=0, shift_v=shift_v,
                                      show=True, print_phase_mse=False)
print ("\nSolution:\tMean Squared Error = {}\tParameters = {}".format(best_model_mse, [amp, per, shift_v]))
"""


# Call the function for a range of parameter combinations & print top 10 best solutions!:
top_mse = [1000000 for _ in range(10)]
top_params = [[] for _ in range(10)]

combinations = 0
"""
for amp in np.linspace(4.4, 4.6, 2 + 1):
    for per in np.linspace(18.8, 19.2, 4 + 1):
        for shift_v in np.linspace(18.3, 18.7, 4 + 1):
"""
for amp in [4.55, 4.6, 4.65]:
    for per in [19.15, 19.2, 19.25]:
        for shift_v in [18.55, 18.6, 18.65]:

            combinations += 1
            print ("Calculating for amp = {}, per = {}, shift_v = {}".format(amp, per, shift_v))

            best_model_mse = DesignCustomSineWave(family_list=family_list, how_many_gen=2, amp=amp, per=per, shift_h=0, shift_v=shift_v)

            if best_model_mse < top_mse[0]:
                for i in range(8, -1, -1):      # reversed order
                    top_mse[i+1] = top_mse[i]
                    top_params[i+1] = top_params[i]
                top_mse[0] = best_model_mse
                top_params[0] = [amp, per, shift_v]


print ("Top 10 Solutions from {} combinations\n".format(combinations))
for counter, (mse, params) in enumerate(zip(top_mse, top_params)):
    print ("\tTop #{}: \tMean Squared Error = {}\tParameters = {}".format(counter + 1, mse, params))
