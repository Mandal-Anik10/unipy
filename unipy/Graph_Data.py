# Graph Plotting:


def Graph_Data(xx, yy, small_x, small_y):
    x_data = []
    y_data = []
    for i in range(len(xx)):
        x_data.append(xx[i]/small_x)
        y_data.append(yy[i]/small_y)
    return x_data, y_data
