# 3DGEO Remote Sensing Application Programming Interface (API)

<p style="text-align: justify;">
  <a href="https://www.linkedin.com/company/3dgeobr/">3DGEO Agricultural Monitoring with Remotely Piloted Aircraft System (RPAS) / Drones</a>, startup that uses the most modern aerial mapping tools with drones offering agile and low-cost geotechnology solutions for agricultural monitoring.<br>  
  <br> 
  This project is part of the first project built by the company. The code presented ⚠️⚠️<b>DOES NOT COMPROMISE INTELLECTUAL PROPERTY</b>⚠️⚠️, as it is present in a <b>Machine Learning technique</b>.<br>
  <br>
  The code is also ⚠️⚠️<b>NOT</b> in its <b>MOST CURRENT VERSION</b>.⚠️⚠️<br>
  <br>
  This API aims to <b>detect tampering</b> using <b>satellite images</b> and a set of <b>remote sensing indices</b>: Normalized Difference Vegetation Index (NDVI), Normalized Difference Water Index (NDWI) and Normalized Difference Built-up Index (NDBI), among others.
</p>

<br>
<hr>
<br>

## Source Code Structure 🏘️
<br><br>

<p style="text-align: justify;">
  This source code contains the following <b>applications</b>: <br>
  <ul>
    <li><em>tdg_back</em>: main project folder;</li>
    <li><em>authentication</em>: responsible for <b>Create</b>, <b>Read</b>, <b>Update</b> and <b>Delete</b> and <b>business rules</b> for <b>users and groups</b>;</li>
    <li><em>sentinel</em>: responsible for obtaining <b>satellite images from Sentinel Hub</b>, <b>NDVI</b> and the <b>first pre-processing</b> of the images and files for geoprocessing, for example, segmenting territories from shapefiles.</li>
  </ul>
  <br>
  ⚠️⚠️<b>I removed several methods from the classes and just left the comment</b>⚠️⚠️, classes, for example <em>sentinel.DetectChange</em>, can be <b>difficult to understand</b>.
</p>

<br><br><br>

<figure>
<p align="center">
  <img src="![app-sentinel-parte-1-ndvi drawio](https://github.com/GabesSeven/3DGEO-remote-sensing-API/assets/37443722/5a57d1fc-87de-4f65-819b-ba1119e6f0fa)" height="450" width="650" alt="3DGEO Remote Sensing API"/><br>
  Fluxo Parcial de Execução da API.
</p>
</figure>

<br>
<hr>
<br>

## Goal 🎯
<br><br>

<p style="text-align: justify;">
  Present my <b>technical mastery</b>, <b>coding standards</b>, <b>development experience</b>, and <b>proficiency</b> in the <b>Python</b> programming language.
  <br>
  I made the following code <b>snippets available</b>: <br> 
  <ul>
    <li><em>tdg_back.settings</em>: responsible for Django configurations;</li>
    <li><em>authentication.views.UserView.get</em>: responsible for returning user data through the Universally Unique Identifier (UUID);</li>
    <li><em>authentication.views.LoginView.post</em>: responsible for authentication;</li>
    <li><em>sentinel.SentinelRequests.cut_out</em>: responsible for cropping satellite images using shapefiles and Geospatial Data Abstraction Library (GDAL);</li>
    <li><em>sentinel.SentinelRequests.create_shapefile_geo</em>: responsible for creating shapefiles from coordinates recorded in the PostgreSQL;</li>
    <li><em>sentinel.SentinelRequests.get_statistics</em>: responsible for obtaining statistical values of pixels from satellite images;</li>
    <li><em>sentinel.SentinelRequests.unpack_tar_file</em>: responsible for decompacting images and metadata from requests to the Sentinel Hub;</li>
    <li><em>sentinel.SentinelRequests.sentinel_image_request_rgb</em>: responsible for building and sending request to Sentinel Hub;</li>
    <li><em>sentinel.SentinelRequests.sentinel_authentication</em>: responsible for authenticating the Sentinel Hub API.</li>
  </ul>  
</p>

<br>
<hr>
<br>

## Technologies Used 💾
<br><br>

<ul>
  <li>``Python``</li>
  <li>``Django``</li>
  <li>``Django REST Framework``</li>
  <li>``PostgreSQL``</li>
  <li>``Sentinel Hub``</li>
  <li>``GDAL and other geoprocessing libraries``</li> 
  <li>``JSON Web Token (JWT)``</li>
</ul> 

<br>
<hr>
<br>

## Developer 🧑‍💻 
<br><br>
| [<img src="https://avatars.githubusercontent.com/u/37443722?v=4" width=115><br><sub>Gabriel Ferreira</sub>](https://github.com/GabesSeven)
| :---: 


