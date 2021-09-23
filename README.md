# DNARepBreak
DNA replication breakage

Run digestion.py and load in maRTA data.
Data is loaded in from no treatment as original and digested/treatment as treatment data.
Next use the Set up files button to assign the corresponding DNA pattern to measurement label.
Finally, use manual digest to choose parameters for one digestion type or use find best to automatically parse data.

Run runsim.py to create simulated maRTA data and store as dataframes for each pattern type. 
Will automatically generate based on available parameter (length of total, number of replisomes, min speed, max speed, time in label 1, time in label 2, starting timeframe, label 1 speed(%), label 2 speed(%))
