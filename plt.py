import matplotlib
from matplotlib.widgets import RangeSlider
matplotlib.use('WXAgg')
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
import matplotlib.pyplot as plt

class RangeFilter:
    def __init__(self, panel, min, max):
        """
        Initializes the range filter with given min, max, start, and end values.
        Creates a slider and sets up the initial configuration.
        """
        self.min = min
        self.max = max
        self.current_min = min
        self.current_max = max
        self.panel = panel
        self.slider = None
        self.fig = None
        self.canvas = None
        self.min_text = None
        self.max_text = None

        self.create_slider()

    def create_slider(self):
        """
        Create the range slider and the associated UI elements.
        """
        self.fig, axs = plt.subplots()
        self.fig.subplots_adjust(bottom=0.25)
        slider_ax = self.fig.add_axes([0.1, 0.7, 0.6, 0.05])

        # Create the RangeSlider with the initial values
        self.slider = RangeSlider(slider_ax, " ", self.min, self.max, valinit=(self.current_min, self.current_max))        
        self.slider.valtext.set_visible(False)
        self.slider.ax.set_xticks([])
        
        # Hide unnecessary grid and axes spines
        axs.set_visible(False)
        for spine in axs.spines.values():
            spine.set_visible(False)
        axs.xaxis.set_visible(False)
        axs.yaxis.set_visible(False)
        axs.grid(False)

        self.min_text = slider_ax.text(0, -6, f'{self.current_min}', transform=slider_ax.transAxes, va='center')
        self.max_text = slider_ax.text(0.8, -6, f'{self.current_max}', transform=slider_ax.transAxes, va='center')

        # Resize the canvas to fit the panel
        h, w = self.panel.GetSize()
        self.fig.set_size_inches(h / self.fig.get_dpi(), w / self.fig.get_dpi())
        self.canvas = FigureCanvasWxAgg(self.panel, -1, self.fig)
        self.canvas.SetSize((h, w))
        self.panel.Layout()
        self.canvas.draw()

        self.slider.on_changed(self.update_labels)
        self.update_labels((self.current_min, self.current_max))

    def update_labels(self, val):
        """
        Updates the min/max labels and their positions based on the slider values.
        """
        self.current_min, self.current_max = val
        self.min_text.set_x((self.current_min - self.min) / (self.max - self.min) * 0.8)
        self.max_text.set_x((self.current_max - self.min) / (self.max - self.min) * 0.8 + 0.1)
        self.min_text.set_text(f'{self.current_min:.1f}')
        self.max_text.set_text(f'{self.current_max:.1f}')
        self.fig.canvas.draw_idle()

    def update_slider_range(self, min, max, current_min, current_max):
        """
        Updates the range and position of the slider with new values.
        """
        self.min = min
        self.max = max
        self.current_min = current_min
        self.current_max = current_max

        self.slider.ax.remove()
        self.create_slider()

    def getValue(self):
        """
        Returns the current min and max values of the slider.
        """
        return self.current_min, self.current_max

def progression_bar(panel, current_intake, estimated_intake, user_goal):
    fig, ax = plt.subplots()
    if ((current_intake+estimated_intake)< user_goal):
        ax.barh([0], [(1000/user_goal)*current_intake], color='#0ABAB5')
        ax.barh([0], [(1000/user_goal)*estimated_intake], left=[(1000/user_goal)*current_intake], color='white', edgecolor='gray', hatch='//')
    else:
        ax.barh([0], [(1000/user_goal)*current_intake], color='#0ABAB5')
        ax.barh([0], [(1000/user_goal)*user_goal-current_intake], left=[(1000/user_goal)*current_intake], color='#e2808a', edgecolor='gray',hatch='//')

    ax.set_xlim(0, 1000)
    ax.set_yticks([])
    ax.set_xticks([])

    h, w = panel.GetSize()
    fig.set_size_inches(h / fig.get_dpi(), w / fig.get_dpi())
    canvas = FigureCanvasWxAgg(panel, -1, fig)
    canvas.SetSize((h, w))
    panel.Layout()
    canvas.draw()
    plt.close(fig)

def plot_chart(panel, chartType, nutrients, values):
    fig, ax = plt.subplots()
    colors = ['#0ABAB5', '#004B49', '#003D36', '#7D5BA6', '#A48FBF']
    explode = [0.1] + [0] * (len(values) - 1)
    if chartType == 'Pie':
        wedges, texts = ax.pie(values, labels=None, explode=explode, colors=colors, autopct=None,shadow=True)
        total = sum(values)
        legend_labels = [f"{nutrient}: {value / total * 100:.1f}%" for nutrient, value in zip(nutrients, values)]
        ax.legend(wedges, legend_labels, loc="upper right", bbox_to_anchor=(1.1, 1))
        ax.set_title(f'Nutritional Information')
    elif chartType == 'Bar':
        bars = ax.bar(nutrients, values, color=colors)
        ax.set_ylabel('Values')
        ax.set_xticks([])
        ax.set_title(f'Nutritional Information')
        ax.legend(bars, nutrients, loc='upper left', bbox_to_anchor=(-0.1, 0), ncol=2, frameon=False)

    left, bottom, width, height = ax.get_position().bounds
    ax.set_position([left+0.03, bottom + 0.1, width, height])
    h, w = panel.GetSize()
    fig.set_size_inches(h / fig.get_dpi(), w / fig.get_dpi())
    canvas = FigureCanvasWxAgg(panel, -1, fig)
    canvas.SetSize((h, w))
    panel.Layout()
    canvas.draw()