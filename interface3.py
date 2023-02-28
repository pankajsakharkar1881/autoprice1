from flask import Flask,jsonify,render_template,request
import config
from utils import AUTO_PRICE

app = Flask(__name__)

@app.route("/")
def get_home():
    return "Welcome to API Testing"

@app.route("/AUTOPRICE",methods = ["POST","GET"])
def get_price():
    if request.method == "POST":
        print("We are using POST Method")
        data = request.form   # ImmutableMultiDict >>list of tuple (key , value pair)
        print("Data1 using POST method",data)
        symboling = eval(data["symboling"])
        normalized_losses = int(data["normalized_losses"])
        make = (data["make"])  # object
        fuel_type = (data["fuel_type"])  # object 
        aspiration = (data["aspiration"])  # object aspiration
        num_of_doors = (data["num_of_doors"])  # object 
        body_style = (data["body_style"])  # object 
        drive_wheels = (data["drive_wheels"])  # object
        engine_location = (data["engine_location"])  # object
        wheel_base = int(data["wheel_base"])
        length = int(data["length"])
        width = int(data["width"])
        height = int(data["height"])
        curb_weight = int(data["curb_weight"])
        engine_type = (data["engine_type"])  # object
        num_of_cylinders = data["num_of_cylinders"]
        engine_size = int(data["engine_size"])
        fuel_system = data["fuel_system"]
        bore = eval(data["bore"])
        stroke = int(data["stroke"])
        compression_ratio = int(data["compression_ratio"])
        horsepower = int(data["horsepower"])
        peak_rpm = int(data["peak_rpm"])
        city_mpg = int(data["city_mpg"])
        highway_mpg = int(data["highway_mpg"])

        """ Calling get_Predicted_price() method for prediction
        """
        auto_obj = AUTO_PRICE(symboling,normalized_losses,make,fuel_type,aspiration,num_of_doors,body_style,drive_wheels,engine_location,wheel_base,length,width,height,curb_weight,engine_type,num_of_cylinders,engine_size,fuel_system,bore,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg)
        result = auto_obj.get_predicted_price()
        return jsonify({"Result":f"Predcicted Auto car price is {result}"})


    elif request.method == "GET":
        print("we are using GET method")
        data = request.form 
        print("Data2 using GET method",data)
        symboling = eval(data["symboling"])
        normalized_losses = int(data["normalized_losses"])
        make = (data["make"])  # object
        fuel_type = (data["fuel_type"])  # object 
        aspiration = (data["aspiration"])  # object aspiration
        num_of_doors = (data["num_of_doors"])  # object 
        body_style = (data["body_style"])  # object 
        drive_wheels = (data["drive_wheels"])  # object
        engine_location = (data["engine_location"])  # object
        wheel_base = int(data["wheel_base"])
        length = int(data["length"])
        width = int(data["width"])
        height = int(data["height"])
        curb_weight = int(data["curb_weight"])
        engine_type = (data["engine_type"])  # object
        num_of_cylinders = data["num_of_cylinders"]
        engine_size = int(data["engine_size"])
        fuel_system = data["fuel_system"]
        bore = eval(data["bore"])
        stroke = int(data["stroke"])
        compression_ratio = int(data["compression_ratio"])
        horsepower = int(data["horsepower"])
        peak_rpm = int(data["peak_rpm"])
        city_mpg = int(data["city_mpg"])
        highway_mpg = int(data["highway_mpg"])

        """ Calling get_Predicted_price() method for prediction
        """
        auto_obj = AUTO_PRICE(symboling,normalized_losses,make,fuel_type,aspiration,num_of_doors,body_style,drive_wheels,engine_location,wheel_base,length,width,height,curb_weight,engine_type,num_of_cylinders,engine_size,fuel_system,bore,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg)
        result = auto_obj.get_predicted_price()
        return jsonify({"Result":f"Predcicted Auto car price is {result}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=config.PORT_NUMBER_1)