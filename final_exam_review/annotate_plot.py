"""Annotate a plot using Pyplot's text function.

__Kaitlyn Tombari__
"""

from datetime import datetime

import matplotlib.pyplot as plt


def annotate_plot(annotations: dict):
    """Function used to create and annotate a plot."""
    for label, annotation_info in annotations.items():
        position = annotation_info['position']
        alignment = annotation_info['alignment']
        fontsize = annotation_info['fontsize']
        plt.text(position[0], position[1], label, fontsize=fontsize,
                 ha=alignment[0], va=alignment[1])


if __name__ == "__main__":
    today_date = datetime.now().isoformat()[:10]
    first_name = "Kaitlyn"
    last_name = "Tombari"
    annotation_text = f'Created by {first_name} {last_name} {today_date}.'
    annotations = {
        annotation_text: {
            "position": (0.05, 0.05),
            "alignment": ['left', 'bottom'],
            "fontsize": 10
        }
    }
    annotate_plot(annotations)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Sample Plot")
    plt.show()
