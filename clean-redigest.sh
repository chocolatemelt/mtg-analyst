#!/usr/bin/sh

./kafka_2.12-2.3.0/bin/kafka-topics.sh --zookeeper localhost:2181 --delete --topic mtg
./kafka_2.12-2.3.0/bin/kafka-topics.sh --zookeeper localhost:2181 --create --replication-factor 1 --partitions 1 --topic mtg

for data in ./data/*.json; do
	./franz.py "$data"
done
