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
        "CMEMS" : CMEMSOffer,
        "CEMS": CEMSOffer               
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
    t_new=[]
    # print(t)
    for j in range(len(t[0])):
        column_values = [row[j] for row in t]
        if all(value == '' for value in column_values):
            empty_columns.append(j)
    # print(empty_columns)
    if empty_columns:
        # Remove empty columns
        for row in t:
            t_temp=[]
            for i,_ in enumerate(headers):
                if i not in empty_columns:
                    t_temp.append(row[i])
            t_new.append(t_temp)
        headers = [header for i, header in enumerate(headers) if i not in empty_columns]
        # print(t_new,headers)
        return t_new,headers
    else:
        return t,headers
    
############################ FETCH THE DATA AVAILABILITY DETAILS EXCEPT FOR CLMS AND CMEMS####################################

def DataFetch(c,i):
    try:
        type = c['summaries']['DataAvailability'][i]['Product']
    except Exception:
        type = ''
    try:
        status = c['summaries']['DataAvailability'][i]['Archive_status']
    except Exception:
        status = ''
    try:
        access = c['summaries']['DataAvailability'][i]['Access_type']
    except Exception:
        access = ''
    try:
        product_type = c['summaries']['DataAvailability'][i]['Product_type']
    except Exception:
        product_type = ''
    try:
        specific_product = c['summaries']['DataAvailability'][i]['SpecificProduct']
    except Exception:
        specific_product = ''
    try:
        spatial = c['summaries']['DataAvailability'][i]['Spatial']
    except Exception:
        spatial = ''
    try:
        temporal = c['summaries']['DataAvailability'][i]['Temporal']
    except Exception:
        temporal = ''
    try:
        product_link = c['summaries']['DataAvailability'][i]['ProductLink']
    except Exception:
        product_link = ''
    try:
        catalogue = c['summaries']['DataAvailability'][i]['Catalogue']
    except Exception:
        catalogue = ''
    try:
        footnotes = c['summaries']['DataAvailability'][i]['Note']
    except Exception:
        footnotes = ''
    try:
        provider = c['summaries']['DataAvailability'][i]['Provider']
    except Exception:
        provider = ''
    try:
        satellite = c['summaries']['DataAvailability'][i]['Satellite']
    except Exception:
        satellite = ''
    try:
        resolution = c['summaries']['DataAvailability'][i]['Resolution']
    except Exception:
        resolution = ''



    return type,status,access,product_type,specific_product,spatial,temporal,product_link,catalogue,footnotes,provider,satellite,resolution

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
                status = c['summaries']['DataAvailability'][i]['Archive_status']
            except Exception:
                status = ''
            try:
                access = c['summaries']['DataAvailability'][i]['Access_type']
            except Exception:
                access = ''
            try:
                spatial = c['summaries']['DataAvailability'][i]['Spatial']
            except Exception:
                spatial = ''
            try:
                temporal = c['summaries']['DataAvailability'][i]['Temporal']
            except Exception:
                temporal = ''
            try:
                available_from = c['summaries']['DataAvailability'][i]['Availabilty']
            except Exception:
                available_from = ''
            try:
                footnotes = c['summaries']['DataAvailability'][i]['Note']
            except Exception:
                footnotes = ''
            try:
                offered_type = c['summaries']['DataAvailability'][i]['offered_type']
            except Exception:
                offered_type = ''
        
            if offered_type != '':
                t.append([offered_type, status, access, spatial, temporal, available_from])
                note += footnotes
                headers = ["Timeliness","Archive Status", "Access Type", "Spatial Extent", "Temporal Extent", "Available in Ecosystem from"]
            else:
                t.append([status, access, spatial, temporal, available_from])
                note += footnotes
                headers = ["Archive Status", "Access Type", "Spatial Extent", "Temporal Extent", "Available in Ecosystem from"]

        # Find empty columns and remove them
        t,headers=removeempty(t,headers)

        table = tabulate(t, headers=headers, tablefmt='html', floatfmt=".4f", stralign="left", numalign="left")
        # Set the minimum width of each column to 100 pixels
        table = table.replace("<table>", '<table class="table">')
        table = f"""<h5>{tabletitle}</h5>{table}{note}"""
    except Exception:
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
            type,status,access,product_type,specific_product,spatial,temporal,product_link,catalogue,footnotes,provider,satellite,resolution = DataFetch(c,i)
            t.append([type,status, access, spatial, temporal,catalogue])
            note += footnotes
            headers = ["Product","Archive Status", "Access Type", "Spatial Extent", "Temporal Extent","Catalogue"]

        # Find and remove empty columns
        t,headers=removeempty(t,headers)

        table = tabulate(t, headers=headers, tablefmt='html', floatfmt=".4f", stralign="left", numalign="left")
        # Set the minimum width of each column to 100 pixels
        table = table.replace("<table>", '<table class="table">')
        table = f"""<h5>{tabletitle}</h5>{table}{note}"""
    except Exception:
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
            type,status,access,product_type,specific_product,spatial,temporal,product_link,catalogue,footnotes,provider,satellite,resolution = DataFetch(c,i)
            t.append([specific_product, spatial, temporal,catalogue])
            note += footnotes
            headers = ["Specific Products", "Spatial Extext","Temporal Extent","Catalogue"]

        # Find and remove empty columns
        t,headers=removeempty(t,headers)

        table = tabulate(t, headers=headers, tablefmt='html', floatfmt=".4f", stralign="left", numalign="left")
        # Set the minimum width of each column to 100 pixels
        table = table.replace("<table>", '<table class="table">')
        # call the merge cell function
        table=mergecells(table)
        table = f"""<h5>{tabletitle}</h5>{table}{note}"""
    except Exception:
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
            type,status,access,product_type,specific_product,spatial,temporal,product_link,catalogue,footnotes,provider,satellite,resolution = DataFetch(c,i)
            t.append([product_type, specific_product, spatial, temporal, catalogue,product_link])
            note += footnotes
            headers = ["Product Type", "Specific Products", "Spatial Extext","Temporal Extent","Catalogue","Product Detail"]

        # Find and remove empty columns
        t,headers=removeempty(t,headers)

        table = tabulate(t, headers=headers, tablefmt='html', floatfmt=".4f", stralign="left", numalign="left")
        # Set the minimum width of each column to 100 pixels
        table = table.replace("<table>", '<table class="table">')
        table = f"""<h5>{tabletitle}</h5>{table}{note}"""
    except Exception:
        table = " "
    
    return table

########################## DEFINE FUNCTION TO CREATE DATA AVAILABILITY TABLE FOR CEMS ########################
def CEMSOffer(c):    
    try: 
        data_offer = len(c['summaries']['DataAvailability'])
        t = []
        note = ""
        empty_columns = []  # Track empty columns

        for i in range(0, data_offer):
            try:
                event_list = c['summaries']['DataAvailability'][i]['Details']
            except:
                event_list = ""
            Type,Status,Access,Product_type,SpecificProduct,Spatial,Temporal,ProductLink,Catalogue,footnotes,Provider,Satellite,Resolution = DataFetch(c,i)
            t.append([Product_type, Catalogue, event_list])
            note += footnotes
            headers = ["Product Type", "Catalogue", "Events"]

        # Find and remove empty columns
        t,headers=removeempty(t,headers)

        table = tabulate(t, headers=headers, tablefmt='html', floatfmt=".4f", stralign="left", numalign="left")
        # Set the minimum width of each column to 100 pixels
        table = table.replace("<table>", '<table class="table">')
        table = f"""<h5>{tabletitle}</h5>{table}{note}"""
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
            type,status,access,product_type,specific_product,spatial,temporal,product_link,catalogue,footnotes,provider,satellite,resolution = DataFetch(c,i)

            t.append([provider, satellite, product_type, resolution, access])
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
        table = f"""<h5>{tabletitle}</h5>{table}{note}"""
    except Exception:
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
            headers = ["Product Type", "Specific Products","Temporal Extent","S3 path","Product Detail"]
            # print(product_id)  
            t = []
            empty_columns = []  # Track empty columns
            for i in range(0, int(counts[product_id])):
                k+=1
                i=k
                try:
                    product_type = c['summaries']['DataAvailability'][i-1]['Product_type']
                except Exception:
                    product_type = ''
                try:
                    specific_product = c['summaries']['DataAvailability'][i-1]['SpecificProduct']
                except Exception:
                    specific_product = ''
                try:
                    temporal = c['summaries']['DataAvailability'][i-1]['Temporal']
                except Exception:
                    temporal = ''
                try:
                    product_link = c['summaries']['DataAvailability'][i-1]['ProductLink']
                except Exception:
                    product_link = ''
                try:
                    footnotes = c['summaries']['DataAvailability'][i-1]['Note']
                except Exception:
                    footnotes = ''
                try:
                    catalogue = c['summaries']['DataAvailability'][i-1]['Catalogue']
                except Exception:
                    catalogue = ''

                t.append([product_type, specific_product, temporal,catalogue, product_link])
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
        tablertn = f"""<h5>{tabletitle}</h5>{tables}{note}"""
    except Exception:
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
                    product_type = c['summaries']['DataAvailability'][i-1]['Product_type']
                except Exception:
                    product_type = ''
                try:
                    specific_product = c['summaries']['DataAvailability'][i-1]['SpecificProduct']
                except Exception:
                    specific_product = ''
                try:
                    product = c['summaries']['DataAvailability'][i-1]['Product']
                except Exception:
                    product = ''
                try:
                    sub_product = c['summaries']['DataAvailability'][i-1]['Sub-product']
                except Exception:
                    sub_product = ''
                try:
                    spatial = c['summaries']['DataAvailability'][i-1]['Spatial']
                except Exception:
                    spatial = ''
                try:
                    temporal = c['summaries']['DataAvailability'][i-1]['Temporal']
                except Exception:
                    temporal = ''
                try:
                    product_link = c['summaries']['DataAvailability'][i-1]['ProductLink']
                except Exception:
                    product_link = ''
                try:
                    footnotes = c['summaries']['DataAvailability'][i-1]['Note']
                except Exception:
                    footnotes = ''
                try:
                    catalogue = c['summaries']['DataAvailability'][i-1]['Catalogue']
                except Exception:
                    catalogue = ''

                if product_id == "HIGH RESOLUTION LAYERS (HRL)":
                    t.append([product_type, product,sub_product,specific_product,catalogue,product_link])
                    headers = ["Product Type", "Products","Sub-Product","Specific Products","S3 path","Product Detail"]
                    note += footnotes
                elif product_id == "RELATED PAN-EUROPEAN":
                    t.append([product_type, product,specific_product,spatial,catalogue,product_link])
                    headers = ["Product Type", "Products","Specific Products","Spatial","S3 path","Product Detail"]
                    note += footnotes
                elif product_id == "Local":
                    t.append([product_type, specific_product, sub_product,spatial,catalogue, product_link])
                    headers = ["Product Type", "Products","Specific Products","Spatial","S3 path","Product Detail"]
                    note += footnotes
                else:
                    t.append([product_type, specific_product, spatial, temporal,catalogue, product_link])
                    headers = ["Product Type", "Specific Products", "Spatial Extext","Temporal Extent","S3 path","Product Detail"]
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
        tablertn = f"""<h5>{tabletitle}</h5>{tables}{note}"""
    except Exception:
        tablertn = " "
    
    return tablertn

