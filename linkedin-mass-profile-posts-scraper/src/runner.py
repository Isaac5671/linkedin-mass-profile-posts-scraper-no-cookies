thonimport json
import time
from extractors.linkedin_parser import LinkedInParser
from outputs.exporters import Exporter
from extractors.utils_time import convert_time_format

def run_scraper(input_file: str, output_file: str):
    # Load the input profiles list
    with open(input_file, 'r') as file:
        profiles = file.readlines()

    # Initialize LinkedInParser and Exporter
    parser = LinkedInParser()
    exporter = Exporter()

    # Scrape posts from each profile
    scraped_data = []
    for profile in profiles:
        print(f"Scraping data for {profile.strip()}")
        data = parser.scrape_profile(profile.strip())
        scraped_data.append(data)

    # Export data to JSON
    exporter.export_data(scraped_data, output_file)
    print(f"Scraping completed. Data saved to {output_file}")

if __name__ == "__main__":
    input_file = 'data/inputs.sample.txt'
    output_file = 'data/sample.json'
    run_scraper(input_file, output_file)