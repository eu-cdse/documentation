import json
from IPython.display import display, Markdown, Latex,HTML
from tabulate import tabulate
from bs4 import BeautifulSoup
import pandas as pd

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
        "CAMS": CAMSOffer,
        "CLMS": CLMSOffer,               #NEED FIXING
        "CMEMS" : CMEMSOffer          #NEED FIXING     
    }
    AvailabilityTable = cases.get(constellation, general)(c)
    return AvailabilityTable

###################### DEFINE A FUNCTION TO MERGE TABLES ######################
def mergecells(tabletxt):
    soup = BeautifulSoup(tabletxt, 'html.parser')
    table = soup.find('table')

    header_cell = None

    for row in table.find_all('tr'):
        first_cell = row.find('td')
        
        if header_cell is None or first_cell.get_text() != header_cell.get_text():
            header_cell = first_cell
        else:
            header_cell['rowspan'] = int(header_cell.get('rowspan', 1)) + 1
            first_cell.extract()
    return table

################## DEFINE GENERAL FUNCTION TO CREATE DATA AVAILABILITY TABLE ########################
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

########################### DEFINE FUNCTION TO CREATE DATA AVAILABILITY TABLE FOR SMOS, LANDSAT AND MERIS ########################

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
                footnotes = c['summaries']['DataAvailability'][i]['Note']
            except:
                footnotes = ''

            t.append([Type,Status, Access, Spatial, Temporal])
            note += footnotes
            headers = ["Product Type","Archive Status", "Access Type", "Spatial Extent", "Temporal Extent"]

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


########################## DEFINE FUNCTION TO CREATE DATA AVAILABILITY TABLE FOR ADDITIONAL ########################
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
        # call the merge cell function
        table=mergecells(table)
        table = f"""<h5>{tabletitle}</h5>{table}{note}"""
    except:
        table = " "
    
    return table

########################## DEFINE FUNCTION TO CREATE DATA AVAILABILITY TABLE FOR CAMS ########################
def CAMSOffer(c):
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
            headers = ["Product Type", "Specific Products", "Spatial Extext","Temporal Extent","Product Detail"]

        # Find empty columns
        for j in range(len(t[0])):
            column_values = [row[j] for row in t]
            if all(value == '' for value in column_values):
                empty_columns.append(j)

        # Remove empty columns
        
        headers = [header for i, header in enumerate(headers) if i not in empty_columns]
        t = [[row[i] for i in range(len(headers))] for row in t]

        table = tabulate(t, headers=headers, tablefmt='html', floatfmt=".4f", stralign="left", numalign="left")
        # Set the minimum width of each column to 100 pixels
        table = table.replace("<table>", '<table class="table">')
        table = f"""<h5>{tabletitle}</h5>{table}{note}"""
    except:
        table = " "
    
    return table


########################## DEFINE FUNCTION TO CREATE DATA AVAILABILITY TABLE FOR VHR ########################
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
            headers = ["Dataset provider ","Satellite constellation", "Product Type", "Spatial Resolution ", "Type of Access"]

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
        ###################### merge the table content into a merged table #####################
        table=mergecells(table)
        ###################### end merging the content into a merged table #####################
        table = f"""<h5>{tabletitle}</h5>{table}{note}"""
    except:
        table = " "
    return table

###################### FUNCTION TEST FOR CLMS ######################
def CMEMSOffer(c):
    tabletitle = "Offered Data"
    tables=""
    try:
        note = ""
        #first find the unique product ids
        df=pd.DataFrame.from_records(c['summaries']['DataAvailability'])
        product_ids=df.ProductID.unique().tolist()
        counts=dict(df.ProductID.value_counts())
        k=0
        for product_id in  product_ids:
            headers = ["Product Type", "Specific Products","Temporal Extent","Product Detail"]
            # print(product_id)  
            t = []
            empty_columns = []  # Track empty columns
            for i in range(0, int(counts[product_id])):
                k+=1
                i=k
                try:
                    Product_type = c['summaries']['DataAvailability'][i-1]['Product_type']
                except:
                    Product_type = ''
                try:
                    SpecificProduct = c['summaries']['DataAvailability'][i-1]['SpecificProduct']
                except:
                    SpecificProduct = ''
                try:
                    Spatial = c['summaries']['DataAvailability'][i-1]['Spatial']
                except:
                    Spatial = ''
                try:
                    Temporal = c['summaries']['DataAvailability'][i-1]['Temporal']
                except:
                    Temporal = ''
                try:
                    ProductLink = c['summaries']['DataAvailability'][i-1]['ProductLink']
                except:
                    ProductLink = ''
                try:
                    footnotes = c['summaries']['DataAvailability'][i-1]['Note']
                except:
                    footnotes = ''

                t.append([Product_type, SpecificProduct, Temporal, ProductLink])
                note += footnotes
                
            # Find empty columns
            for j in range(len(t[0])):
                column_values = [row[j] for row in t]
                if all(value == '' for value in column_values):
                    empty_columns.append(j)

            # Remove empty columns
            
            headers = [header for i, header in enumerate(headers) if i not in empty_columns]
            t = [[row[i] for i in range(len(headers))] for row in t]

            table = tabulate(t, headers=headers, tablefmt='html', floatfmt=".4f", stralign="left", numalign="left")
            # Set the minimum width of each column to 100 pixels
            table = table.replace("<table>", '<table class="table">')
            table=mergecells(table)
            table = f"""<h4>{product_id}</h4>{table}"""
            tables=tables+table
            del t 
            del headers
            # break
        # print(tables)
        tablertn = f"""<h5>{tabletitle}</h5>{tables}{note}"""
    except:
        tablertn = " "
    
    return tablertn


########################## DEFINE FUNCTION TO CREATE DATA AVAILABILITY TABLE FOR CMEMS and CLMS ########################
def CLMSOffer(c):
    tabletitle = "Offered Data"
    tables=""
    try:
        note = ""
        #first find the unique product ids
        df=pd.DataFrame.from_records(c['summaries']['DataAvailability'])
        product_ids=df.ProductID.unique().tolist()
        counts=dict(df.ProductID.value_counts())
        k=0
        for product_id in  product_ids:
            headers = ["Product Type", "Specific Products", "Spatial Extext","Temporal Extent","Product Detail"]
            # print(product_id)  
            t = []
            empty_columns = []  # Track empty columns
            for i in range(0, int(counts[product_id])):
                k+=1
                i=k
                try:
                    Product_type = c['summaries']['DataAvailability'][i-1]['Product_type']
                except:
                    Product_type = ''
                try:
                    SpecificProduct = c['summaries']['DataAvailability'][i-1]['SpecificProduct']
                except:
                    SpecificProduct = ''
                try:
                    Spatial = c['summaries']['DataAvailability'][i-1]['Spatial']
                except:
                    Spatial = ''
                try:
                    Temporal = c['summaries']['DataAvailability'][i-1]['Temporal']
                except:
                    Temporal = ''
                try:
                    ProductLink = c['summaries']['DataAvailability'][i-1]['ProductLink']
                except:
                    ProductLink = ''
                try:
                    footnotes = c['summaries']['DataAvailability'][i-1]['Note']
                except:
                    footnotes = ''

                t.append([Product_type, SpecificProduct, Spatial, Temporal, ProductLink])
                note += footnotes
                
            # Find empty columns
            for j in range(len(t[0])):
                column_values = [row[j] for row in t]
                if all(value == '' for value in column_values):
                    empty_columns.append(j)

            # Remove empty columns
            
            headers = [header for i, header in enumerate(headers) if i not in empty_columns]
            t = [[row[i] for i in range(len(headers))] for row in t]

            table = tabulate(t, headers=headers, tablefmt='html', floatfmt=".4f", stralign="left", numalign="left")
            # Set the minimum width of each column to 100 pixels
            table = table.replace("<table>", '<table class="table">')
            table=mergecells(table)
            table = f"""<h4>{product_id}</h4>{table}"""
            tables=tables+table
            del t 
            del headers
            # break
        # print(tables)
        tablertn = f"""<h5>{tabletitle}</h5>{tables}{note}"""
    except:
        tablertn = " "
    
    return tablertn
