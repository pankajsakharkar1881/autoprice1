import config
import json
import pickle
import numpy as np

class AUTO_PRICE():
    def __init__(self,symboling,normalized_losses,make,fuel_type,aspiration,num_of_doors,body_style,drive_wheels,engine_location,wheel_base,length,width,height,curb_weight,engine_type,num_of_cylinders,engine_size,fuel_system,bore,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg):   
        
        self.symboling                    = symboling
        self.normalized_losses            = normalized_losses
        self.make                         = make  # one hot
        self.fuel_type                    = fuel_type
        self.aspiration                   = aspiration
        self.num_of_doors                 =  num_of_doors
        self. body_style                  = "body-style_" + body_style # onehot encoded
        self.drive_wheels                 = drive_wheels
        self.engine_location              = engine_location
        self.wheel_base                   = wheel_base
        self.length                       = length
        self.width                        = width
        self.height                       = height
        self.curb_weight                  = curb_weight
        self.engine_type                  = "engine-type_"+ engine_type # onehot encoded
        self.num_of_cylinders             = num_of_cylinders
        self.engine_size                  = engine_size
        self.fuel_system                  = "fuel-system_"+ fuel_system # onehot encoded
        self.bore                         = bore
        self.stroke                       = stroke
        self.compression_ratio            = compression_ratio
        self.horsepower                   = horsepower
        self.peak_rpm                     = peak_rpm
        self.city_mpg                     = city_mpg
        self.highway_mpg                  = highway_mpg

    def load_model(self):
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.model = pickle.load(f)  # loading model 
        with open(config.JSON_FILE_PATH,"r") as file:
            self.json_data = json.load(file)  # laoding all encoded factors

    def get_predicted_price(self):
        self.load_model() # instance method calling
        array = np.zeros(len(self.json_data["Columns"]),dtype=int)

        array[0] = self.symboling
        array[1] = self.normalized_losses
        array[2] = self.json_data["fuel_type_values"][self.fuel_type] 
        array[3] = self.json_data["aspiration_values"][self.aspiration] 
        array[4] = self.json_data["num_of_doors_values"][self.num_of_doors] 
        array[5] = self.json_data["drive_wheels_values"][self.drive_wheels]
        array[6] = self.json_data["engine_location_values"][self.engine_location]
        array[7] = self.wheel_base
        array[8] = self.length
        array[9] = self.width
        array[10] =self.height
        array[11] =self.curb_weight
        array[12] = self.json_data["num_of_cylinders_values"][self.num_of_cylinders]
        array[13] = self.engine_size
        array[14] = self.bore
        array[15] =self.stroke
        array[16] =self.compression_ratio
        array[17] =self.horsepower
        array[18] =self.peak_rpm
        array[19] =self.city_mpg
        array[20] =self.highway_mpg
        make_index  = self.json_data["Columns"].index(self.make)
        array[make_index] = 1
        body_style_index  = self.json_data["Columns"].index(self.body_style)
        array[body_style_index] = 1
        engine_type_index  = self.json_data["Columns"].index(self.engine_type)
        array[engine_type_index] = 1
        fuel_system_index  = self.json_data["Columns"].index(self.fuel_system)
        array[fuel_system_index] = 1

        print("Array>>.",array)

        predicted_price = np.around(self.model.predict([array])[0],2)

        return predicted_price
    
if __name__ == "__main__":
    symboling                    = 3
    normalized_losses            = 115
    make                         = "audi" # onehot encoded
    fuel_type                    = "gas"
    aspiration                   = "std"
    num_of_doors                 =  "two"
    body_style                   = "convertible" # onehot encoded
    drive_wheels                 = "rwd"
    engine_location              ="rear"
    wheel_base                   = 88.6
    length                       = 168.8
    width                        = 64.1
    height                       = 48.8
    curb_weight                  = 2548
    engine_type                  = "dohc" # onehot encoded
    num_of_cylinders             = "four"
    engine_size                  = 14
    fuel_system                  = "mpfi" # onehot encoded
    bore                         = 3.47
    stroke                       = 2.68
    compression_ratio            = 9.0
    horsepower                   = 111
    peak_rpm                     = 5000
    city_mpg                     = 21
    highway_mpg                  = 27
    auto_obj = AUTO_PRICE(symboling,normalized_losses,make,fuel_type,aspiration,num_of_doors,body_style,drive_wheels,engine_location,wheel_base,length,width,height,curb_weight,engine_type,num_of_cylinders,engine_size,fuel_system,bore,stroke,compression_ratio,horsepower,peak_rpm,city_mpg,highway_mpg)
    result = auto_obj.get_predicted_price()
    print("Predcited price>>.",result)