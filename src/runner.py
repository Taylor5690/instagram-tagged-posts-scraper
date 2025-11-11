thonimport json
from extractors.instagram_parser import InstagramParser
from outputs.exporters import Exporter

def run_scraper():
    # Load configuration
    with open('src/config/settings.example.json', 'r') as f:
        settings = json.load(f)

    # Create scraper instance
    scraper = InstagramParser(settings['usernames'], settings['max_posts'])
    data = scraper.scrape()

    # Export the data
    exporter = Exporter('data/sample_output.json')
    exporter.export(data)

if __name__ == "__main__":
    run_scraper()