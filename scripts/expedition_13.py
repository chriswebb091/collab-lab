import csv, json, sys
def csv_to_json(path):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    return json.dumps(rows, indent=2)
if __name__ == "__main__":
    print(csv_to_json(sys.argv[1]))
