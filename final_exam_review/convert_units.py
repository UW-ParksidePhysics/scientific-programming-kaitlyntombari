"""
Convert data from one unit to another.
"""

__author__ = "Kaitlyn Tombari"


def convert_units(value, from_units, to_units):
    """
    Function used to convert data from one unit to another.
    Parameters:
        value (float): The value to be converted.
        from_units (str): The units of the value to be converted from.
        to_units (str): The units to convert the value to.
    Returns:
        float: The converted value.
    """
    # Define the conversion factors
    conversion_factors = {
      'cubic_bohr/atom': 0.14818471147216278, # cubib bohr per atom to cubic angstroms \
      # per atom
      'rydberg/atom': 13.605693122994, # rydberg per atom to electron volts per atom
      'rydberg/cubic_bohr': 14710.507848260711, # rydberg per cubic bohr to gigapascals
      'cubic_angstrom/atom': 1.0, # cubic angstroms per atom to cubic bohr per atom
      'electron_volts/atom': 1.0, # electron volts per atom to rydberg per atom'
      'gigapascals': 1.0 # gigapascals to rydberg per cubic bohr
    }
    
    # Convert the units
    converted_value =  value * conversion_factors[from_units] / conversion_factors\
    [to_units]
    
    return converted_value


if __name__ == "__main__":
    print("1 cubic bohr per atom equals", convert_units(1, 'cubic_bohr/atom', \
    'cubic_angstrom/atom'), "cubic angstroms per atom")
    print("1 rydberg per atom equals", convert_units(1, 'rydberg/atom',\
    'electron_volts/atom'), "electron volts per atom")
    print("1 rydberg per cubic bohr equals", \
    convert_units(1, 'rydberg/cubic_bohr', 'gigapascals'), "gigapascals")
    
