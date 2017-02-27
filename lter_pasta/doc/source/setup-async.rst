Configure the PASTA-GMN Adapter asynchronous process
====================================================

PASTA-GMN Adapter consists of two main parts; a web service that accepts
notifications of new packages and queues them, and an asynchronous process that
processes the queue.

The asynchronous process is implemented as a Django management command that
is launched at regular intervals by :term:`cron`. The management command
examines the queue and process the requests.

Set up cron job
~~~~~~~~~~~~~~~

  Edit the cron table for the gmn user::

    $ su gmn
    $ crontab -e

  Add::

    # Process the PASTA-GMN Adapter queue.
    0 * * * * cd /var/local/dataone/pasta_gmn_adapter && /var/local/dataone/gmn/bin/python ./manage.py process_population_queue >>pasta_gmn_adapter.log 2>&1

  This sets the processes to run every hour. To modify the schedule, consult
  the crontab manual::

    $ man 5 crontab
