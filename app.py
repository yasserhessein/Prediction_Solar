from flask import Flask, render_template, request
import joblib

# __name__ is equal to app.py
app = Flask(__name__)

# load model from model.pck
#model = joblib.load('model2.pkl')



@app.route("/")
def home():
    return render_template('index.html')





@app.route("/predict", methods=["POST"])
def predict():
	Global_SPP = request.form['Global_SPP']
	Azimuth_Angle = request.form['Azimuth_Angle']
	Solar_Eclipse = request.form['Solar_Eclipse']
	Total_Cloud_Cover = request.form['Total_Cloud_Cover']
	Station_Pressure= request.form['Station_Pressure']
	Precipitation = request.form['Precipitation']
	Moisture = request.form['Moisture']
	Period = request.form['Period']

	if Period == 'evening':
		is_morning = 0
		is_aftermoon = 0
		is_evening = 1
	elif Period == 'morning ':
		is_aftermoon = 0
		is_morning  = 1
		is_evening = 0

	else:
		is_evening = 0
		is_morning = 0


		

	Zenith_Angle = int(round(model.predict([[Global_SPP, Azimuth_Angle, Solar_Eclipse,Total_Cloud_Cover,Station_Pressure,Precipitation,Moisture, is_morning, is_aftermoo]])[0]))
	return render_template("index.html", Zenith_Angle=Zenith_Angle)	





if __name__ == "__main__":
    app.run()
