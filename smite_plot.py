import matplotlib.pyplot as plt
import numpy as np

labels=['Siege', 'Initiation', 'Crowd Control', 'Wave Clear', 'Objective Damage']
markers = [0, 1, 2, 3, 4, 5]

def make_radar_chart(name, stats, labels = labels, plot_markers = markers):

    labels = np.array(labels)

    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
    stats = np.concatenate((stats,[stats[0]]))
    angles = np.concatenate((angles,[angles[0]]))

    fig= plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, stats, 'o-', linewidth=2)
    ax.fill(angles, stats, alpha=0.25)
    ax.set_thetagrids(angles * 180/np.pi, labels)
    plt.yticks(plot_markers)
    ax.set_title(name)
    ax.grid(True)

    fig.savefig("static/images/%s.png" % name)


#
# make_radar_chart("Agni", [2,3,4,4,5])
