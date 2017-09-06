import re
import json

lakes = []

def main():
    data_file_path_prefix = "/Users/hartley/Dropbox/ml/getaway-house/data/"
    raw_file_names = [
        "raw_natural_lakes.csv",
        # "raw_articifical_lakes.csv"
    ]
    output_file_name = "lakes.json"

    for raw_file_name in raw_file_names:
        file_path = "{}{}".format(data_file_path_prefix, raw_file_name)
        with open(file_path, "r") as f:
            print "Reading {}".format(raw_file_name)
            for line in f:
                pieces = [p.strip() for p in line.split("\t")]

                size = re.findall(r'([0-9]+) acres', pieces[3])
                size = int(size[0])

                # wrong size
                if size < 50:
                    print "too small: " + pieces[0]
                    continue
                if size > 1000:
                    print "too large: " + pieces[0]
                    continue

                lakes.append({
                    "name": pieces[0],
                    "town": "{}, {}, OH".format(pieces[4], pieces[5]),
                    "size (acres)": size,
                })


    file_path = "{}{}".format(data_file_path_prefix, output_file_name)
    with open(file_path, "w") as f:
        f.write(json.dumps(lakes, indent=2))

if __name__ == '__main__':
    main()