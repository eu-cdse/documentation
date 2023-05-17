## About the Browser

The Browser is a web browser application that allows you to easily search, visualize, modify and download imagery from the Sentinel satellites. You can access the Browser at:

[https://dataspace.copernicus.eu/browser/](https://dataspace.copernicus.eu/browser/){target="_blank"}

You can access the data and basic visualization without logging in but to utilize all the features of the Browser, you need a free account. To register for a free account, click [here](https://identity.cloudferro.com/auth/realms/CDSE/protocol/openid-connect/auth?client_id=sh-5f8b630b-b083-49ed-b340-b8f01ecb81c4&redirect_uri=https%3A%2F%2Fdataspace.copernicus.eu%2Fbrowser%2FoauthCallback.html&response_type=token&state=) to the browser. A new window will open where you can click on **New user? Click [here](https://identity.cloudferro.com/auth/realms/CDSE/login-actions/registration?client_id=sh-5f8b630b-b083-49ed-b340-b8f01ecb81c4&tab_id=kuySlol9oac){target="_blank"} to create an account and access the data**. Once you have created the account, you will automatically be logged in to the Browser. Remember to save your login credentials for the next time you want to log in to the Browser.

![Browser start screen](../_images/StartScreen.png){#fig-startscreen}


The Browser window is divided into three parts:

 1. The sidebar on the left side of the screen. Here you can set the parameters to search for, visualize and download data.
 2. The map in the middle of the screen. Here you can zoom in and out and move around to find the place you are interest in. In this area you will see visualized satellite imagery or geometries of the products, that are the result of your search.
 3. The toolbar on the right side of the screen. Here you find various tools (e.g., for measuring or downloading images) with which you can work with the data displayed on the map.
   

## Visualizing data

You can find the *VISUALIZE* tab in the upper left corner of the sidebar (selected by default). The *VISUALIZE* tab will allow you to easily visualize satellite imagery on the map. Change or modify your visualization with just a few clicks.

### Visualizing data
In order to visualize data on the map, you need to zoom in to your area of interest. You can do this either with the mouse wheel or with the location search in the upper right corner.

Let's try to visualize the latest Sentinel-2 L2A imagery over Italy.

1. Either zoom to Italy with the mouse wheel or type *Italy* in the search box in the upper right corner.
2. In the sidebar, a maximum cloud coverage of 30% and the product type Sentinel-2 L2A are already preselected. To visualize the latest available data with cloud coverage below 30% click on the *Show latest date* button.
<!-- ![Visualize](../_images/VisualizeLatestInfo.png) -->

    ![VisualizeTab](../_images/VisualizeLatestInfo.png){#fig-2 width=350}



    Fig 2: VISUALIZE tab with *show latest date button* and *Sentinel-2 L2A* collection highlighted

You can now see the latest data over Italy on the map. Depending on the latest data available you will see data from one or more orbits (stripes of images on the map).

#### Modifying and Changing a Visualization

If you want to improve how the data is displayed on the map, you can modify the visualization by clicking on *Show effects and advanced options* at the bottom of the sidebar. Change the *Gain/Gamma* values, the values of the *R/G/B* colour channels, specify which sampling method is used for the visualization *(Layer default, Bilinear, Bicubic, Nearest)* or click on _Reset_ to reset all changes made. To return to the visualization layers overview, click on *Show visualizations*.

To visualize different Sentinel-2 band combinations, either use one of the prepared options from the list of layers (e.g., NDVI for the Normalized Difference Vegetation Index using the Sentinel bands B4 and B8) or click *Custom* at the bottom of the layers list.

<img src="../_images/Customlayer.png" width="350">

Fig 3: *Custom* Layers option with *Composite Index and Custom* script highlighted

Here you can create a custom *R/G/B* composite or _Index_ (band ratio, normalized difference index) by dragging and dropping the Sentinel-2 bands into the appropriate circles or use the _Custom script_ functionality to insert a piece of JavaScript code.

#### Changing the Data Collection

You can switch visualizing between different data collections by clicking on the arrow next to the Data Collections section in the Visualization tab. Once you click on the arrow as seen in Fig. 4, you will be able to see a drop-down menu with a list of the satellite data that is available. Let us try to visualize Sentinel-3 data of the same location and date as that of the Sentinel-2 data in section 2.1.  
1.	Click on the drop-down arrow on the right next to Pins icon. 
2.	Click on the drop-down arrow next to Sentinel-2 and select Sentinel-3.
3.	You can select the product you want to visualize. To visualize the Brightness temperature, select Sentinel-3 SLSTR L1B. You can see the predefined layers that can be visualized and click on the green button to Show latest date.

At the moment, the Data Collections available for visualization are Sentinel-2 (L1C and L2A), Sentinel-3 (OLCI Level-1 EFT, SLSTR Level-1 RBT) and Sentinel-5P.

<img src="../_images/DataCollection.png" width="450">

Fig 4: Changing *Data Collection* from *Visualization* tab directly

#### Comparing Visualizations

To compare two (or more) visualizations you must add them to the compare panel. You can add a visualization to the compare panel by clicking on the *Add to compare* button in each visualization layer *(see Fig. 5)*. When you have added all the layers you want to compare to the compare panel, you can switch to it by clicking on the compare icon ( ![compare](../_images/icons/CompareIcon.png) ). In the compare panel you can choose between a *Split* and an *Opacity* mode. With the *Split* mode you can compare two images side by side. With the *Opacity* mode you can compare two (or more) visualizations on top of each other.

<img src="../_images/AddIcon.png" width="350">

Fig 5: *Add to compare* and compare icon

#### Saving Pins

To save a visualization for future viewing, you can save it as a pin by clicking on ( ![addto](../_images/icons/AddTo.png)) next to the Layer name and clicking on *Add to Pins*. You can find the saved pins by clicking on the ( ![pin](../_images/icons/PinIcon.png)) icon. If you wish to compare saved pins, you can add them to the compare panel as explained in the previous section. If you have multiple pins saved and want to compare them altogether, you can directly go to the compare panel and add all the pins to compare by clicking on ( ![addallpins](../_images/icons/AddAllPins.png)). Another feature of the Browser is that you can export pins as a JSON file and import previously exported pins as well.

<img src="../_images/AddPins.png" width="350">

Fig 6: *Add to pins* and Pins icon

### Product Search for Current Visualization

When you are visualizing data (chapter Visualizing data), you can easily find the products associated with the data you see on the map. The product allows you to inspect the full metadata and easily download the raw data. To find connected products, just click the *Find products for current view* button in the sidebar (under the *Show latest date* button).


<img src="../_images/FindProduct.png" width="350">

Fig 7: *Add to compare* and compare icon

### 3D Visualization

With the 3D visualization tool, users can also visualize the terrain. To obtain a 3D visualization, you need to first select a layer to view and then click on the ![3d](../_images/icons/3D.png) icon. You can move forward, backward, left, or right by right clicking on the pan console (labelled 1 in the red box in Fig. 8) and rotate around a point by right clicking on the camera console (labelled 2 in the red box in Fig. 8). The viewing angle can be adjusted by scaling vertically and panning in all directions. You can further explore the area by adjusting the sun projected shadows and the shading parameters of the scene in the settings (labelled as box 3 and 4 respectively in Fig. 8). This 3D view can also be downloaded as a PNG or JPEG file.
Let us try visualizing Mont Blanc, the highest peak in the Alps.
1.	Follow the steps mentioned in *Visualizing Data* chapter to visualize Mont Blanc and select the “True Color” visualization.
2.	Click on the ![3d](../_images/icons/3D.png) icon placed at the right of the screen.
3.	You can navigate around the visualization either with your mouse, keyboard or directly on the map by following the instructions mentioned in the “Help” section (click on the ( ![info3d](../_images/icons/Info3D.png)) icon).
4.  Click on the Settings icon ( ![settings](../_images/icons/Settings.png)). Set the Vertical terrain scaling to 150% by moving the slider. 
5.	To adjust shadows, click on the Parameters next to Sun projected shadows toggle switch. 
6.	To adjust Shading parameters, click on Edit and modify the Ambient factor, Diffuse factor, Specular factor, and Specular power.
7.	You can Reset values at any point to return to the default settings. 

<img src="../_images/3DViz.png" width="1024">

Fig 8: 3D visualization in the Browser with pop-up Settings windows on the right

## Product Search

With the product search you can find products from four Sentinel missions (Sentinel-1, Sentinel-2, Sentinel-3, Sentinel-5p) and the sensors on board these satellites (C-SAR, MSI, OLCI, SRAL, SLSTR, SYNERGY). You can explore the metadata for each of those products, download the raw data or visualize the data on the map (currently only Sentinel-2, Sentinel-3 and Sentinel-5P are supported, but more data sources will be supported here in the future).

The *SEARCH* tab is located in the sidebar next to the *VISUALIZE* tab (see Fig. 9).

<img src="../_images/SearchTab.png" width="350">

Fig 9: *SEARCH* tab with different *Data Sources, Time range and Search* button


### How to find a Product

To find products you can either use the keyword search (text input) or select one or more data sources using the checkboxes. To find products for a specific time range only, set the from/to date in the date input boxes. For example, let us find the latest Sentinel-2 L2A image over Italy for the beginning of 2023.

   1. Zoom in on Italy on the map with the scroll wheel of your mouse.
   2. Select Sentinel-2 \> MSI (selected by default) \> L2A.
   3. Set the Time Range to reflect two weeks (e.g., 2023-01-02, 2023-01-16)
   4. Press the _Search_ button

<img src="../_images/SearchResult.png" width="1024">

Fig. 10: *SEARCH* tab with L2A collection selected and map centred on Rome (Italy)

You will now see the first 50 search results for your search settings (Sentinel L2A data over Italy for a time range of 2 weeks) in the sidebar and on the map. To load the next 50 results, click on the _Load more_ button at the end of the list in the sidebar. You can view the metadata of a product in the sidebar or by selecting a product on the map. In both cases you can:

* Directly view the basic metadata (preview image (available for most Sentinel-2 L1C, L2A, Sentinel-3 SLSTR and Sentinel-3 OLCI products), name, mission, instrument, acquisition time)
* View the full metadata by clicking on the product info button ( ![Info](../_images/icons/InfoIcon.png)) in the results (full metadata)

#### Additional Filters

To get more suitable results, you can also select or choose additional filters as shown in Figure 11. 
1.	Select the Data Source and the appropriate instrument/ processing level.
2.	Click on the Filter button and set the filtering parameters.
3.	Press the Search button. 
Here, you can choose various parameters depending on the chosen Data Source. For example, you can see the filter parameters for Sentinel-1 in Figure 11, letting you filter the results based on satellite platform, orbit direction, relative orbit number, acquisition mode, Beam ID and polarization.

<img src="../_images/Filters.png" width="450">

Fig 11: Data filters and parameters

#### Visualize the search result

Once you find the tiles you need following the above steps, you can visualize this one in of the two ways: by clicking on the region of interest and looking at the tiles that cover the region or select the tile from the Search panel on the left. Below the preview of the tile, there is a button to visualize ( ![visualize](../_images/icons/VisualizeButton.png) ), which will take you to the Visualize tab.

<img src="../_images/VisualizeTile.png" width="1024">

Fig 12: Tile selection and visualization

### How to download a Product

When you have found a product (see How to find a Product) that you would like to download, you can do so by clicking click on the download icon ( ![download](../_images/icons/DownloadIcon.png) ) for the desired product in the results (in the sidebar or in the results panel on the map after selecting a product). After you click the button, a progress bar will appear below the product to indicate the status of your download. If you have started a download by mistake, you can cancel it by clicking on the "x" below the download button.

You can continue to use the app as normal while a product is being downloaded.

<img src="../_images/ProductDownload.png" width="450">

Fig. 13: Product download (in progress) with Download product and cancel button highlighted

## Tools

The Browser has several tools to help you better understand the data on the map and prepare it for sharing with others. These tools can be found in the upper right corner of the Browser. They can help you select the Area of Interest, measure, download the image, create a timelapse if you want to observe the area over a longer period of time, or analyse the statistics of an index (e.g., the NDVI).

### Area/Point of Interest

Use the **Area of Interest (AOI)** tool to draw a rectangular or polygonal area of interest by clicking on the ![polygon](../_images/icons/PolygonIcon.png) icon in the upper right corner of the browser. You can also upload a KML/KMZ, GPX, WKT (in EPSG:4326) or GEOJSON/JSON file to create an area of interest.

Use the ![location](../_images/icons/Location.png) icon to mark a location and re-centre to the **Point of Interest(PoI)**

### Measure

You can use the **Measure** tool by clicking on the ![measure](../_images/icons/MeasureIcon.png) icon to get the distance and area measurements. To measure the distance between two points, simply click on the start and end points on the map, to measure the area, draw a polygon (areas can also be measured using the AOI drawing, as described in Area/Point of Interest).

### Image Download

There are three different download options. You can switch between the options using the tabs at the top of the pop-up window. Each option contains a preview of the data at the bottom. When you are satisfied with your download settings, you will find the ![Button](../_images/icons/DownloadButton.png) button below the preview:

* **Basic**
  - You can use the *Show Captions* toggle switch to add data source, date, zoom scale and branding information to the exported images.
  - You can also use the *Add Map Overlays* toggle switch to add place labels, streets and political boundaries to the image or the *Show Legend* toggle switch to add the legend data.
  - You can use the *Crop to AOI* toggle switch to crop the image to the bounds of area of interest, if drawn previously.
  - If you want to download the entire image but highlight the AOI, it can be done by enabling the *Draw AOI Geometry*.
  - Use the textbox to add a short description to the exported image.
  - Choose between two image formats (JPG, PNG).
  - A preview of the image that will be downloaded is displayed under *Preview*. Previews are available only when you zoom in enough.
* **Analytical**
  - After preparing the data for download, click the ![Button](../_images/icons/DownloadButton.png) button to download the image in JPG, PNG, KMZ or GeoTIFF format.
  - Choose between different image formats, resolutions and coordinate systems before downloading the image. You can also attach a logo.
  - In the Analytical panel, you can select multiple layers (Visualized/Raw) and download them all in a single ZIP file.
- **High-res print**
  - Prepare the selected visual for high-resolution printing by manually selecting a format, size and DPI. Add captions, legends and descriptions as needed.

### Timelapse

**Timelapses** are a very popular and useful tool to show how a certain location on Earth changed through time. Using the timelapse tool you can create your own visualization of changes through time and export it as .GIF or .MPEG4 to share it with others online. 
Let’s create a timelapse of the deforestation in the Brazil from 2018 – 2022.
1.	Go to: https://sentinelshare.page.link/osH4 
2.	Click on the timelapse icon ( ![lapse](../_images/icons/TimeLapse.png) ) and click on the play button in the middle of the screen. This opens a pop-up window to create a timelapse.
3.	Change the settings on the left side to:
  a.	Dates 2018-01-01 – 2022-12-31
  b.	Select 1 image per: month
Alternatively, you can select only certain months in a year using the filter by months option. Click on Search to see all the results.
4.	In the Visualizations set the Min. tile coverage to 100% and the Max. cloud coverage to 2% and manually deselect the images from the 2022-05-30 (slightly cloudy) and the 2022-09-07 (blurry).
5.	Once you have the list of images you want to display in the timelapse, select the speed, and transition to prepare your timelapse.
6.	Click on the play button to check the result and download the animation as a GIF-file using the Download button for further use online/offline.

<img src="../_images/Timelapse.png" width="1024">

Fig 14: Browser timelapse tool with settings highlighted


#### Histogram

With the **Histogram** tool you can display statistical data (the distribution of values) for specific layers by clicking on the ![histogram](../_images/icons/HistIcon.png) icon. The histogram is calculated for the data within your AOI, if defined or otherwise for the whole screen. This tool currently only works for index layers (e.g., the NDVI).

<img src="../_images/Hist.png" width="550">

Fig. 15: Example of a distribution plot of NDVI values
