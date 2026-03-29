from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    """Handles both Login and Signup for demonstration."""
    if request.method == 'POST':
        # Dummy authentication check, redirects to dashboard
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    """Renders the prediction dashboard and handles form submissions."""
    prediction = None
    probability = None
    
    if request.method == 'POST':
        # Extract features from the form if needed:
        # data = request.form.to_dict()
        
        # Dummy prediction output for the UI
        prediction = "$42,850.75"
        probability = "89.4%"
        
    return render_template('dashboard.html', prediction=prediction, probability=probability)

if __name__ == '__main__':
    app.run(debug=True)