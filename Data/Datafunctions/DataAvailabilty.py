import json
from IPython.display import display, Markdown, Latex,HTML
from tabulate import tabulate
from bs4 import BeautifulSoup
import pandas as pd


tabletitle = "Offered Data"

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
        "CLMS": CLMSOffer,               
        "CMEMS" : CMEMSOffer               
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

######################## FUNCTION TO REMOVE EMPTY COLUMNS #######################
def removeempty(t,headers):
    empty_columns=[]
    for j in range(len(t[0])):
        column_values = [row[j] for row in t]
        if all(value == '' for value in column_values):
            empty_columns.append(j)
    # print(empty_columns)
    if empty_columns:

        # Remove empty columns
        t= [[row[i] for i,_ in enumerate(headers) if i not in empty_columns for row in t]]
        headers = [header for i, header in enumerate(headers) if i not in empty_columns]
        return t,headers
    else:
        return t,headers
    
############################ FETCH THE DATA AVAILABILITY DETAILS EXCEPT FOR CLMS AND CMEMS####################################

def DataFetch(c,i):
    try:
        Type = c['summaries']['DataAvailability'][i]['Product']
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
        Catalogue = c['summaries']['DataAvailability'][i]['Catalogue']
    except:
        Catalogue = ''
    try:
        footnotes = c['summaries']['DataAvailability'][i]['Note']
    except:
        footnotes = ''
    try:
        Provider = c['summaries']['DataAvailability'][i]['Provider']
    except:
        Provider = ''
    try:
        Satellite = c['summaries']['DataAvailability'][i]['Satellite']
    except:
        Satellite = ''
    try:
        Resolution = c['summaries']['DataAvailability'][i]['Resolution']
    except:
        Resolution = ''



    return Type,Status,Access,Product_type,SpecificProduct,Spatial,Temporal,ProductLink,Catalogue,footnotes,Provider,Satellite,Resolution

################## DEFINE GENERAL FUNCTION TO CREATE DATA AVAILABILITY TABLE for Copernicus Missions########################
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

        # Find empty columns and remove them
        t,headers=removeempty(t,headers)

        table = tabulate(t, headers=headers, tablefmt='html', floatfmt=".4f", stralign="left", numalign="left")
        # Set the minimum width of each column to 100 pixels
        table = table.replace("<table>", '<table class="table">')
        table = f"""<h6>{tabletitle}</h6>{table}{note}"""
    except:
        table = " "
    
    return table

########################### DEFINE FUNCTION TO CREATE DATA AVAILABILITY TABLE FOR SMOS, LANDSAT AND MERIS ########################

def ComplementaryOffer(c):
    
    try: 
        data_offer = len(c['summaries']['DataAvailability'])
        t = []
        note = ""
        empty_columns = []  # Track empty columns

        for i in range(0, data_offer):
            Type,Status,Access,Product_type,SpecificProduct,Spatial,Temporal,ProductLink,Catalogue,footnotes,Provider,Satellite,Resolution = DataFetch(c,i)
            t.append([Type,Status, Access, Spatial, Temporal,Catalogue])
            note += footnotes
            headers = ["Product","Archive Status", "Access Type", "Spatial Extent", "Temporal Extent","Catalogue"]

        # Find and remove empty columns
        t,headers=removeempty(t,headers)

        table = tabulate(t, headers=headers, tablefmt='html', floatfmt=".4f", stralign="left", numalign="left")
        # Set the minimum width of each column to 100 pixels
        table = table.replace("<table>", '<table class="table">')
        table = f"""<h6>{tabletitle}</h6>{table}{note}"""
    except:
        table = " "
    
    return table


########################## DEFINE FUNCTION TO CREATE DATA AVAILABILITY TABLE FOR ADDITIONAL ########################
def Additional(c):
    
    try: 
        data_offer = len(c['summaries']['DataAvailability'])
        t = []
        note = ""
        empty_columns = []  # Track empty columns

        for i in range(0, data_offer):
            Type,Status,Access,Product_type,SpecificProduct,Spatial,Temporal,ProductLink,Catalogue,footnotes,Provider,Satellite,Resolution = DataFetch(c,i)
            t.append([SpecificProduct, Spatial, Temporal,Catalogue])
            note += footnotes
            headers = ["Specific Products", "Spatial Extext","Temporal Extent","Catalogue"]

        # Find and remove empty columns
        t,headers=removeempty(t,headers)

        table = tabulate(t, headers=headers, tablefmt='html', floatfmt=".4f", stralign="left", numalign="left")
        # Set the minimum width of each column to 100 pixels
        table = table.replace("<table>", '<table class="table">')
        # call the merge cell function
        table=mergecells(table)
        table = f"""<h6>{tabletitle}</h6>{table}{note}"""
    except:
        table = " "
    
    return table

########################## DEFINE FUNCTION TO CREATE DATA AVAILABILITY TABLE FOR CAMS ########################
def CAMSOffer(c):    
    try: 
        data_offer = len(c['summaries']['DataAvailability'])
        t = []
        note = ""
        empty_columns = []  # Track empty columns

        for i in range(0, data_offer): 
            Type,Status,Access,Product_type,SpecificProduct,Spatial,Temporal,ProductLink,Catalogue,footnotes,Provider,Satellite,Resolution = DataFetch(c,i)
            t.append([Product_type, SpecificProduct, Spatial, Temporal, Catalogue,ProductLink])
            note += footnotes
            headers = ["Product Type", "Specific Products", "Spatial Extext","Temporal Extent","Catalogue","Product Detail"]

        # Find and remove empty columns
        t,headers=removeempty(t,headers)

        table = tabulate(t, headers=headers, tablefmt='html', floatfmt=".4f", stralign="left", numalign="left")
        # Set the minimum width of each column to 100 pixels
        table = table.replace("<table>", '<table class="table">')
        table = f"""<h6>{tabletitle}</h6>{table}{note}"""
    except:
        table = " "
    
    return table


########################## DEFINE FUNCTION TO CREATE DATA AVAILABILITY TABLE FOR VHR ########################
def VHROffer(c):
    
    try: 
        data_offer = len(c['summaries']['DataAvailability'])
        t = []
        note = ""
        empty_columns = []  # Track empty columns

        for i in range(0, data_offer):
            Type,Status,Access,Product_type,SpecificProduct,Spatial,Temporal,ProductLink,Catalogue,footnotes,Provider,Satellite,Resolution = DataFetch(c,i)

            t.append([Provider, Satellite, Product_type, Resolution, Access])
            note += footnotes
            headers = ["Dataset provider ","Satellite constellation", "Product Type", "Spatial Resolution ", "Type of Access"]

        # Find and remove empty columns
        t,headers=removeempty(t,headers)
        
        table = tabulate(t, headers=headers, tablefmt='html', floatfmt=".4f", stralign="left", numalign="left")
        # Set the minimum width of each column to 100 pixels
        table = table.replace("<table>", '<table class="table">')
        ###################### merge the table content into a merged table #####################
        table=mergecells(table)
        ###################### end merging the content into a merged table #####################
        table = f"""<h6>{tabletitle}</h6>{table}{note}"""
    except:
        table = " "
    return table

###################### FUNCTION TEST FOR CMEMS ######################
def CMEMSOffer(c):
    tables=""
    try:
        note = ""
        #first find the unique product ids
        df=pd.DataFrame.from_records(c['summaries']['DataAvailability'])
        product_ids=df.ProductID.unique().tolist()
        counts=dict(df.ProductID.value_counts())
        k=0
        for product_id in  product_ids:
            headers = ["Product Type", "Specific Products","Temporal Extent","Catalogue","Product Detail"]
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
                try:
                    Catalogue = c['summaries']['DataAvailability'][i-1]['Catalogue']
                except:
                    Catalogue = ''

                t.append([Product_type, SpecificProduct, Temporal,Catalogue, ProductLink])
                note += footnotes
                
            # Find and remove empty columns
            t,headers=removeempty(t,headers)

            table = tabulate(t, headers=headers, tablefmt='html', floatfmt=".4f", stralign="left", numalign="left")
            # Set the minimum width of each column to 100 pixels
            table = table.replace("<table>", '<table class="table">')
            table=mergecells(table)
            table = f"""<h6>{product_id}</h6>{table}"""
            tables=tables+table
            del t 
            del headers
            # break
        # print(tables)
        tablertn = f"""<h6>{tabletitle}</h6>{tables}{note}"""
    except:
        tablertn = " "
    
    return tablertn


########################## DEFINE FUNCTION TO CREATE DATA AVAILABILITY TABLE FOR CLMS ########################
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
                    Product = c['summaries']['DataAvailability'][i-1]['Product']
                except:
                    Product = ''
                try:
                    Subproduct = c['summaries']['DataAvailability'][i-1]['Sub-product']
                except:
                    Subproduct = ''
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
                try:
                    Catalogue = c['summaries']['DataAvailability'][i-1]['Catalogue']
                except:
                    Catalogue = ''

                if product_id == "HIGH RESOLUTION LAYERS (HRL)":
                    t.append([Product_type, Product,Subproduct,SpecificProduct,Catalogue,ProductLink])
                    headers = ["Product Type", "Products","Sub-Product","Specific Products","Catalogue","Product Detail"]
                    note += footnotes
                elif product_id == "RELATED PAN-EUROPEAN":
                    t.append([Product_type, Product,SpecificProduct,Spatial,Catalogue,ProductLink])
                    headers = ["Product Type", "Products","Specific Products","Spatial","Catalogue","Product Detail"]
                    note += footnotes
                elif product_id == "Local":
                    t.append([Product_type, SpecificProduct, Subproduct,Spatial,Catalogue, ProductLink])
                    headers = ["Product Type", "Products","Specific Products","Spatial","Catalogue","Product Detail"]
                    note += footnotes
                else:
                    t.append([Product_type, SpecificProduct, Spatial, Temporal,Catalogue, ProductLink])
                    headers = ["Product Type", "Specific Products", "Spatial Extext","Temporal Extent","Catalogue","Product Detail"]
                    note += footnotes
                
            # Find and remove empty columns
            t,headers=removeempty(t,headers)

            table = tabulate(t, headers=headers, tablefmt='html', floatfmt=".4f", stralign="left", numalign="left")
            # Set the minimum width of each column to 100 pixels
            table = table.replace("<table>", '<table class="table">')
            table=mergecells(table)
            table = f"""<h6>{product_id}</h6>{table}"""
            tables=tables+table
            del t 
            del headers
            # break
        # print(tables)
        tablertn = f"""<h6>{tabletitle}</h6>{tables}{note}"""
    except:
        tablertn = " "
    
    return tablertn

