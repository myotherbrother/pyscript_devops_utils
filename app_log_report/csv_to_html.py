#!/usr/bin/env python3

import sys
import csv
import os

def process_csv(csv_file):
    """Turn the contents of the CSV file into a list of lists"""
    print("Processing {}".format(csv_file))
    with open(csv_file, "r") as datafile:
        data = list(csv.reader(datafile))
    return data

def data_to_html(title, data):
    """Turns a list of lists into a HTML table"""

    #HTML Headers
    html_content = """
<html>
<head>
<style>
table {
    width: 25%
    font-family: arial, sans-serif;
    border-callapse: collapse;
}

tr:nth-child(odd) {
    background-color: #dddddd;


