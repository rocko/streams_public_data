#!/usr/bin/python3

import os, requests, brotli, json
from os.path import exists

if __name__ == "__main__":

    storage_folder = os.path.dirname(os.path.abspath(__file__))

    print(storage_folder)


"""
    json_data_url = "https://data.sensor.community/static/v2/data.json"
    try:
        r = requests.get(json_data_url)  
        if r.status_code == 200:
            json_data = r.content  # Result is a list
    except Exception as e:
        print(e)

    # Create temporary JSON for cleaned version
    cleaned_json_data = []
    
    # Clean JSON data
    for element in json_data:
        cleaned_element = {
            "id": element["id"],
            "ts": element["timestamp"],
            "lat": element["location"]["latitude"],
            "long": element["location"]["longitude"],
            "alt": element["location"]["altitude"],
            "sensordatavalues": {
                "temp": None,
                "pressure": None,
                "pressure_asl": None,
                "humidity": None,
                "dust_p1": None,
                "dust_p2": None
            }
        }
        sensordatavalues = {}
        for l in range(len(element["sensordatavalues"])):
            sensordatavalues[element["sensordatavalues"][l]["value_type"]] = element["sensordatavalues"][l]["value"]

        cleaned_element.update(sensordatavalues=sensordatavalues)                
        cleaned_json_data.append(cleaned_element)
    
    # Encode to JSON
    cleaned_json_data = json.dumps(cleaned_json_data).encode("utf-8")

    compressed_cleaned_json_data = brotli.compress(cleaned_json_data)

    # Save to file: data.json
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.min.json")
    with open(filename, 'wb') as output_file:
        output_file.write(compressed_cleaned_json_data)

    # Push to git
    #os.chdir(os.path.dirname(os.path.abspath(__file__)))
    #os.system("git pull https://github.com/rocko/streams_public_data.git")
    #os.system("git add %s" % filename)
    #os.system("git commit -m 'lol'")
    #os.system("git push https://github.com/rocko/streams_public_data.git")
"""    