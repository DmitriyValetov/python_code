import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patches as mpatches
import random
import numpy as np

def scatter_with_legend(data):
    data.sort(key=lambda x: x[2])
    n_groups = set([dote[2] for dote in data])

    # global style
    mpl.style.use('ggplot') # equal to mpl.style.use('seaborn')
    
    # style of text should be defined before any texting
    # affect all except x-ylabels and title
    # only sticks style 
    # mpl.rc('xtick', labelsize=8)
    # mpl.rc('ytick', labelsize=8)
    # global text style
    font = {'family' : 'normal',
            'weight' : 'bold',
            'size' : 8
            }
    plt.rc('font', **font)


    colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(n_groups))]
    legends = []
    legended_colors = set()

    # margins for axis
    x = [dote[0] for dote in data]
    x_min = min(x)
    x_max = max(x)
    y = [dote[1] for dote in data]
    y_min = min(y)
    y_max = max(y)
    x_margin = (x_max - x_min)*0.05 
    y_margin = (y_max - y_min)*0.05 
    plt.xlim(x_min - x_margin, x_max + x_margin)
    plt.ylim(y_min - y_margin, y_max + y_margin)


    for dote_i, dote in enumerate(data):
        plt.scatter(dote[0], dote[1], color = colors[dote[2]])
        if colors[dote[2]] not in legended_colors:
            legended_colors.add(colors[dote[2]])
            legends.append(mpatches.Patch(color=colors[dote[2]], label='group: {}'.format(dote[2])))
        plt.text(dote[0]+0.002, dote[1]+0.002, '{}'.format(dote_i), horizontalalignment='left', 
                size=8, color=colors[dote[2]], weight='semibold')

    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.title('Hmmm, title')
    lgd = plt.legend(handles=legends, prop={'size': 6}, bbox_to_anchor=(1.04,1), loc="upper left")
    
    # place the legend inside of the view by counting the sizes
    # plt.gcf().canvas.draw()
    # invFigure = plt.gcf().transFigure.inverted()
    # lgd_pos = lgd.get_window_extent()
    # lgd_coord = invFigure.transform(lgd_pos)
    # lgd_xmax = lgd_coord[1, 0]
    # ax_pos = plt.gca().get_window_extent()
    # ax_coord = invFigure.transform(ax_pos)
    # ax_xmax = ax_coord[1, 0]
    # shift = 1 - (lgd_xmax - ax_xmax)
    # plt.gcf().tight_layout(rect=(0, 0, 0.87, 1))
    # or this simple way:
    plt.tight_layout(rect=(0, 0, 1, 1))


    plt.plot()
    plt.show()
    # plt.savefig(fname = 'scatters with legend.png')
    # plt.close()


if __name__ == '__main__':
    N = random.randint(0, 100)
    groups = random.randint(0, 10)
    data = [ (random.random(), random.random(), random.randint(0, groups)) for _ in range(N) ]
    scatter_with_legend(data)