from googleplaces import GooglePlaces, types, lang
import csv
import argparse
import sys

try:
	keyFile = open('key.txt', 'r')
	apikey = keyFile.readline().rstrip()
	google_places = GooglePlaces(apikey)
except FileNotFoundError:
	print("key.txt not found!")
	sys.exit()


parser = argparse.ArgumentParser(description="Google Places API Scraper")
parser.add_argument("keyword", help="keyword for scraping")
args = parser.parse_args()
print("Searching for %s and dumping to list.csv:" % (args.keyword))

def find40(city):
	query_result = google_places.nearby_search(location = city, keyword=args.keyword)

	for place in query_result.places:
		place.get_details()
		name = "Name: " + place.name + " "
		address = " Address: " + str(place.formatted_address) + " "
		number = " Number: " + str(place.local_phone_number) + " "
		rating = " Rating: " + str(place.rating)
		ordered = [name, address, number, rating]
		with open("list.csv", "a") as fp:
			wr = csv.writer(fp, delimiter='|', dialect='excel')
			try:
				wr.writerow(ordered)
			except UnicodeEncodeError:
				print("Emoji in name, not adding to list!")
				pass
		with open("list.csv", "r") as fp:
			reader = csv.reader(fp)
			line_count = sum(1 for line in reader)
			print("Places Found: %s" % (line_count))

	if query_result.has_next_page_token:
		query_result_next_page = google_places.nearby_search(pagetoken=query_result.next_page_token)

		for place in query_result_next_page.places:
			place.get_details()
			name = "Name: " + place.name + " "
			address = " Address: " + str(place.formatted_address) + " "
			number = " Number: " + str(place.local_phone_number) + " "
			rating = " Rating: " + str(place.rating)
			ordered = [name, address, number, rating]
			with open("list.csv", "a") as fp:
				wr = csv.writer(fp, delimiter='|', dialect='excel')
				try:
					wr.writerow(ordered)
				except UnicodeEncodeError:
					print("Emoji in name, not adding to list!")
					pass
			with open("list.csv", "r") as fp:
				reader = csv.reader(fp)
				line_count = sum(1 for line in reader)
			print("Places Found: %s" % (line_count))
try:
	filepath = 'cities.txt'
	with open(filepath) as fp:
		line = fp.readline()
		for line in fp:
			find40(line.strip())
except FileNotFoundError:
	print("City list could not be found, please make sure cities.txt exists and is in your current directory!")
