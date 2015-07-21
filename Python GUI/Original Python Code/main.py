"""
Kathryn DiPippo
6/16/2015
main.py
- The main function with a commented structure to make this easy to understand
- While each function is clearly commented, this one is outlined to make the process of
   gathering and calculating data easily readable
"""

def main(): #{
	[out,dev,wave] = LaserPlusLIF(name, conc, total_runs, final_num_of_runs)#;	Generate the Data Set
	remove_outliers(final_num_of_runs)#;		Modify data set to remove outliers
#}

# =====================================================================================================================
# Main function execution. This will be placed at the bottom of the file.
if __name__ == "__main__": #{
    main()#;
#}


'''
Personal notes for self:
- the program starts with LaserPlusLIF
	- this calls the Zurich_asynch_SINGLE function, which gathers data
		- this calls run_example, which executes functions for the thing
			- it also calls plot_data which plots the data simultaneously
	- the data is returned as a list
- now remove outliers can be performed on the list
'''