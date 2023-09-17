from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
import csv
from time import sleep

def load_avro_schema_file(key_file, value_file):
    key_schema = avro.load(key_file)
    value_schema = avro.load(value_file)
    return key_schema, value_schema

def send_record():
    key_schema, value_schema = load_avro_schema_file(key_file, value_file)
    