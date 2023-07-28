import json

# Save API response JSON to files for debugging.
class Files:

    @staticmethod
    def save_as_json(data, filename):
        """Save data to a json file with preferred name.

        Params:
            data:       the json data to write
            filename:   desired name for the file (ex. data.json)
        """

        with open(filename, "w") as outfile:
            json.dump(data, outfile)