# 3DGEO remote sensing Application Programming Interface (API)

<p style="text-align: justify;">
  <a href="https://www.linkedin.com/company/3dgeobr/">3DGEO Monitoramento Agrícola com RPAS (Drones)</a>, startup que utiliza as mais modernas ferramentas de mapeamento aéreo com Drones oferecendo de forma ágil e com baixo custo soluções em geotecnologias para o monitoramento Agrícola. <br>  
  <br>
  Neste projeto está parte do primeiro projeto contruído pela empresa. O código apresentado ⚠️⚠️<b>NÃO COMPROMETE A PROPRIEDADE INTELECTUAL</b>⚠️⚠️, pois a mesma está presente em uma <b>técnica Machine Learning.</b> <br>
  <br>
  O código também ⚠️⚠️<b>NÃO ESTÁ</b> na sua <b>VERSÃO MAIS ATUAL</b>.⚠️⚠️<br>
  <br>
  Esta API tem como objetivo <b>detectar aduteração</b> utilizando <b>imagens satelitáis</b> e conjunto de <b>índices de sensoriamento remoto</b>: Normalized Difference Vegetation Index (NDVI), Normalized Difference Water Index (NDWI) e Normalized Difference Built-up Index (NDBI), entre outros.
</p>

<br>
<hr>
<br>

# Source Code Structure 🏘️

<p style="text-align: justify;">
  Neste código-fonte está presente as seguintes aplicações: <br>
  <ul>
    <li><em>tdg_back</em>: pasta principal do projeto;</li>
    <li><em>authentication</em>: responsável pelo <b>Creat</b>, <b>Read</b>, <b>Update</b> e <b>Delete</b> e <b>regras de negócio</b> para <b>usuários e grupos</b>;</li>
    <li><em>sentinel</em>: responsável por obter <b>imagens satelitais.SentinelRequests. do Sentinel Hub</b>, <b>NDVI</b> e os <b>primeiros pré-processamentos</b> nas imanges e arquivos para geoprocessamento, por exemplo, segmentação de territórios a partir de shapefiles</li>.
  </ul>
  <br>
  ⚠️⚠️<b>Retirei diversas métodos das classes</b> e <b>somente deixei o cometário</b>⚠️⚠️, classes, por exemplo <em>sentinel.DetectChange</em>, podem estar de <b>difícis compreensão</b>.
</p>

<br>
<hr>
<br>

# Goal 🎯

<p style="text-align: justify;">
  Apresentar meu <b>domínio técnico</b>, <b>padrões de codificação</b>, <b>experiência em desenvolvimento</b> e <b>proficiência na linguagem</b> de programação <b>Python</b>. <br>
  <br>
  Deixei disponível os seguintes <b>trechos de código</b>: <br> 
  <ul>
    <li><em>tdg_back.settings</em>: responsável pelas configurações do Django;</li>
    <li><em>authentication.views.UserView.get</em>: responsável por retornar usuário através do Universally Unique Identifier (UUID);</li>
    <li><em>authentication.views.LoginView.post</em>: responsável por autenticação de usuário;</li>
    <li><em>sentinel.SentinelRequests.cut_out</em>: responsável por recortar a imagem satelital utilizando arquivos shapefile e biblioteca Geospatial Data Abstraction Library (GDAL);</li>
    <li><em>sentinel.SentinelRequests.create_shapefile_geo</em>: responsável por criar arquivos shapefiles a partir de coordenadas gravadas no Banco de Dados;</li>
    <li><em>sentinel.SentinelRequests.get_statistics</em>: responsável por obter valores estatíticos de píxels de imagens satelitais;</li>
    <li><em>sentinel.SentinelRequests.unpack_tar_file</em>: responsável por descompactar imagens e metadados vindas de requisição ao Sentinel Hub;</li>
    <li><em>sentinel.SentinelRequests.sentinel_image_request_rgb</em>: responsável por construir e enviar requisição ao Sentinel Hub;</li>
    <li><em>sentinel.SentinelRequests.sentinel_authentication</em>: responsável pela autenticação a API do Sentinel Hub.</li>
  </ul>  
</p>

<br>
<hr>
<br>


<br>
<hr>
<br>


<br>
<hr>
<br>



## Developer 🧑‍💻 
<br><br>
| [<img src="https://avatars.githubusercontent.com/u/37443722?v=4" width=115><br><sub>Gabriel Ferreira</sub>](https://github.com/GabesSeven)
| :---: 


