import json
from IPython.display import display, Markdown, Latex,HTML
from tabulate import tabulate

def main(c):
    constellation = c["constellation"]
    cases = {
        "SMOS": ComplementaryOffer,
        "MERIS": ComplementaryOffer,
        "Landsat-5": ComplementaryOffer,
        "Landsat-7": ComplementaryOffer,
        "Landsat-8": ComplementaryOffer,
        "Commercial data": VHROffer,
        "AdditionalComplementaryData": Additional,
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


def ComplementaryOffer(c):
    tabletitle = "Offered Data"
    
    try: 
        data_offer = len(c['summaries']['DataAvailability'])
        t = []
        note = ""
        empty_columns = []  # Track empty columns

        for i in range(0, data_offer):
            try:
                Type = c['summaries']['DataAvailability'][i]['Product_type']
            except:
                Type = ''
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
                Catalogue = c['summaries']['DataAvailability'][i]['Catalogue']
            except:
                Catalogue = ''
            try:
                footnotes = c['summaries']['DataAvailability'][i]['Note']
            except:
                footnotes = ''

            t.append([Type,Status, Access, Spatial, Temporal, Catalogue])
            note += footnotes
            headers = ["Product Type","Archive Status", "Access Type", "Spatial Extent", "Temporal Extent", "Catalogue"]

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


def VHROffer(c):
    tabletitle = "Offered Data"
    
    try: 
        data_offer = len(c['summaries']['DataAvailability'])
        t = []
        note = ""
        empty_columns = []  # Track empty columns

        for i in range(0, data_offer):
            try:
                Provider = c['summaries']['DataAvailability'][i]['Provider']
            except:
                Provider = ''
            try:
                Satellite = c['summaries']['DataAvailability'][i]['Satellite']
            except:
                Satellite = ''
            try:
                Product_type = c['summaries']['DataAvailability'][i]['Product_type']
            except:
                Product_type = ''
            try:
                Resolution = c['summaries']['DataAvailability'][i]['Resolution']
            except:
                Resolution = ''
            try:
                Access_type = c['summaries']['DataAvailability'][i]['Access_type']
            except:
                Access_type = ''
            try:
                footnotes = c['summaries']['DataAvailability'][i]['Note']
            except:
                footnotes = ''

            t.append([Provider, Satellite, Product_type, Resolution, Access_type])
            note += footnotes
            headers = ["Dataset provider ","Satellite constellation", "Product Type  ", "Spatial Resolution ", "Type of Access"]

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


def Additional(c):
    tabletitle = "Offered Data"
    
    try: 
        data_offer = len(c['summaries']['DataAvailability'])
        t = []
        note = ""
        empty_columns = []  # Track empty columns

        for i in range(0, data_offer):
            try:
                Product_type = c['summaries']['DataAvailability'][i]['Product_type']
            except:
                Product_type = ''
            try:
                SpecificProduct = c['summaries']['DataAvailability'][i]['SpecificProduct']
            except:
                SpecificProduct = ''
            try:
                Spatial = c['summaries']['DataAvailability'][i]['Spatial']
            except:
                Spatial = ''
            try:
                Temporal = c['summaries']['DataAvailability'][i]['Temporal']
            except:
                Temporal = ''
            try:
                ProductLink = c['summaries']['DataAvailability'][i]['ProductLink']
            except:
                ProductLink = ''
            try:
                footnotes = c['summaries']['DataAvailability'][i]['Note']
            except:
                footnotes = ''

            t.append([Product_type, SpecificProduct, Spatial, Temporal, ProductLink])
            note += footnotes
            headers = ["Product Type", "Specific Products", "Spatial Extext","Temporal Extent", "Product Detail"]

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