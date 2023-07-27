import json

# Save API response JSON to files for debugging.
class Files:

    # Save data to a json file with preferred name.
    @staticmethod
    def save_as_json(data, filename):
        with open(filename, "w") as outfile:
            json.dump(data, outfile)