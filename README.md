# GPlaces-Scraper
![GAPS](https://raw.githubusercontent.com/FrintoSec/gplaces-scraper/master/image/gplaces.png)

**Web Scraper for the Google Places API written in Python 3**

## Installation

```git clone https://github.com/Frint0/gplaces-scraper.git```

## Configuration

*You must have a Google Places API key to use this Web Scraper!*

```
cd gplaces-scraper
echo YOUR_API_KEY_HERE > key.txt
```

## Requirements

If you will be running the scraper from the source code directly, **python-google-places** is required:

```pip3 install python-google-places```

## Usage 

For each location provided, the scraper will *try* to weed out 40 different places and dump their according contact info into a CSV file:

```
./gscraper {Your Keyword Goes Here}
```

or 

```
python3 gscraper.py {Your Keyword Goes Here}
```

**YOU CAN ONLY USE A SINGLE KEYWORD, NO SPACES ALLOWED!**

## Screenshot

![Screenshot](https://raw.githubusercontent.com/FrintoSec/gplaces-scraper/master/image/screenshot.png)
