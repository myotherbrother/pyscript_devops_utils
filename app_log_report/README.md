# app_log_report process

### app_log_report.py

This script opens and searches for "INFO" and "ERROR" through ./data/syslog.log
then generates ./data/error_message.csv and ./data/user_statistics.csv.

### csv_to_html.py

This script generates html reports from ./data/error_message.csv and
./data/user_statistics.csv
