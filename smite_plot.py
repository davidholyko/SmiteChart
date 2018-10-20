import matplotlib.pyplot as plt
import numpy as np

labels=['siege', 'initiation', 'crowd_control', 'wave_clear', 'objective_damage']
markers = [0, 1, 2, 3, 4, 5]
str_markers = ["0", "1", "2", "3", "4", "5"]

def make_radar_chart(stats, attribute_labels, title, plot_markers = markers, plot_str_markers = str_markers):

    labels = np.array(attribute_labels)

    angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
    stats=np.concatenate((stats,[stats[0]]))
    angles=np.concatenate((angles,[angles[0]]))

    fig=plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, stats, 'o-', linewidth=2)
    ax.fill(angles, stats, alpha=0.25)
    ax.set_thetagrids(angles * 180/np.pi, labels)
    plt.yticks(markers)
    ax.set_title(title)
    ax.grid(True)

    plt.show()
