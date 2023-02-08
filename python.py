#! /usr/bin/python
from dynatrace import Dynatrace
import csv
import os

# Set these via
# export DT_BASE_URL="http://[YOUR-TENANT].live.dynatrace.com"
# export DT_API_TOKEN="[YOUR-TOKEN]"

dt = Dynatrace(
    os.getenv("DT_BASE_URL"),
    os.getenv("DT_API_TOKEN")
)

# adjust as required
#problems = dt.problems.list(time_from="now-30m",problem_selector='status("closed")')
#problems = dt.problems.list(time_from="now-180d",problem_selector='status("closed"),managementZoneIds("mZId-1", "mzId-2")')
#problems = dt.problems.list(time_from="now-30m") #,entity_selector='type("CUSTOM_DEVICE")')
problems = dt.problems.list(time_from="now-120m",problem_selector='affectedEntityTypes("CUSTOM_DEVICE")')

with open('problems.csv', 'w') as file:
  # create the csv writer
  writer = csv.writer(file)
  file.write("problem, title, status, impact_level, severity_level, start_time, end_time\n")

  if not problems:
    print("No problems found")
    quit()

  includedTags = ["tag1","tag2"]
  for problem in problems:
    # adjust as required
    file.write("{},{},{},{},{},{},{}\n".format(
    problem.display_id, \
    problem.title,\
    str(problem.status).partition(".")[2],\
    str(problem.impact_level).partition(".")[2],\
    str(problem.severity_level).partition(".")[2],\
    problem.start_time.strftime("%m/%d/%Y"),\
    problem.end_time.strftime("%m/%d/%Y")))

  file.close()

