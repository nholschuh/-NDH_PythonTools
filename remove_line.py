def remove_line(input_axisObject,num=1,verbose=1):
    """
    % (C) Nick Holschuh - Amherst College - 2022 (Nick.Holschuh@gmail.com)
    % This function removes contours (but I don't remember why I needed this)
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % The inputs are as follows:
    %
    %      input_axisObject - axis object to remove to remove the most recent line or lines
    %
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """
    
    for i in range(num):
        try:
            input_axisObject.lines.pop(-1)
        except:
            if verbose == 1:
                print('Couldn''t remove line')
            else:
                pass