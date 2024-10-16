import yaml
import argparse
import os
from dotenv import load_dotenv

from core.insights import get_insights

# Load environment variables from .env file
load_dotenv()

def main():
    """
    The main context.
    """
    parser = argparse.ArgumentParser(
        description='API Key'
    )
    required_named = parser.add_argument_group('mandatory arguments')
    required_named.add_argument(
        "-k",
        "--key",
        dest="apikey",
        help="Send API Key"
    )
    required_named.add_argument(
        "-b",
        "--bucket",
        dest="bucket",
        help="Influx Bucket name"
    )
    required_named.add_argument(
        "-i",
        "--influxkey",
        dest="influxkey",
        help="Send Influx API Key"
    )
    required_named.add_argument(
        "-u",
        "--influxurl",
        dest="influxurl",
        help="Send Influx Cloud URL"
    )
    required_named.add_argument(
        "-o",
        "--influxorg",
        dest="influxorg",
        help="Send Influx Org"
    )
    args = parser.parse_args()
    key = args.apikey # os.getenv('PAGE_SPEED_API_KEY') #
    bucket = args.bucket # os.getenv('INFLUX_BUCKET_NAME') #
    influxkey = args.influxkey # os.getenv('INFLUX_API_KEY') #
    influxurl = args.influxurl # os.getenv('INFLUX_URL') #
    influxorg = args.influxorg # os.getenv('INFLUX_ORG') #

    with open('urls.yaml') as url:
        url = yaml.safe_load(url)
        for site in url['Websites']:
            get_insights(site, key, bucket, influxkey, influxurl, influxorg)


if __name__ == "__main__":
    main()
