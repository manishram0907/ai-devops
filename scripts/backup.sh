#!/bin/bash

TIMESTAMP=$(date +%F-%H-%M)

docker exec postgres pg_dump -U admin devopsdb > backup-$TIMESTAMP.sql

echo "Backup completed: backup-$TIMESTAMP.sql"