
import os
import sys
from bs4 import BeautifulSoup
from bs4.diagnose import diagnose

current_file = __file__
current_dir = os.path.dirname(current_file)
file_dir = os.path.join(current_dir + "/python.html")

with open(file_dir,encoding="utf8") as fp: data = fp.read()

output_dir = os.path.join(current_dir + "/diagnostic_report.txt")

#pipe stout to file
sys.stdout = open(output_dir, "w")

result = diagnose(data)
