"""

"""

__author__ = "Kaitlyn Tombari"

import matplotlib.pyplot as plt
import numpy as np
import datetime

from read_two_columns_text import read_two_columns_text
from calculate_bivariate_statistics import calculate_bivariate_statistics
from calculate_quadratic_fit import calculate_quadratic_fit
from equations_of_state import fit_eos
from convert_units import convert_units
from annotate_plot import annotate_plot
from generate_matrix import generate_matrix


def parse_file_name():
  