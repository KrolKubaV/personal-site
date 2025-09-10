# Interactive Normal Distribution Simulator

<style>
input, button {
    padding: 0.5em;
    margin: 0.2em;
    font-family: inherit;
    border-radius: 4px;
    border: 1px solid #ccc;
}
button {
    background-color: #4CAF50;
    color: white;
    cursor: pointer;
}
button:hover {
    background-color: #45a049;
}
#plot {
    margin-top: 1em;
}
</style>

<!-- PyScript setup -->
<py-script>
import matplotlib.pyplot as plt
import numpy as np
from pyscript import Element, display

# Global figure and axes
fig, ax = plt.subplots(figsize=(6,3))
plt.tight_layout()

def plot_distribution(*args):
    # Clear previous plot
    ax.clear()

    # Get user inputs
    mu = float(Element("mu").value)
    sigma2 = float(Element("sigma2").value)
    sigma = np.sqrt(sigma2)

    # Create x values
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 500)
    y = (1/(sigma * np.sqrt(2*np.pi))) * np.exp(-0.5 * ((x - mu)/sigma)**2)

    # Plot distribution
    ax.plot(x, y, label=f'N({mu}, {sigma2})')
    ax.fill_between(x, y, alpha=0.2)
    ax.legend()
    display(fig, target="plot")

def generate_random(*args):
    mu = float(Element("mu").value)
    sigma2 = float(Element("sigma2").value)
    sigma = np.sqrt(sigma2)

    # Generate random sample
    sample = np.random.normal(mu, sigma)
    Element("sample").write(f"{sample:.4f}")
</py-script>

<!-- Inputs and buttons -->
<div>
    <label>μ: <input id="mu" type="number" value="0"></label>
    <label>σ²: <input id="sigma2" type="number" value="1" min="0"></label>
    <button py-click="plot_distribution">Plot Distribution</button>
    <button py-click="generate_random">Generate Random Sample</button>
</div>

<!-- Output -->
<div id="plot"></div>
<p>Random Sample: <span id="sample"></span></p>
