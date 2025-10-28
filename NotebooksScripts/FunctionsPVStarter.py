"""
Functions, Classes and Modules Tutorial
This file demonstrates Python functions.

Learning objectives:
- Defining and using functions

Complete the script by filling in the missing code sections marked with <---.

@author: Sara Hajjar 
"""

# Import any necessary libraries
import math
# import pandas as pd
# import numpy as np
# import os

# <--- Define a function to size a PV system based on building dimensions and panel specifications
def calculate_pv_size(building_length, building_width, roof_angle, panel_width, panel_height, panel_power): # <--- include parameters for building length, width, roof angle, panel width, panel height and panel power
    """
    This is a docstring. Use it to describe the function's purpose, parameters, and return values.
    """
    """
    building_length in meters = 30
    building_width in meters = 16
    roof_angle in degrees = 22

    panel_width in mm = 1690
    panel_height in mm = 1046
    panel_power in Wp = 400
    """

    num_panels_length = (building_length) / (panel_width / 1000)  # <--- calculate number of panels that fit along the length of the building
    num_panels_width = (building_width) / (panel_width / 1000)  # <--- calculate number of panels that fit along the width of the building
    num_panels = math.floor(num_panels_length) * math.floor(num_panels_width)  # <--- calculate total number of panels (use math.floor to round down to nearest whole number)
    pv_capacity_kw = (num_panels * panel_power) / 1000  #
    
    return pv_capacity_kw, num_panels # <--- return the total PV capacity in kW and number of panels

if __name__ == "__main__":
    # =============================================================================
    # This section is a common way to incorporate code that you want to run if the 
    # script is executed directly, but will be ignored if the script is 
    # imported as a module into another. 
    # 
    # It separates the executable part of the script from the part that defines
    # reusable components e.g. functions.
    # 
    # This is useful way of testing the code or providing examples of how to 
    # use the code.
    # =============================================================================
    
    pv_capacity_kw, num_panels = calculate_pv_size(30, 8, 22, 1690, 1046, 400)# <--- call the calculate_pv_size function with appropriate arguments

    print(pv_capacity_kw, num_panels) # <--- Add a print statement to display the number of PV panels and the total PV capacity in kW
