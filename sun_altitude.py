# Outputs sun elevation for a given geographical position and date range

import argparse
from datetime import datetime, timedelta
from pysolar import solar

def valid_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d")
    except ValueError:
        message = "Invalid date representation: '%s'" % s
        raise argparse.ArgumentTypeError(message)

# Prepare arguments for command line invocation
parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-x", "--lon", action="store", help="Longitude of the geographical position in decimal degrees", dest="lon", required=True, type=float)
parser.add_argument("-y", "--lat", action="store", help="Latitude of the geographical position in decimal degress", dest="lat", required=True, type=float)
#parser.add_argument("-z", "--elev", action="store", help="Elevation in meters", dest="elevation", required=True, type=float)
parser.add_argument("-s", "--start", action="store", help="The first date of the interval", dest="start", required=True, type=valid_date)
parser.add_argument("-e", "--end", action="store", help="The last date for the interval", dest="end", required=True, type=valid_date)

args = parser.parse_args()
hour = timedelta(hours=1)
date = args.start

while date < args.end:
    sun_elev = solar.get_altitude(args.lat, args.lon, date)
    print("%s, %f"  % (date, sun_elev))
    date = date + hour
