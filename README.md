# DNARepBreak
DNA replication breakage

Simulated DNA replication fault breakage from maRTA data.
Sample data is provided in Sample Data folder, with a no treatment measurement, S1 buffer measurement, and S1 buffer + s1 digest measurement.
Additionally, additional sample data can be generated via the runsim.py script, which will generate appropriately formatted data from simulations with inputted parameteres.
Adjustable parameters are the 
1. Number of repeated runs to combine data from
2. Total tract length to simulate replication
3. Number of replisomes
4. Minimum and maximum speed of replisomes
5. Amount of time in which first and second DNA labels are present
6. Timeframe in which replisomes can be generated
7. Speed modifiers for each label type
8. How long to run each time simulation (recommended >= timeframe of replisome initialization)

Run digestion.py and load in maRTA data.
Data should be formatted in Type/Segments(1+)/Total length(if >1 segment)
Data is loaded in from no treatment as original and digested/treatment as treatment data.
Next use the Set up files button to assign the corresponding DNA pattern to measurement label.
Finally, use manual digest to choose parameters for one digestion type or use find best to automatically parse data.
