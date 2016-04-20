import csv
import urllib2

url = 'http://ir.eia.gov/wpsr/table1.csv'
response = urllib2.urlopen(url)
cr = csv.reader(response)

for row in cr:
    print row
