# Frequently Asked Questions


## Documentation

<details>
  <summary>Any plan to offer the Pangeo platform for "pythonist" ?</summary>
    <div>
    Currently not in the offer or roadmap
    </div>
</details>
<hr>

## Registration and authentication
<details>
  <summary>Will both portals be somehow integrated to support/encourage the transfer of the users from "try basics for free towards paid subscriptions"?</summary>
    <div>
    Yes, there will be a common user identity, which will allow registered users to seamlessly transfer between systems. This will also extend to other systems that will be added to the ecosystem in the future, assuming they will integrate it.
    </div>
</details>
<hr>

## Data

<details>
  <summary>You mentioned cloud native formats/interfaces. Will the data also be available in the original data formats (e.g., for data downloading)?</summary>
    <div>
    Yes, data will also be available in original data formats (i.e. .SAFE).
    </div>
</details>
<details>
  <summary>Are the data offered via Cloud Optimized Geotiffs (Also Level 1)?</summary>
    <div>
    Sentinel-1 GRD data will be available in COG format. Sentinel-2 will stay in JP2 for the moment, as it is a similarly performant cloud optimised format.
    </div>
</details>
<hr>

## APIs
<details>
  <summary>Comparing with existing https://scihub.copernicus.eu/ what will be the other free services (other than stac/cog already described above) ? for exemple are WMS/WCS api provided for visualisation on GIS ?</summary>
    <div>
    Compared to existing SciHub, there will indeed be additional APIs - OGC interfaces (WMS, WMTS, WCS), OpenEO, Sentinel Hub API, S3, and others
    </div>
</details>
<hr>


## Services
<details>
  <summary>Will both portals be somehow integrated to support / encourage the transfer of the users from "try basics for free" towards paid subscriptions?</summary>
    <div>
    Yes, there will be a common user identity, which will allow registered users to seamlessly transfer between systems. This will also extend to other systems that will be added to the ecosystem in the future, assuming they will integrate it.
    </div>
</details>





























































<style>@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap');


.container h1{
  color: #fff;
  text-align: center;
}

details{
  background-color: #FFFFFF;
  color: #0a0a0a;
  font-size: 1.2rem;
  border-radius: 5px;

}


summary {
    background-color: #FFFFFF;
  color: #0a0a0a;
  /* height:50px; */
  font-size:1.2rem;
  border-radius: 5px;
  padding: .5em 1.3rem;
  list-style: none;
  display: flex;
  justify-content: space-between;  
  transition: height 1s ease;
  box-shadow: rgba(0, 0, 0, 0.20) 0px 5px 15px;
  margin:15px;
  
}

summary::-webkit-details-marker {
  display: none;
}

summary:after{
  content: "\002B";
}

details[open] summary {
    border-bottom: 1px solid #aaa;
    margin-bottom: .5em;

}

details[open] summary:after{
  content: "\00D7";
 
}

details[open] div{
  padding: .5em 1em;
  margin-left:25px;}
  </style>