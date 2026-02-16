# � Evolve Mera Lead Generation Tool

An automated lead scanner for identifying property owners through Airbnb host profiles.

## Features

✨ **Smart Lead Scanning** - Analyzes host bios for ownership indicators
📍 **Geolocation Mapping** - Extracts precise property addresses and coordinates
🗺️ **Google Maps Integration** - Direct links to property locations
📊 **Data Export** - Download leads as CSV or Excel
⚡ **Async Processing** - Fast, efficient multi-threaded scanning

## Requirements

- Python 3.8+
- Playwright (with Chromium browser)
- Pandas for data processing
- Geopy for geocoding

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/merarichardson-create/evolve-mera-lead-tool.git
   cd evolve-mera-lead-tool
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Install Playwright browser
   ```bash
   playwright install chromium
   ```

## Usage

Run the Streamlit app:
```bash
streamlit run streamlit_app.py
```

The app will open in your browser. Enter Airbnb host profile URLs and click "Scan Leads" to begin.

### How It Works

1. **Input URLs** - Paste Airbnb host profile links
2. **Bio Scanning** - Checks for ownership keywords
3. **Property Detection** - Extracts associated property listings
4. **Location Mapping** - Identifies exact addresses via geolocation
5. **Export Results** - Download lead data in your preferred format

## Example URLs

```
https://www.airbnb.com/users/show/123456789
https://www.airbnb.com/users/show/987654321
```

## Keywords Detected

The scanner identifies owners based on these keywords in their bio:
- "my home", "our home", "owner", "we own", "my villa", "my business", "local", "own and operate"

## License

See LICENSE file for details.
