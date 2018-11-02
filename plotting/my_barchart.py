import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib as mpl


def plot_barchart(data, x):
    groups = len(data)
    xposes = np.arange(len(x))
    x_delta = xposes[1] - xposes[0]
    width = x_delta/(groups+2) # 0.35 # width of the bars
    

    colors = [plt.cm.rainbow(each) for each in np.linspace(0, 1, groups)]
    # mpl.style.use('ggplot') # equal to mpl.style.use('seaborn')
    font = {'family' : 'normal',
            'weight' : 'bold',
            'size' : 8
            }
    plt.rc('font', **font)


    fig, ax = plt.subplots() # should be after styles certained
    for group_i in range(groups):
        # for i, x in enumerate(xposes):
        if groups % 2 == 0:
            rects = ax.bar(xposes + (group_i-groups//2)*width + width/2, 
                        data[group_i], width,
                        color=colors[group_i], 
                        label='group: {}'.format(group_i))
        else:
            rects = ax.bar(xposes + (group_i-groups//2)*width, 
                        data[group_i], width,
                        color=colors[group_i], 
                        label='group: {}'.format(group_i))

    ax.set_ylabel('x axis name')
    ax.set_ylabel('y axis name')
    ax.set_title('Hmmm, title')
    ax.set_xticks(xposes)
    ax.set_xticklabels(x)
    
    # ax.legend() # or:
    # plt.legend()

    # legend mpatch array is not used, because labels are certained while plotting the bars
    lgd = plt.legend(prop={'size': 6}, bbox_to_anchor=(1.04,1), loc="upper left")
    plt.tight_layout(rect=(0, 0, 1, 1))

    plt.show()


if __name__ == '__main__':
    groups = random.randint(2, 5)
    x = ['1s', '1h', '1d', '1y', '10y', '100y', '1000y']
    data = [ [ random.random() for _ in range(len(x))] for _ in range(groups)]
    plot_barchart(data, x)