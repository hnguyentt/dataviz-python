import matplotlib.pyplot as plt
from seaborn.categorical import _ViolinPlotter
import numpy as np
from scipy.stats import gaussian_kde
from sklearn.linear_model import LinearRegression

class _SinaPlotter(_ViolinPlotter):
    """
    https://github.com/mparker2/seaborn_sinaplot/blob/master/sinaplot/sinaplot.py
    """
    def __init__(self, x, y, hue, data, order, hue_order,
                 bw, cut, scale, scale_hue, gridsize,
                 width, inner, split, dodge, orient, linewidth,
                 color, palette, saturation,
                 violin_facealpha, point_facealpha):
        # initialise violinplot
        super(_SinaPlotter, self).__init__(
            x, y, hue, data, order, hue_order,
            bw, cut, scale, scale_hue, gridsize,
            width, inner, split, dodge, orient, linewidth,
            color, palette, saturation
        )

        # Set object attributes
        self.dodge = dodge
        # bit of a hack to set color alphas for points and violins
        self.point_colors = [(*color, point_facealpha) for color in self.colors]
        self.colors = [(*color, violin_facealpha) for color in self.colors]

    def jitterer(self, values, support, density):
        if values.size:
            max_density = np.interp(values, support, density)
            max_density *= self.dwidth
            low = 0 if self.split else -1
            jitter = np.random.uniform(low, 1, size=len(max_density)) * max_density
        else:
            jitter = np.array([])
        return jitter

    def draw_sinaplot(self, ax, kws):
        """Draw the points onto `ax`."""
        # Set the default zorder to 2.1, so that the points
        # will be drawn on top of line elements (like in a boxplot)
        for i, group_data in enumerate(self.plot_data):
            if self.plot_hues is None or not self.dodge:

                if self.hue_names is None:
                    hue_mask = np.ones(group_data.size, np.bool)
                else:
                    hue_mask = np.array([h in self.hue_names
                                         for h in self.plot_hues[i]], np.bool)
                    # Broken on older numpys
                    # hue_mask = np.in1d(self.plot_hues[i], self.hue_names)

                strip_data = group_data[hue_mask]
                density = self.density[i]
                support = self.support[i]

                # Plot the points in centered positions
                cat_pos = np.ones(strip_data.size) * i
                cat_pos += self.jitterer(strip_data, support, density)
                kws.update(color=self.point_colors[i])
                if self.orient == "v":
                    ax.scatter(cat_pos, strip_data, **kws)
                else:
                    ax.scatter(strip_data, cat_pos, **kws)

            else:
                offsets = self.hue_offsets
                for j, hue_level in enumerate(self.hue_names):
                    hue_mask = self.plot_hues[i] == hue_level
                    strip_data = group_data[hue_mask]
                    density = self.density[i][j]
                    support = self.support[i][j]
                    if self.split:
                        # Plot the points in centered positions
                        center = i
                        cat_pos = np.ones(strip_data.size) * center
                        jitter = self.jitterer(strip_data, support, density)
                        cat_pos = cat_pos + jitter if j else cat_pos - jitter
                        kws.update(color=self.point_colors[j])
                        if self.orient == "v":
                            ax.scatter(cat_pos, strip_data, zorder=2, **kws)
                        else:
                            ax.scatter(strip_data, cat_pos, zorder=2, **kws)
                    else:
                        # Plot the points in centered positions
                        center = i + offsets[j]
                        cat_pos = np.ones(strip_data.size) * center
                        cat_pos += self.jitterer(strip_data, support, density)
                        kws.update(color=self.point_colors[j])
                        if self.orient == "v":
                            ax.scatter(cat_pos, strip_data, zorder=2, **kws)
                        else:
                            ax.scatter(strip_data, cat_pos, zorder=2, **kws)

    def add_legend_data(self, ax, color, label):
        """Add a dummy patch object so we can get legend data."""
        # get rid of alpha band
        if len(color) == 4:
            color = color[:3]
        rect = plt.Rectangle([0, 0], 0, 0,
                             linewidth=self.linewidth / 2,
                             edgecolor=self.gray,
                             facecolor=color,
                             label=label)
        ax.add_patch(rect)

    def plot(self, ax, kws):
        """Make the sinaplot."""
        if kws.pop('violin', True):
            self.draw_violins(ax)
        elif self.plot_hues is not None:
            # we need to add the dummy box back in for legends
            for j, hue_level in enumerate(self.hue_names):
                self.add_legend_data(ax, self.colors[j], hue_level)
        self.draw_sinaplot(ax, kws)
        self.annotate_axes(ax)
        if self.orient == "h":
            ax.invert_yaxis()


def sinaplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None,
             bw="scott", cut=2, scale="count", scale_hue=True, gridsize=100,
             violin=True, inner=None, 
             width=.8, split=False, dodge=True, orient=None,
             linewidth=1, color=None, palette=None, saturation=.75, violin_facealpha=0.25,
             point_linewidth=None, point_size=5, point_edgecolor="none", point_facealpha=1,
             legend=True, random_state=None, ax=None, **kwargs):
    """
    https://github.com/mparker2/seaborn_sinaplot/blob/master/sinaplot/sinaplot.py
    """

    plotter = _SinaPlotter(x, y, hue, data, order, hue_order,
                           bw, cut, scale, scale_hue, gridsize,
                           width, inner, split, dodge, orient, linewidth,
                           color, palette, saturation,
                           violin_facealpha, point_facealpha)

    np.random.seed(random_state)
    point_size = kwargs.get("s", point_size)
    if point_linewidth is None:
        point_linewidth = point_size / 10
    if point_edgecolor == "gray":
        point_edgecolor = plotter.gray
    kwargs.update(dict(s=point_size ** 2,
                       edgecolor=point_edgecolor,
                       linewidth=point_linewidth,
                       violin=violin))

    if ax is None:
        ax = plt.gca()

    plotter.plot(ax, kwargs)
    if not legend:
        ax.legend_.remove()
    return ax

def plot_qq(data, ax=None, **kwargs):
    if ax is None:
        _, ax = plt.subplots(1, 1, figsize=(6, 6))
    
    color = kwargs.get('color', '#004E94')
    markersize = kwargs.get('markersize', 3)
    line_color = kwargs.get('line_color', '#8FAAD9')
    line_width = kwargs.get('line_width', 2)
    title = kwargs.get('title', None)
    
    qq = np.ones([len(data), 2])
    np.random.shuffle(data)
    qq[:, 0] = np.sort(data[0:len(data)])
    qq[:, 1] = np.sort(np.random.normal(size=len(data)))
    ax.plot(qq[:, 0], qq[:, 1], 'o', color=color, markersize=markersize)
    
    # Plot fitting line
    model = LinearRegression().fit(qq[:, 0].reshape(-1, 1), qq[:, 1])
    x = np.linspace(qq[:, 0].min(), qq[:, 0].max(), 100)
    y = model.predict(x.reshape(-1, 1))
    ax.plot(x, y, color=line_color, linewidth=line_width)
    ax.set_title(title)
    
def ridgeline(data, ax=None, overlap=0, fill=None, labels=None, n_points=150, **kwargs):
    """
    Creates a standard ridgeline plot.

    data, list of lists.
    overlap, overlap between distributions. 1 max overlap, 0 no overlap.
    fill, matplotlib color to fill the distributions.
    n_points, number of points to evaluate each distribution function.
    labels, values to place on the y axis to describe the distributions.
    """
    if fill is not None:
        fill = fill if isinstance(fill, list) else [fill] * len(data)
    alpha = kwargs.get('alpha', [1] * len(data))
    alpha = alpha if isinstance(alpha, list) else [alpha] * len(data)
    
    if ax is None:
        _, ax = plt.subplots(1,1)
    if overlap > 1 or overlap < 0:
        raise ValueError('overlap must be in [0 1]')
    xx = np.linspace(np.min(np.concatenate(data)),
                     np.max(np.concatenate(data)), n_points)
    curves = []
    ys = []
    for i, d in enumerate(data):
        pdf = gaussian_kde(d)
        y = i*(1.0-overlap)
        ys.append(y)
        curve = pdf(xx)
        if fill is not None:
            if type(fill) == list: 
                current_fill = fill[i] 
            else:
                current_fill = fill
            
            ax.fill_between(xx, np.ones(n_points)*y, 
                            curve+y, zorder=len(data)-i+1, 
                            color=current_fill,
                            alpha=alpha[i])
            
        ax.plot(xx, curve+y, c=fill[i], zorder=len(data)-i+1)
    if labels:
        ax.yticks(ys, labels)