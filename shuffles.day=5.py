def shuffle(l1,l2):

    # Find the shorter list and save it's size
    if len(l1) < len(l2):
        minlength = len(l1)
    else:
        minlength = len(l2)
    
    # create empty list to use it later
    shuffled = []

    # Loop over both lists until the final entry
    # for the smaller one is reached
    for i in range(minlength):
        # In the loop, add the entry from list one on the current position 
        # to shuffled
        shuffled.append(l1[i])
        # Then, do the same with list two
        shuffled.append(l2[i])

