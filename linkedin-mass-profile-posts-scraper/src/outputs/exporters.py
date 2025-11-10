thonimport json

class Exporter:
    def export_data(self, data, output_file: str):
        """Export scraped data to a JSON file"""
        with open(output_file, 'w') as outfile:
            json.dump(data, outfile, indent=4)