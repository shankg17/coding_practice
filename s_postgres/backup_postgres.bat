@echo off
REM --- PostgreSQL credentials ---
set PGPASSWORD=1618

REM --- Backup folder ---
set BACKUP_PATH=C:\Users\array\OneDrive\Documents\Programming\sql_projects\PostgresBackups

REM --- Base filename ---
set BASE_NAME=db_backup
set EXTENSION=.dump

REM --- Initialize counter ---
set /a COUNT=0

:find_filename
set /a COUNT+=1
set BACKUP_FILE=%BACKUP_PATH%\%BASE_NAME%_%COUNT%%EXTENSION%
if exist "%BACKUP_FILE%" goto find_filename

REM --- Run pg_dump with the available filename ---
"C:\Program Files\PostgreSQL\17\bin\pg_dump.exe" -U postgres -d db -Fc -f "%BACKUP_FILE%"

echo Backup complete: %BACKUP_FILE%
pause
