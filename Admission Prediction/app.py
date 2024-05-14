from flask import Flask, render_template, request
import joblib
import openpyxl

app = Flask(__name__,)

# Load the trained SVR model
model = joblib.load("svr_model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/university")
def university():
    return render_template("university.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/predict")
def prediction():
    return render_template("predict.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get the input values from the form
    GRE_Quantz = int(request.form['GRE Quant'])
    GRE_Ver = int(request.form['GRE Verbal'])
    TOEFL_Score = int(request.form['TOEFL Score'])
    University_Rating = int(request.form['University Rating'])
    SOP = float(request.form['SOP'])
    LOR = float(request.form['LOR'])
    CGPA = float(request.form['CGPA'])
    Research = int(request.form['Research'])
    GRE_Score= GRE_Quantz+GRE_Ver
    
     # Transform the input values using the scaler
    input_data = [[GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA, Research]]
    input_data_scaled = scaler.transform(input_data)

    # Make a prediction using the SVR model
    prediction = model.predict(input_data_scaled)[0]
    
    # Make a prediction using the SVR model
    #prediction = model.predict([[GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA, Research]])

    # Open the Excel file
    workbook = openpyxl.load_workbook('data.xlsx')

    # Select the active worksheet
    worksheet = workbook.active

    # Get the last row in the worksheet
    last_row = worksheet.max_row

    # Insert a new row after the last row
    worksheet.insert_rows(last_row + 1)

    # Write data to Excel worksheet
    worksheet.append([GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA, Research,prediction])

    # Save Excel workbook
    workbook.save('data.xlsx')
    
    # Render the prediction in a new HTML page
    return render_template('predict.html', prediction_text='Your Admission chances are {:.2f}%'.format(prediction*100))

if __name__ == "__main__":
    app.run(debug=True)
