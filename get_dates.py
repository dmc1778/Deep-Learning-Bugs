
from datetime import date
import pandas as pd
import os, json
import requests as r
from selenium import webdriver
from bs4 import BeautifulSoup as soup
import csv

token = os.getenv('GITHUB_TOKEN', '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')
driver = webdriver.Firefox(executable_path= r"D:\\applications\\geckodriver")

def write_to_csv(paper_list, filename):
  with open(filename+".csv", "a", newline="") as f:
      writer = csv.writer(f, dialect='excel', delimiter='\n')
      writer.writerow(paper_list)


def main():
    new_col = []
    # data = pd.read_csv('date.csv', sep=',')
    with open('date.csv') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        for i, d in enumerate(data):
            content = r.get(d[0])
            page_soup = soup(content.text, "html.parser")
            try:
                sdate = page_soup.contents[3].contents[3].contents[9].contents[1].contents[1].contents[5].contents[1].contents[5].contents[11].contents[3].contents[5]
                sdate_str = sdate.contents[0].split(" ")
                print("Req status {}: Row {}: Commit {}".format(content.status_code, i, d[0]))
                if len(sdate_str) == 1:
                    new_col.append('could not get date!')
                if len(sdate_str) == 3:
                    sdate_str[1] = sdate_str[1].replace(",","")
                    if sdate_str[0] == 'Jan':
                        new_col.append(sdate_str[1]+"/"+"1"+"/"+sdate_str[2])
                    if sdate_str[0] == 'Feb':
                        new_col.append(sdate_str[1]+"/"+"2"+"/"+sdate_str[2])
                    if sdate_str[0] == 'Mar':
                        new_col.append(sdate_str[1]+"/"+"3"+"/"+sdate_str[2])
                    if sdate_str[0] == 'Apr':
                        new_col.append(sdate_str[1]+"/"+"4"+"/"+sdate_str[2])
                    if sdate_str[0] == 'May':
                        new_col.append(sdate_str[1]+"/"+"5"+"/"+sdate_str[2])
                    if sdate_str[0] == 'Jun':
                        new_col.append(sdate_str[1]+"/"+"6"+"/"+sdate_str[2])
                    if sdate_str[0] == 'Jul':
                        new_col.append(sdate_str[1]+"/"+"7"+"/"+sdate_str[2])
                    if sdate_str[0] == 'Aug':
                        new_col.append(sdate_str[1]+"/"+"8"+"/"+sdate_str[2])
                    if sdate_str[0] == 'Sep':
                        new_col.append(sdate_str[1]+"/"+"9"+"/"+sdate_str[2])
                    if sdate_str[0] == 'Oct':
                        new_col.append(sdate_str[1]+"/"+"10"+"/"+sdate_str[2])
                    if sdate_str[0] == 'Nov':
                        new_col.append(sdate_str[1]+"/"+"11"+"/"+sdate_str[2])
                    if sdate_str[0] == 'Dec':
                        new_col.append(sdate_str[1]+"/"+"12"+"/"+sdate_str[2])
                if len(sdate_str) == 2:
                    if sdate_str[0] == 'Jan':
                        new_col.append(sdate_str[1]+"/"+"1"+"/"+"2021")
                    if sdate_str[0] == 'Feb':
                        new_col.append(sdate_str[1]+"/"+"2"+"/"+"2021")
                    if sdate_str[0] == 'Mar':
                        new_col.append(sdate_str[1]+"/"+"3"+"/"+"2021")
                    if sdate_str[0] == 'Apr':
                        new_col.append(sdate_str[1]+"/"+"4"+"/"+"2021")
                    if sdate_str[0] == 'May':
                        new_col.append(sdate_str[1]+"/"+"5"+"/"+"2021")
                    if sdate_str[0] == 'Jun':
                        new_col.append(sdate_str[1]+"/"+"6"+"/"+"2021")
                    if sdate_str[0] == 'Jul':
                        new_col.append(sdate_str[1]+"/"+"7"+"/"+"2021")
                    if sdate_str[0] == 'Aug':
                        new_col.append(sdate_str[1]+"/"+"8"+"/"+"2021")
                    if sdate_str[0] == 'Sep':
                        new_col.append(sdate_str[1]+"/"+"9"+"/"+"2021")
                    if sdate_str[0] == 'Oct':
                        new_col.append(sdate_str[1]+"/"+"10"+"/"+"2021")
                    if sdate_str[0] == 'Nov':
                        new_col.append(sdate_str[1]+"/"+"11"+"/"+"2021")
                    if sdate_str[0] == 'Dec':
                        new_col.append(sdate_str[1]+"/"+"12"+"/"+"2021")
            except:
                print("got error")
                new_col.append('could not get date!')

            write_to_csv(new_col, 'output')
            new_col = []
if __name__ == "__main__":
    main()
