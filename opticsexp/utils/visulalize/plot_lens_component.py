import matplotlib.pyplot as plt
from ...components.lens_component import LensComponent

def plot_lens_component(lens_component: LensComponent):
    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(111)

    ax.plot(
        lens_component.optical_axis[[0, 1]][:, 0],
        lens_component.optical_axis[[0, 1]][:, 1], 
        c = 'r'
        )
    ax.plot(
        lens_component.optical_axis[[0, 2]][:, 0],
        lens_component.optical_axis[[0, 2]][:, 1], 
        c = 'b'
        )
    ax.scatter(
        [lens_component.optical_axis[0][0]], 
        [lens_component.optical_axis[0][1]], 
        c = 'k',
        marker='$⊙$'
    )

    ax.plot(
        lens_component.surface_1_axis[[0, 1]][:, 0],
        lens_component.surface_1_axis[[0, 1]][:, 1], 
        c = 'r'
        )
    ax.plot(
        lens_component.surface_1_axis[[0, 2]][:, 0],
        lens_component.surface_1_axis[[0, 2]][:, 1], 
        c = 'b'
        )
    ax.scatter(
        [lens_component.surface_1_axis[0][0]], 
        [lens_component.surface_1_axis[0][1]], 
        c = 'k',
        marker='$⊙$'
    )


    ax.plot(
        lens_component.surface_2_axis[[0, 1]][:, 0],
        lens_component.surface_2_axis[[0, 1]][:, 1], 
        c = 'r'
        )
    ax.plot(
        lens_component.surface_2_axis[[0, 2]][:, 0],
        lens_component.surface_2_axis[[0, 2]][:, 1], 
        c = 'b'
        )
    ax.scatter(
        [lens_component.surface_2_axis[0][0]], 
        [lens_component.surface_2_axis[0][1]], 
        c = 'k',
        marker='$⊙$'
    )

    ax.scatter(
        [lens_component.pivot[0]], 
        [lens_component.pivot[1]], 
        c = 'k',
        marker='x'
    )

    ax.set_aspect('equal')


    return fig, ax