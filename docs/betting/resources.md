# Interactive Calculator

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
</style>

<py-script>
# Your Python code here
</py-script>

<input id="num1" type="number" placeholder="Enter first number">
<input id="num2" type="number" placeholder="Enter second number">
<button py-click="calculate">Add</button>

<p>Result: <span id="result"></span></p>
