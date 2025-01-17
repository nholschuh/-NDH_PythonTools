import numpy as np

def round_to(data_to_round,spacing,shift=0,ceil_floor=0):
    """
    % (C) Nick Holschuh - Amherst College - 2022 (Nick.Holschuh@gmail.com)
    % This function rounds a value to a given spacing / order of magnitude
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % The inputs are as follows:
    %
    %    data_to_round -- the array that you want to collapse onto the new spacing
    %    spacing -- the gap between sequential values
    %    shift -- the offset from 0 to round to
    %    ceil_floor -- -1 acts as a floor, 0 a round, 1 a floor
    % 
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % The outputs are as follows:
    %
    %    new_data -- the values of the original array, rounded to their target
    %    data_inds -- the number of steps away from the lowest value, using the given spacing
    % 
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """

    if ceil_floor == 0:
        data_inds = np.round((data_to_round-shift)/spacing).astype(int)
    elif ceil_floor == -1:
        data_inds = np.floor((data_to_round-shift)/spacing).astype(int)
    elif ceil_floor == 1:
        data_inds = np.ceil((data_to_round-shift)/spacing).astype(int)

    new_data = data_inds*spacing+shift
    
    return new_data, data_inds