import math
import matplotlib.pyplot as plt
import numpy as np
# from mayavi import mlab
import glyph_visualization_lib as gvl


def task1():
    n = 256

    x = np.linspace(-10., 10., n)
    y = np.linspace(-10., 10., n)
    X, Y = np.meshgrid(x, y)
    Z = (7 * np.log(x ** 2 + (1 / 13))) - (4 * np.sin(X * Y))

    plt.pcolormesh(X, Y, Z)
    plt.show()


def task2_1():
    xx, yy = np.meshgrid(np.linspace(-10, 10, 10),
                         np.linspace(-10, 10, 10))

    u_val = (xx ** 2) * yy
    v_val = -yy

    plt.quiver(xx, yy, u_val, v_val)
    plt.show()

    plt.streamplot(xx, yy, u_val, v_val)
    plt.show()


def task2_2():
    def u(x, y):
        return (x ** 2) * y

    def v(x, y):
        return -y

    def create_stream_line(x0, y0, u, v, t0=-10, t1=10, dt=0.001):
        t = np.arange(t0, t1, dt)
        xx_new = np.zeros_like(t)
        yy_new = np.zeros_like(t)
        xx_new[0] = x0
        yy_new[0] = y0

        for i in range(1, t.size):
            xx_new[i] = x0 + u(x0, y0) * dt
            yy_new[i] = y0 + v(x0, y0) * dt
            x0, y0 = xx_new[i], yy_new[i]

        return xx_new, yy_new

    for i in range(-10, 10):
        x1, y1 = create_stream_line(i, 0, u, v)
        plt.plot(x1, y1)
    plt.show()


def task3():
    ax = plt.figure().add_subplot(projection='3d')

    x, y, z = np.meshgrid(np.arange(-10, 10, 4.9),
                          np.arange(-10, 10, 4.9),
                          np.arange(-10, 10, 3))

    u = (x + z) / (x ** 2)
    v = 1 / y
    w = 1 / z

    ax.quiver(x, y, z, u, v, w, length=0.2, color='black')
    plt.show()


def task4():
    def main():
        x = np.linspace(1, 3, 4, dtype=float, endpoint=True)
        y = np.linspace(1, 3, 4, dtype=float, endpoint=True)
        z = np.linspace(1, 3, 4, dtype=float, endpoint=True)
        X, Y, Z = np.meshgrid(x, y, z)
        stress_tensor = np.array([
            [np.log(X)/np.sin(X), (X ** (1/2)) / Y, (Y ** (1/2)) / Z],
            [(X ** (1/2)) / Y, np.log(Y)/np.sin(Y), (Z ** (1/2)) / X],
            [(Y ** (1/2)) / Z, (Z ** (1/2)) / X, np.log(Z)/np.sin(Z)]
        ])
        print(stress_tensor.shape)
        vm_stress = gvl.get_von_Mises_stress(stress_tensor)
        glyph_radius = 0.25
        limits = [np.min(vm_stress), np.max(vm_stress)]
        colormap = plt.get_cmap('rainbow', 120)
        fig2 = plt.figure()
        ax = fig2.add_subplot(111, projection='3d')

        for i in range(x.size):
            for j in range(y.size):
                for k in range(z.size):
                    center = [x[i], y[j], z[k]]
                    data = stress_tensor[:, :, i, j, k]
                    color = colormap(gvl.get_colormap_ratio_on_stress(vm_stress[i, j, k], limits))[:3]
                    """
                    glyph_type = {0: 'cuboid', 1: 'cylinder', 2: 'ellipsoid', 3: 'superquadric'}
                    if glyph_type == 3 (superquadric)
                    there are glyph shape type
                    0 - superquadrics,
                    1 - Kindlmann_glyph,
                    2 - Kindlmann_modified_glyph
                    """
                    x_g, y_g, z_g = gvl.get_glyph_data(center, data, limits, glyph_points=12, glyph_radius=glyph_radius,
                                                       glyph_type=3,
                                                       superquadrics_option=2)
                    surf = ax.plot_surface(x_g, y_g, z_g, linewidth=0, antialiased=True, color=color)
                    surf = ax.plot_wireframe(x_g, y_g, z_g, linewidth=1, antialiased=True, color=color)

        plt.show()
        pass

    if __name__ == '__main__':
        main()


task1()
task2_1()
task2_2()
task3()
task4()
