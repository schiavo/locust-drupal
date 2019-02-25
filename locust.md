# **Running locust tests**

## With client

locust --host=http://vagovcms.lndo.site

## From command line

locust -f locustfile.py --host="http://vagovcms.lndo.site/" --no-web -c 1000 -r 100 --run-time 1h30m
