def solution(a):
    import numpy as np  

    mean_holder = [np.array(i).mean() for i in a]

    mean_groups= [[i for i,x in enumerate(mean_holder) if x==v] for v in mean_holder]

    mean_g = []

    for i in mean_groups:

        if i not in mean_g:

            mean_g.append(i)

        # print(mean_holder)

    return mean_g