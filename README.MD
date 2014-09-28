PNR Predictor
=============

Rest API based PNR predictor

How to use
----------

First restore the database dump to your mongodb

mongorestore -d pnr -c prediction path/to/prediction.bson
mongorestore -d pnr -c pnr_change path/to/pnr_change.bson

Use virtual env

activate it

pip install cherrypy pymongo numpy scipy

python server.py

open web browser and run