#!/usr/bin/env python3

import re
import csv
import operator

errors = {}
per_user = {}
logfile = r"./data/syslog.log"
pattern = r"(INFO|ERROR) ([\w' ]+|[\w\[\]#' ]+) (\(\w+\)|\(\w+\.\w+\))$"
file = open(logfile, 'r')

for line in file:
    result = re.search(pattern, line)
    if result is None:
        continue
    if result.groups()[0] == "INFO":
        category = result.groups()[0]
        msg = result.groups()[1]
        user_name = str(result.groups()[2])[1:-1]
        if user_name in per_user:
            user = per_user[user_name]
            user[category] += 1
        else:
            per_user[user_name] = {'INFO':1, 'ERROR':0}
    if result.groups()[0] == "ERROR":
        category = result.groups()[0]
        msg = result.groups()[1]
        user_name = str(result.groups()[2])[1:-1]
        errors[msg] = errors.get(msg, 0) + 1

        if user_name in per_user:
            user = per_user[user_name]
            user[category] += 1
        else:
            per_user[user_name] = {'INFO':0, 'ERROR':1}

errors = sorted(errors.items(), key = operator.itemgetter(1), reverse=True)

per_user = sorted(per_user.items())

file.close()
errors.insert(0, ("Error", "Count"))

with open("./data/error_message.csv", "w") as error_file:
    for error in errors:
        a,b = error
        error_file.write(str(a)+','+str(b)+'\n')

with open("./data/user_statistics.csv", "w") as user_file:
    user_file.write("Username,INFO,ERROR\n")
    for stats in per_user:
        a,b = stats
        user_file.write(str(a)+','+str(b["INFO"])+','+str(b["ERROR"])+'\n')




