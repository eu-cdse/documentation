import json
from IPython.display import display, Markdown, Latex,HTML
from tabulate import tabulate

def main(c):
    constellation = c["constellation"]
    cases = {
        "SMOS": SMOSOffer,
        "Landsat": Landsat
    }
    AvailabilityTable = cases.get(constellation, general)(c)
    return AvailabilityTable


def general(c):
    tabletitle = "Offered Data"
    
    try: 
        data_offer = len(c['summaries']['DataAvailability'])
        t = []
        note = ""
        empty_columns = []  # Track empty columns

        for i in range(0, data_offer):
            try:
                Status = c['summaries']['DataAvailability'][i]['Archive_status']
            except:
                Status = ''
            try:
                Access = c['summaries']['DataAvailability'][i]['Access_type']
            except:
                Access = ''
            try:
                Spatial = c['summaries']['DataAvailability'][i]['Spatial']
            except:
                Spatial = ''
            try:
                Temporal = c['summaries']['DataAvailability'][i]['Temporal']
            except:
                Temporal = ''
            try:
                From = c['summaries']['DataAvailability'][i]['Availabilty']
            except:
                From = ''
            try:
                footnotes = c['summaries']['DataAvailability'][i]['Note']
            except:
                footnotes = ''
            try:
                offered_type = c['summaries']['DataAvailability'][i]['offered_type']
            except:
                offered_type = ''

            if offered_type != '':
                t.append([offered_type, Status, Access, Spatial, Temporal, From])
                note += footnotes
                headers = ["Timeliness","Archive Status", "Access Type", "Spatial Extent", "Temporal Extent", "Available in Ecosystem from"]
            else:
                t.append([Status, Access, Spatial, Temporal, From])
                note += footnotes
                headers = ["Archive Status", "Access Type", "Spatial Extent", "Temporal Extent", "Available in Ecosystem from"]

        # Find empty columns
        for j in range(len(t[0])):
            column_values = [row[j] for row in t]
            if all(value == '' for value in column_values):
                empty_columns.append(j)

        # Remove empty columns
        
        headers = [header for i, header in enumerate(headers) if i not in empty_columns]
        t = [[row[i] for i in range(len(headers))] for row in t]

        table = tabulate(t, headers=headers, tablefmt='html', floatfmt=".4f", stralign="center", numalign="center")
        # Set the minimum width of each column to 100 pixels
        table = table.replace("<table>", '<table class="table">')
        table = f"""<h5>{tabletitle}</h5>{table}{note}"""
    except:
        table = " "
    
    return table


def SMOSOffer(c):
    tabletitle = "Offered Data"
    
    try: 
        data_offer = len(c['summaries']['DataAvailability'])
        t = []
        note = ""
        empty_columns = []  # Track empty columns

        for i in range(0, data_offer):
            try:
                Status = c['summaries']['DataAvailability'][i]['Archive_status']
            except:
                Status = ''
            try:
                Access = c['summaries']['DataAvailability'][i]['Access_type']
            except:
                Access = ''
            try:
                Spatial = c['summaries']['DataAvailability'][i]['Spatial']
            except:
                Spatial = ''
            try:
                Temporal = c['summaries']['DataAvailability'][i]['Temporal']
            except:
                Temporal = ''
            try:
                From = c['summaries']['DataAvailability'][i]['Availabilty']
            except:
                From = ''
            try:
                footnotes = c['summaries']['DataAvailability'][i]['Note']
            except:
                footnotes = ''
            try:
                offered_type = c['summaries']['DataAvailability'][i]['offered_type']
            except:
                offered_type = ''

            if offered_type != '':
                t.append([offered_type, Status, Access, Spatial, Temporal, From])
                note += footnotes
                headers = ["Timeliness","Archive Status", "Access Type", "Spatial Extent", "Temporal Extent", "Available in Ecosystem from"]
            else:
                t.append([Status, Access, Spatial, Temporal, From])
                note += footnotes
                headers = ["Archive Status", "Access Type", "Spatial Extent", "Temporal Extent", "Available in Ecosystem from"]

        # Find empty columns
        for j in range(len(t[0])):
            column_values = [row[j] for row in t]
            if all(value == '' for value in column_values):
                empty_columns.append(j)

        # Remove empty columns
        
        headers = [header for i, header in enumerate(headers) if i not in empty_columns]
        t = [[row[i] for i in range(len(headers))] for row in t]

        table = tabulate(t, headers=headers, tablefmt='html', floatfmt=".4f", stralign="center", numalign="center")
        # Set the minimum width of each column to 100 pixels
        table = table.replace("<table>", '<table class="table">')
        table = f"""<h5>{tabletitle}</h5>{table}{note}"""
    except:
        table = " "
    
    return table
    

def Landsat(c):
    print("I will print a table")