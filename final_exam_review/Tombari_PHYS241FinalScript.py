"""
SCRIPT NOT FINISHED (I emailed you about it): This script reads data from a file, fits a specified functional form to the data, and \
generates plots of the fitted curve along with select eigenvectors visualized on a \
grid of spatial points.
"""

__author__ = "Kaitlyn Tombari"

import datetime

import matplotlib.pyplot as plt
import numpy as np
from annotate_plot import annotate_plot
from calculate_bivariate_statistics import calculate_bivariate_statistics
from calculate_lowest_eigenvectors import calculate_lowest_eigenvectors
from calculate_quadratic_fit import calculate_quadratic_fit
from convert_units import convert_units
from equations_of_state import fit_eos
from generate_matrix import generate_matrix
from read_two_columns_text import read_two_columns_text


def parse_file_name(file_name):
    """Function used to extract the chemical symbol, crystal symmetry symbol, and \
    desity funcional exchange-correlation approximation acronym from a given data \
    file's name."""
    file_name_split = str.split(file_name, '-')
    chemical_symbol = file_name_split[0]
    crystal_symmetry_symbol = file_name_split[1]
    functional_exchange_correlation_approximation = file_name_split[2]
    return chemical_symbol, crystal_symmetry_symbol, \
    functional_exchange_correlation_approximation


def main():
    """Part One: Fit an Equation of State."""
    
    # Parse the file name
    file_name = 'final_exam_review/Pt.Fm-3m.GGA-PBE.volumes_energies.dat'
    chemical_symbol, crystal_symmetry_symbol, \
    functional_exchance_correlation_approximation = parse_file_name(file_name)
    
    # Read in the data into a NumPy array.
    data = read_two_columns_text(file_name)

    # Fit a quadratic polynomial to the data 
    fit_coefficients = calculate_quadratic_fit(data)

    # Pull out the statistics on the data set
    mean_y, standard_deviation_y, minimum_x_value, maximum_x_value, minimum_y_value, \
    maximum_y_value = calculate_bivariate_statistics(data)
    
    # Pass the fit quadratic coefficients and the data to the fit_eos function
    eos_fit_curve, eos_parameters = fit_eos(data[:, 0], data[:, 1], fit_coefficients, \
    eos='vinet')

    # Convert the units of the data and fit
    converted_volume = convert_units(1, 'cubic_bohr/atom', 'cubic_angstrom/atom')
    converted_energy = convert_units(1, 'rydberg/atom', 'electron_volts/atom')
    converted_bulk_modulus = convert_units(1, 'rydberg/cubic_bohr', 'gigapascals')

    # Plot the data and the fit curve
    plt.figure()
    plt.plot(converted_volume, converted_energy, 'bo', label='Data Points')
    plt.plot(converted_volume, eos_fit_curve, 'k-', label='Fit Curve')

    # Set the axes limits
    plt.xlim(min(data[0]) - 0.1 * (max(data[0]) - min(data[0])), max(data[0]) + 0.1 * \
             (max(data[0]) - min(data[0])))
    plt.ylim(min(data[1]) - 0.1 * (max(data[1]) - min(data[1])), max(data[1]) + 0.1 * \
         (max(data[1]) - min(data[1])))

    # Label the axes
    plt.xlabel('Volume (Å^3/atom)')
    plt.ylabel('Energy (eV/atom)')
    plt.title(f'{chemical_symbol} Equation of State in DFT \
    ({functional_exchance_correlation_approximation})')

    # Annotate the plot
    annotate_plot({'chemical_symbol': {'position': (0.1, 0.9)}})
    annotate_plot({'crystal_symmetry_symbol': {'position':(0.5, 0.95), 'italic':True}})
    annotate_plot({'K_0': {'text': f'K_0 = {converted_bulk_modulus:.1f} GPa', \
    'position': (0.5, 0.9)}})
    annotate_plot({'equilibrium_volume': {f'Equilibrium Volume: \
    {np.min(converted_volume):.2f} Å^3/atom': {'position': (0.5, 0.85)}}})
    annotate_plot({'E_0': {'text': f'E_0 = {converted_energy:.2f} eV/atom', \
    'position': (0.5, 0.8)}})

    # Sign and title the graph
    annotate_plot({'created_by': {'text': f'Created by Kaitlyn Tombari on \
    {datetime.datetime.now().isoformat()[:10]}', 'position': (0.1, 0.1)}})
    plt.title(f'{functional_exchance_correlation_approximation} Equation of State for \
    {chemical_symbol} in DFT {crystal_symmetry_symbol}')

    # Display or save the plot
    display_graph = True
    if display_graph:
        plt.show()
    else:
        plt.savefig('Tombari.{chemical_symbol}.{crystal_symmetry_symbol}.{functional_exchance_correlation_approximation}EquationOfState.png')

    
    """Part Two: Visualize Vectors in Space"""

    # Generate the matrix with given data
    matrix = generate_matrix(minimum_x_value, maximum_x_value,\
    potential_name='sinusodial', number_of_dimensions=130, potential_parameter=3)

    # Calculate the eigenvectors and eigenvalues of the matrix
    eigenvalues, eigenvectors = calculate_lowest_eigenvectors(matrix)

    # Generate the grid of spatial points
    grid_points = np.linspace(-10, 10, 130)

    # Plot the eigenvectors against the grid
    plt.figure()
    for i in [3, 4, 5]:
        eigenvector = eigenvectors[i]
        if np.any(eigenvector < 0):
            eigenvector *= -1
        plt.plot(grid_points, eigenvector, label=f'ψ{i+1}, E{i+1} = \
        {eigenvalues[i]:.3f} a.u.')
    plt.plot()
    plt.xlabel('x [a.u.]')
    plt.ylabel('ψ_n (x) [a.u.]')
    plt.title(f'Select Wavefunctions for a {crystal_symmetry_symbol} Potential on a \
    Spatial Grid of 130 Points')
    plt.axhline(0, color='black', linestyle='-')
    plt.legend()
    annotate_plot({'created by': {'text': f'Created by Kaitlyn Tombari on \
    {datetime.datetime.now().isoformat()}', 'position': (0.1, 0.1)}})
             
    # Display or save the plot
display_graph = True
if display_graph:
    plt.show()
else:
    plt.savefig('Tombari.{chemical_symbol}.Eigenvector130.png')


if __name__ == "__main__":
    main()
    