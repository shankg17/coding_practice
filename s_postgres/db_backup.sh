# shell script to run pg_dump to take periodic db backup
#!/usr/bin/env bash

# to execute - ./db_backup.sh

# ==== CONFIGURATION ====
PGHOST="localhost"
PGPORT="5432"
PGUSER="svm"
PGDATABASE="sdb"
BACKUP_DIR="/Users/svm/Documents/OneDrive/pg_backups"

# If pg_dump is not in PATH, set full path, e.g.:
# PGBIN="/Library/PostgreSQL/16/bin"
# PGPATH="$PGBIN/pg_dump"
PGPATH="pg_dump"

# ==== DO NOT EDIT BELOW THIS LINE ====
mkdir -p "$BACKUP_DIR"

DATESTAMP="$(date +%Y-%m-%d_%H-%M-%S)"

"$PGPATH" \
  -h "$PGHOST" \
  -p "$PGPORT" \
  -U "$PGUSER" \
  -F c \
  -d "$PGDATABASE" \
  -f "$BACKUP_DIR/${PGDATABASE}_${DATESTAMP}.dump"

echo "Backup finished: $BACKUP_DIR/${PGDATABASE}_${DATESTAMP}.dump"
