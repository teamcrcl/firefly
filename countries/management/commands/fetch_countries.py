import logging
import time
from datetime import timedelta
import requests
import yaml
from django.core.management.base import BaseCommand

from countries.models import Country


class Command(BaseCommand):

    def handle(self, *args, **options):
        logger = logging.getLogger(__name__)

        logger.info('Starting to fetch countries')
        start_time = time.monotonic()
        with open('config/config.yaml', 'r') as stream:
            try:
                conf = yaml.load(stream)
                url = conf['countries']['api']
                logger.info(url)
                response = requests.request('get', url)
                if response.status_code == 200:
                    data = response.json()
                    count = 0
                    for item in data:
                        name = item.get('name')
                        name = name.lower()
                        flag = item.get('flag')
                        if not Country.objects.filter(name=name).exists():
                            country = Country(name=name, flag=flag)
                            country.save()
                            count += 1
                    end_time = time.monotonic()
                    logger.info("Saved {} countries in : {}".format(count, timedelta(seconds=end_time - start_time)))
                    return 0
            except yaml.YAMLError as e:
                return 1, str(e)


