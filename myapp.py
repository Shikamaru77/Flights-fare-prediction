from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("RFC_Flights.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    global predict
    if request.method == "POST":
        # date and time section begins here---->
        """the columns are:
        'total_stops',
        'month_name',
        'day_name',
        'dep_hour',
        'dep_min',
        'arrival_hour',
        'arrival_min',
        'duration_hours',
        'duration_mins',
        """
        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        journey_month = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)
        # print("Journey Date : ",Journey_day, Journey_month)

        # Departure
        dep_hour = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").hour)
        dep_min = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").minute)
        # print("Departure : ",Dep_hour, Dep_min)

        # Arrival
        date_arr = request.form["Arrival_Time"]
        arrival_hour = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").hour)
        arrival_min = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").minute)
        # print("Arrival : ", Arrival_hour, Arrival_min)

        # Duration
        duration_hour = abs(arrival_hour - dep_hour)
        duration_min = abs(arrival_min - dep_min)
        # print("Duration : ", dur_hour, dur_min)

        # Total Stops

        # Example for 'total_stops' feature
        total_stops = int(request.form["stops"])

        # print(Total_stops)

        # Airline section
        """Here, the airline names are
            'Air India',
            'GoAir',
            'IndiGo',
            'Jet Airways',
            'Jet Airways Business',
            'Multiple carriers',
            'Multiple carriers Premium economy',
            'SpiceJet',
            'Trujet', 'Vistara',
            'Vistara Premium economy',
            """

        airline = request.form["airline"]
        if airline == "Jet Airways":
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif airline == "IndiGo":
            Jet_Airways = 0
            IndiGo = 1
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif airline == "Air India":
            jet_airways = 0
            indigo = 0
            air_india = 1
            multiple_carriers = 0
            spicejet = 0
            vistara = 0
            goair = 0
            multiple_carriers_premium_economy = 0
            jet_airways_business = 0
            vistara_premium_economy = 0
            trujet = 0

        elif airline == "Multiple carriers":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif airline == "SpiceJet":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif airline == "Vistara":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif airline == "GoAir":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif airline == "Multiple carriers Premium economy":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 1
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        elif airline == "Jet Airways Business":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 1
            Vistara_Premium_economy = 0
            Trujet = 0

        elif airline == "Vistara Premium economy":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 1
            Trujet = 0

        elif airline == "Trujet":
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 1

        else:
            Jet_Airways = 0
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0

        # source
        # Banglore = 0 (not in column)
        # Source
        source = request.form["Source"]
        if source == "Delhi":
            source_Delhi = 1
            source_Kolkata = 0
            source_Mumbai = 0
            source_Chennai = 0

        elif source == "Kolkata":
            source_Delhi = 0
            source_Kolkata = 1
            source_Mumbai = 0
            source_Chennai = 0

        elif source == "Mumbai":
            source_Delhi = 0
            source_Kolkata = 0
            source_Mumbai = 1
            source_Chennai = 0

        elif source == "Chennai":
            source_Delhi = 0
            source_Kolkata = 0
            source_Mumbai = 0
            source_Chennai = 1

        else:
            source_Delhi = 0
            source_Kolkata = 0
            source_Mumbai = 0
            source_Chennai = 0
        # print(s_Delhi,
        #     s_Kolkata,
        #     s_Mumbai,
        #     s_Chennai)

        # Destination
        # Banglore = 0 (not in column as we omitted [drop_first] through one hot encoding to remove overfitting issues)
        destination = request.form["destination"]
        if destination == "Cochin":
            destination_cochin = 1
            destination_delhi = 0
            destination_new_delhi = 0
            destination_hyderabad = 0
            destination_kolkata = 0

        elif destination == "Delhi":
            destination_Cochin = 0
            destination_Delhi = 1
            destination_New_Delhi = 0
            destination_Hyderabad = 0
            destination_Kolkata = 0

        elif destination == "New_Delhi":
            destination_Cochin = 0
            destination_Delhi = 0
            destination_New_Delhi = 1
            destination_Hyderabad = 0
            destination_Kolkata = 0

        elif destination == "Hyderabad":
            destination_Cochin = 0
            destination_Delhi = 0
            destination_New_Delhi = 0
            destination_Hyderabad = 1
            destination_Kolkata = 0

        elif destination == "Kolkata":
            destination_Cochin = 0
            destination_Delhi = 0
            destination_New_Delhi = 0
            destination_Hyderabad = 0
            destination_Kolkata = 1

        else:
            destination_Cochin = 0
            destination_Delhi = 0
            destination_New_Delhi = 0
            destination_Hyderabad = 0
            destination_Kolkata = 0

            # Prepare the feature list for prediction
            predict = model.predict([[
                total_stops,
                journey_month,
                journey_day,
                dep_hour,
                dep_min,
                arrival_hour,
                arrival_min,
                duration_hour,
                duration_min,
                Air_India,
                GoAir,
                IndiGo,
                Jet_Airways,
                Jet_Airways_Business,
                Multiple_carriers,
                Multiple_carriers_Premium_economy,
                SpiceJet,
                Trujet,
                Vistara,
                Vistara_Premium_economy,
                source_Chennai,
                source_Delhi,
                source_Kolkata,
                source_Mumbai,
                destination_Cochin,
                destination_Delhi,
                destination_Hyderabad,
                destination_Kolkata,
                destination_New_Delhi
            ]])

            output = round(predict[0])

            return render_template('index.html', predict_text="The price of the flight would be {}".format(output))

        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
