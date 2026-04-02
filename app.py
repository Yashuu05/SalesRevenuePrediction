from flask import Flask, render_template, request, redirect, url_for
import joblib
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
    prediction = None
    probability = None
    
    # load saved model
    def load_model():
        return joblib.load('model/xgb.pkl')
    
    model = load_model()
    
    if request.method == 'POST':
        print("Form data received:", request.form)
        # Extract features from the form in the correct order
        feature_order = [
            'region', 'channel', 'product_category', 'customer_segment', 'ad_spend', 
            'price', 'discount_rate', 'market_reach', 'impressions', 'click_through_rate', 
            'competition_index', 'seasonality_index', 'campaign_duration_days', 
            'customer_lifetime_value', 'year', 'month', 'day', 'time_of_day', 
            'cost_per_impression', 'cost_per_click', 'reach_per_spend', 'value_ratio'
        ]
        
        # Convert form data to list of values in correct order
        try:
            # Extract values and convert to appropriate types
            features = []
            for feature in feature_order:
                value = request.form.get(feature)
                if value is None:
                    raise ValueError(f"Missing feature: {feature}")
                
                # Convert categorical features to numerical (simplified encoding)
                if feature in ['region', 'channel', 'product_category', 'customer_segment', 'time_of_day']:
                    # Simple encoding - you may need to match your training encoding
                    categorical_mapping = {
                        'region': {'North': 0, 'South': 1, 'East': 2, 'West': 3, 'Central': 4},
                        'channel': {'Social Media': 0, 'Affiliate': 1, 'Influencer': 2, 'Search': 3, 'TV': 4, 'Email': 5},
                        'product_category': {'Lighting': 0, 'Storage': 1, 'General': 2, 'Seasonal': 3, 'Kitchen': 4, 'Stationery': 5},
                        'customer_segment': {'Budget': 0, 'Standard': 1, 'Premium': 2},
                        'time_of_day': {'morning': 0, 'afternoon': 1, 'evening': 2, 'night': 3}
                    }
                    mapping = categorical_mapping.get(feature, {})
                    encoded_value = mapping.get(value, 0)
                    features.append(encoded_value)
                else:
                    # Convert numerical features to float
                    features.append(float(value))
            
            # Reshape for 2D array (single sample)
            features_2d = [features]  # This creates [[feature1, feature2, ...]]
            
            # Make prediction
            prediction = model.predict(features_2d)[0]
            # Format prediction as currency
            formatted_prediction = f"INR {prediction:.2f}"
            # For demonstration, set a default confidence score
            probability = "95%"
            
        except Exception as e:
            print(f"Prediction error: {e}")
            formatted_prediction = f"Error: {str(e)}"
            probability = "N/A"
        
        print(f"Prediction: {prediction}")
        print(f"Formatted prediction: {formatted_prediction if prediction else None}")
        print(f"Probability: {probability}")
        
    else:
        # For testing, show a sample result on GET request
        formatted_prediction = "INR 12345.67"
        probability = "95%"
    
    return render_template('dashboard.html', prediction=formatted_prediction if formatted_prediction else None, probability=probability)

if __name__ == '__main__':
    app.run(debug=True)