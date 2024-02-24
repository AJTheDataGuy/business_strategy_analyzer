"""Module to control which spiders to run
Can be modified to scrape any site.

Spiders are currently set to run in series
due to resource constraints on my laptop
but can be set to run in parallel in the future
"""
from spiders import web_spider

def main():
    web_spider.run_spider(root_site=r"https://www.alintaenergy.com.au/"
                          ,pen_depth=2)

if __name__ == "__main__":
    main()