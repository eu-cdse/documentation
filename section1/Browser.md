## About the Browser

The Browser is a web browser application that allows you to easily search, visualize, modify and download imagery from the Sentinel satellites. You can access the Browser at:

[https://dataspace.copernicus.eu/browser/](https://dataspace.copernicus.eu/browser/)

Currently you need a free account to use the Browser. To register for a free account, click [here](https://identity.cloudferro.com/auth/realms/CDSE/protocol/openid-connect/auth?client_id=sh-5f8b630b-b083-49ed-b340-b8f01ecb81c4&redirect_uri=https%3A%2F%2Fdataspace.copernicus.eu%2Fbrowser%2FoauthCallback.html&response_type=token&state=) to the browser. A new window will open where you can click on **New user? Click [here](https://identity.cloudferro.com/auth/realms/CDSE/login-actions/registration?client_id=sh-5f8b630b-b083-49ed-b340-b8f01ecb81c4&tab_id=kuySlol9oac) to create an account and access the data**. Once you have created the account, you will automatically be logged in to the Browser. Remember to save your login credentials for the next time you want to log in to the Browser.

![Start Screen](RackMultipart20230119-1-h4ibb1_html_bc15e4ea743ab33.gif)

Fig. 1: Browser start screen

The Browser window is divided into three parts:

1. the sidebar on the left side of the screen. Here you can set the parameters to search for, visualize and download data.
2. the map in the middle of the screen. Here you can zoom in and out and move around to find the place you are interest in. In this area you will see visualized satellite imagery or geometries of the products, that are the result of your search.
3. the toolbar on the right side of the screen. Here you find various tools (e.g., for measuring or downloading images) with which you can work with the data displayed on the map.
## Visualizing data

![Shape2](RackMultipart20230119-1-h4ibb1_html_e5aa10674d73800d.gif) You can find the _VISUALIZE_ tab in the upper left corner of the sidebar (selected by default). The _VISUALIZE_ tab allows you to easily visualize satellite imagery on the map. Change or modify your visualization with just a few clicks.

1.
2.

## 2.1Visualizing data

In order to visualize data on the map, you need to zoom in to your area of interest. You can do this either with the mouse wheel or with the location search in the upper right corner.

Let's try to visualize the latest Sentinel-2 L2A imagery over Italy.

1. Either zoom to Italy with the mouse wheel or type _Italy_ in the search box in the upper right corner.
2. In the sidebar, a maximum cloud coverage of 30% and the product type Sentinel-2 L2A are already preselected. To visualize the latest available data with cloud coverage below 30% click on the _Show latest date_ button.

You can now see the latest data over Italy on the map. Depending on the latest data available you will see data from one or more orbits (stripes of images on the map).

### 2.1.1Modifying and Changing a Visualization

![Shape3](RackMultipart20230119-1-h4ibb1_html_8dc78895de69e561.gif) If you want to improve how the data is displayed on the map, you can modify the visualization by clicking on _Show effects and advanced options_ ( ![](RackMultipart20230119-1-h4ibb1_html_9ef657e62597dd9a.png) ) at the bottom of the sidebar. Change the _Gain_/_Gamma_ values, the values of the _R_/_G_/_B_colour channels, specify which sampling method is used for the visualization (_Layer default, Bilinear, Bicubic, Nearest)_ or click on _Reset_ to reset all changes made. To return to the visualization layers overview, click on _Show visualizations_ ( ![](RackMultipart20230119-1-h4ibb1_html_28948cd2c791cf2e.png)).

To visualize different Sentinel-2 band combinations, either use one of the prepared options from the list of layers (e.g., NDVI for the Normalized Difference Vegetation Index using the Sentinel bands B4 and B8) or click _Custom_ at the bottom of the layers list.

Here you can create a custom _R/G/B_ composite or _Index_ (band ratio, normalized difference index) by dragging and dropping the Sentinel-2 bands into the appropriate circles or use the _Custom script_ functionality to insert a piece of JavaScript code.

### 2.1.2Comparing Visualizations

![Shape4](RackMultipart20230119-1-h4ibb1_html_fe8a6303f821a611.gif) To compare two (or more) visualizations you have to add them to the compare panel. You can add a visualization to the compare panel by clicking on the _Add to compare_ button in each visualization layer (see Fig. 4). When you have added all the layers you want to compare to the compare panel, you can switch to it by clicking on the compare icon ( ![](RackMultipart20230119-1-h4ibb1_html_8c3226fdb6f6fe3e.png) ). In the compare panel you can choose between a _Split_ and an _Opacity_ mode. With the _Split_ mode you can compare two images side by side. With the _Opacity_ mode you can compare two (or more) visualizations on top of each other.

## 2.2Product Search for Current Visualization

![Shape5](RackMultipart20230119-1-h4ibb1_html_abe0ae487ed73e19.gif)
 When you are visualizing data (chapter Visualizing data), you can easily find the products associated with the data you see on the map. The product allows you to inspect the full metadata and easily download the raw data. To find connected products, just click the _Find products for current view_ button in the sidebar (under the _Show latest date_ button).


# Product Search

![Shape6](RackMultipart20230119-1-h4ibb1_html_7dad4744fd2f7b0a.gif) With the product search you can find products from four Sentinel missions (Sentinel-1, Sentinel-2, Sentinel-3, Sentinel-5p) and the sensors on board these satellites (C-SAR, MSI, OLCI, SRAL, SLSTR, SYNERGY). You can explore the metadata for each of those products, download the raw data or visualize the data on the map (currently only Sentinel-2 L1C and L2A are supported, but more data sources will be supported here in the future).

The _SEARCH_ tab is located in the sidebar next to the _VISUALIZE_ tab (see Fig. 6).


## 3.1How to find a Product

To find products you can either use the keyword search (text input) or select one or more data sources using the checkboxes. To find products for a specific time range only, set the from/to date in the date input boxes. For example, let us find the latest Sentinel-2 L2A image over Italy for the beginning of 2023.

1. Zoom in on Italy on the map with the scroll wheel of your mouse.
2. Select Sentinel-2 \> MSI (selected by default) \> L2A
3. Set the Time Range to reflect two weeks (e.g., 2023-01-02, 2023-01-16)

![](RackMultipart20230119-1-h4ibb1_html_a06cc7435e7c4e69.png)

Fig. 7: _SEARCH_ tab with L2A collection selected and map centered on Rome (Italy)

1. Press the _Search_ button

You will now see the first 50 search results for your search settings (Sentinel L2A data over Italy for a time range of 2 weeks) in the sidebar and on the map. To load the next 50 results, click on the _Load more_ button at the end of the list in the sidebar. You can view the metadata of a product in the sidebar or by selecting a product on the map. In both cases you can:

- Directly view the basic metadata (preview image (available for most Sentinel-2 L1C, L2A, Sentinel-3 SLSTR and Sentinel-3 OLCI products), name, mission, instrument, acquisition time)
- view the full metadata by clicking on the product info button ( ![](RackMultipart20230119-1-h4ibb1_html_dfe48462b23bf80f.png)) in the results (full metadata)

## 3.2How to download a Product

![Shape7](RackMultipart20230119-1-h4ibb1_html_a842d7beaf60e68c.gif)
 When you have found a product (see How to find a Product) that you would like to download, you can do so by clicking click on the download icon ( ![](RackMultipart20230119-1-h4ibb1_html_6be88a493ad25750.png) ) for the desired product in the results (in the sidebar or in the results panel on the map after selecting a product). After you click the button, a progress bar will appear below the product to indicate the status of your download. If you have started a download by mistake, you can cancel it by clicking on the "x" below the download button.

You can continue to use the app as normal while a product is being downloaded.


# Tools

The Browser has several tools to help you better understand the data on the map and prepare it for sharing with others. These tools can be found in the upper right corner of the Browser. They can help you select the Area of Interest, measure, download the image, create a timelapse if you want to observe the area over a longer period of time, or analyze the statistics of an index (e.g., the NDVI).

1.

## 4.1Area/Point of Interest

Use the **Area of Interest (AOI)** tool to draw a rectangular or polygonal area of interest by clicking on the ![](RackMultipart20230119-1-h4ibb1_html_8c60d37e6fd795d1.png) icon in the upper right corner of the browser. You can also upload a KML/KMZ, GPX, WKT (in EPSG:4326) or GEOJSON/JSON file to create an area of interest.

Use the ![](RackMultipart20230119-1-h4ibb1_html_4576834c7961e264.png) icon to mark a location and re-center to the **Point of**  **I**** nterest (POI) ****.**

## 4.2Measure

You can use the **Measure** tool by clicking on the ![](RackMultipart20230119-1-h4ibb1_html_487d30066eefa25f.png) icon to get the distance and area measurements. To measure the distance between two points, simply click on the start and end points on the map, to measure the area, draw a polygon (areas can also be measured using the AOI drawing, as described in Area/Point of Interest).

## 4.3Image Download

There are three different download options. You can switch between the options using the tabs at the top of the pop-up window. Each option contains a preview of the data at the bottom. When you are satisfied with your download settings, you will find the ![](RackMultipart20230119-1-h4ibb1_html_53c1895165aae7e0.png) button below the preview:

- **Basic**
  - You can use the _Show Captions_ toggle switch to add data source, date, zoom scale and branding information to the exported images.
  - You can also use the _Add Map Overlays_ toggle switch to add place labels, streets and political boundaries to the image or the _Show Legend_ toggle switch to add the legend data.
  - You can use the _Crop to AOI_ toggle switch to crop the image to the bounds of area of interest, if drawn previously.
  - If you want to download the entire image but highlight the AOI, it can be done by enabling the _Draw AOI Geometry_.
  - Use the textbox to add a short description to the exported image.
  - Choose between two image formats (JPG, PNG).
  - A preview of the image that will be downloaded is displayed under _Preview_. Previews are available only when you zoom in enough.
- **Analytical**
  - After preparing the data for download, click the ![](RackMultipart20230119-1-h4ibb1_html_53c1895165aae7e0.png) button to download the image in JPG, PNG, KMZ or GeoTIFF format.
  - Choose between different image formats, resolutions and coordinate systems before downloading the image. You can also attach a logo.
  - In the Analytical panel, you can select multiple layers (Visualized/Raw) and download them all in a single ZIP file.
- **High-res print**
  - Prepare the selected visual for high-resolution printing by manually selecting a format, size and DPI. Add captions, legends and descriptions as needed.

## 4.4Timelapse

- You can create a **Timelapse Animation** by clicking the ![](RackMultipart20230119-1-h4ibb1_html_80ae6fe3802bd385.png) icon.
- Select the Area of Interest by zooming in or out. When you are satisfied with the scene, click on the play button in the middle of the screen for more options.
- Select the time span in the upper left corner of the pop-up window. Alternatively, you can select only certain months in a year using the _filter by months_ option. You can also select the interval between images. Click on _Search_ to see all the results.
- You can filter the images by two methods: Minimum tile coverage and Maximum Cloud coverage. You can select the percentage of cover for each of those filters by adjusting the slider.
- You can either select all the images or choose the images manually. Once you have the list of images you want to display in the timelapse, select the speed, and transition to prepare your timelapse.
- Download the video by clicking on the _Download_ button.

### 4.4.1Histogram

With the **Histogram** tool you can display statistical data (the distribution of values) for specific layers by clicking on the ![](RackMultipart20230119-1-h4ibb1_html_3fd329e34152dd2.png) icon. The histogram is calculated for the data within your AOI, if defined or otherwise for the whole screen. This tool currently only works for index layers (e.g., the NDVI).
