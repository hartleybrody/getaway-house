import csv
import json

import requests

geocoded_lakes = []

def main():
    data_file_path_prefix = "/Users/hartley/Dropbox/ml/getaway-house/data/"
    input_file_names = "lakes.json"
    output_file_name = "lakes_geocoded.csv"


    file_path = "{}{}".format(data_file_path_prefix, input_file_names)
    with open(file_path, "r") as f:
        lakes = json.load(f)

        for lake in lakes:
            r = requests.get("https://maps.googleapis.com/maps/api/geocode/json", params=dict(
                address="{}, {}".format(lake["name"], lake["town"])
            ))

            j = r.json()
            location = j["results"][0]["geometry"]["location"]

            lake["location"] = location
            geocoded_lakes.append(lake)


    file_path = "{}{}".format(data_file_path_prefix, output_file_name)
    with open(file_path, "w") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "size", "lat", "lng"])
        for l in geocoded_lakes:
            writer.writerow([l["name"], l["size (acres)"], l["location"]["lat"], l["location"]["lng"]])

if __name__ == '__main__':
    main()