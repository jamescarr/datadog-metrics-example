import os
import click
import time

from datadog import initialize, api

options = {
    'api_key': os.environ.get('DD_API_KEY')
}


@click.command()
def submit():
    initialize(**options)

    now = time.time()
    future_10s = now + 10

    # Submit a single point with a timestamp of `now`
    api.Metric.send(metric='page.views', points=1000)

    # Submit a point with a timestamp (must be current)
    api.Metric.send(metric='my.pair', points=(now, 15))


