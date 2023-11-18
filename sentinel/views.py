from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sentinelhub import SHConfig
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient
from datetime import datetime, timedelta
import json
import subprocess
import tarfile
import shutil
from django.core.files.images import ImageFile        
from rest_framework.permissions import IsAuthenticated, AllowAny

import os
import urllib.request
            
import rasterstats
import shapefile
from osgeo import gdal

from .serializers import GeometryImmobileWithoutPropertiesSerializer, GeometryDistrictWithoutPropertiesSerializer, GeometryBorderWithoutPropertiesSerializer, PropertieImmobileSerializer
from .models import GeometryCoordinatesUTM, GeometryBorder, GeometryDistrict, GeometryImmobile, DistrictImagesNDVISub, DistrictImageRGB, ImmobileImageRGB, NDVIStatistics
from django.http import JsonResponse

from django.shortcuts import render
from django.conf import settings

class GetStoredStatisticsView(APIView):
    """
    Obtém dados estatísticos a partir de uma data.
    """
    pass 

        # """
        # Verifica a variável convertendo a data de string para timestamp.
        # """

        # """
        # Busca no banco de dados as estatísticas relacionadas a variável "date".
        # """
        
        # """
        # Prepara dados de resposta ao usuário e retorna ao frontend.
        # """
    
class GetStatisticsDatesView(APIView):
    """
    Obtém datas disponíveis agrupadas.
    """
    pass
    
        # """
        # Busca no banco de dados todas as datas disponíveis agrupadas por DD/MM/AAAA.        
        # """
    
        # """
        # Prepara dados de resposta ao usuário e retorna ao frontend.
        # """
    
class GetPropertieView(APIView):
    """
    De acordo com o parâmetro 'gid', retorna os dados JSON da propriedade.
    """
    pass

    
class GetFeauresView(APIView):
    """
    De acordo com o prâmetro 'code', retorna os dados JSON de coordenadas geográficas de todos imóveis, distritos e/ou fronteira (borda).
    """
    pass 
    

class SentinelRequests():
    """
    Possui métodos de:
      - autenticação com o satélite Sentinel Hub;
      - requisição de imagens NDVI para o satélite Sentinel Hub;
      - requisição de imagens RGB para o satélite Sentinel Hub;
      - conversão de coordenada de imagens;
      - recorte de imagens utilizando shapefile;
      - criação de arquivos shapefile montados a partir de coordenadas GEO;
      - criação de arquivos shapefile montados a partir de coordenadas UTM;
      - criação de bound box (bbox) a partir de coordenadas;
      - descompactação de arquivos e busca por metadados.
    """
    pass

    def __del__(self):
        """
        Limpa variável global que representa o token da requisição ao sentinel.
        """
        pass

    def convert_image_coordinates(self):
        """
        Converte imagens IMAGE_RGB_NEW.png e IMAGE_RGB_OLD.png de coordenadas EPSG 4326 para EPSG 3857.
        """
        pass

            # """
            # Abrir os arquivos de entrada.
            # """
        
            # """
            # Definir o sistema de coordenadas de origem (EPSG 4326).
            # """
            
            # """
            # Criar um novo arquivo de saída com o sistema de coordenadas de destino (EPSG 3857)
            # """
            
            # """
            # Fechar os datasets.
            # """
            
    
    def cut_out(self, gid):
        """
        Realiza criação de arquivo shapefile, caso ele não exista.
        """
        if not(os.path.exists(f"media/files/input/shapefiles/utm/{gid}/polygon_{gid}.shp")):
            if not(self.create_shapefile_utm(gid)):
                return False
            
        """
        Abre o conjunto de dados raster, define os parâmetros para a saída do recorte, executa a operação de recorte, libera a memória e fecha os arquivos. 
        """
        print("\n*** Recortando raster com GDAL... ***\n")
        try:
            raster_ds = gdal.Open("media/images/output_rgb/RGB_NOT_CUT.tif")            
            output_options = gdal.WarpOptions(cutlineDSName=f"media/images/input/shapefiles/{gid}/polygon_{gid}.shp", cropToCutline=True)
            gdal.Warp("media/images/output_rgb/RGB_CUT.tif", raster_ds, options=output_options)
        except:
            return Response({"info": 'erroooo acontece aqui', "status": status.HTTP_400_BAD_REQUEST})
        
        raster_ds = None

        print("\n*** Recorte concluída com sucesso. ***\n")
        return True
      
    def create_shapefile_geo(self, gid):
        """ 
        Cria um novo shapefile, define seus campos (atributos), adiciona um polígono ou multipolígono para o shapefile e depois o salva.
        """

        print("\n*** Criando arquivo shapefile... ***\n")
        try:
            geometry = GeometryImmobile.objects.get(gid=gid)
            sf = shapefile.Writer(f"media/files/input/shapefiles/geo/{gid}/polygon_{gid}.shp", shapeType=shapefile.POLYGON)
            sf.field("Nome", "C", size=50)
            sf.field("Valor", "N", decimal=10)
            if geometry.geometry["type"] == "Polygon":
                sf.poly(geometry.geometry["coordinates"])
                sf.record("", None)  # Atributos vazios, pois não foram fornecidos
            else:    
                for polygon in geometry.geometry["coordinates"]:
                    sf.poly(polygon)
                    sf.record("", None)  # Atributos vazios, pois não foram fornecidos        
            sf.close()

            print("\n*** Arquivo shapefile criado com sucesso. ***\n")
            return True
        except:
            return False

    def create_shapefile_utm(self, gid):
        """ 
        Cria um novo shapefile, define seus campos (atributos), adiciona um polígono ou multipolígono para o shapefile e depois o salva.
        """
        pass

    def get_statistics(self, gid):
        """
        Realiza criação de arquivo shapefile, caso ele não exista.
        """
        if not(os.path.exists(f"media/files/input/shapefiles/utm/{gid}/polygon_{gid}.shp")):
            if not(self.create_shapefile_utm(gid)):
                return None

        """
        Calcula estatistica zonal referente a propriedade em execução.
        """
        stats = rasterstats.zonal_stats(f"media/files/input/shapefiles/utm/{gid}/polygon_{gid}.shp", 'media/images/output_ndvi/IMAGE_NDVI_SUB.tif', stats=['mean', 'min', 'max', 'std'])        
        print(f"\n*** GID {gid}: ***\n", json.dumps(stats, indent=4), "\n\n")
        return stats   

    def search_data(self, name, path):
        """
        Lê arquivos JSON e procura pela com menor valor de cobertura de nuvem, pois foi essa escolhida na requisição.
        """
        pass

    def unpack_tar_file(self, tar_file_path, tar_filename, path_destination, new_filename):
        """
        Descompacta um arquivo específico e o salva localmente renomeando-o.
        """
        try:
            with tarfile.open(tar_file_path, 'r') as tar_file:
                file = tar_file.extractfile(tar_filename)
                if file:
                    try:
                        with open(path_destination + '/' + new_filename, 'wb') as new_file:
                            shutil.copyfileobj(file, new_file)
                        print(f"\n*** Sucesso na descompactação do arquivo {new_filename}. ***\n")
                        return True
                    except:
                        print(f"\n*** Erro na descompactação do arquivo {new_filename}. ***\n")
                        return False
                else:
                    print(f"\n*** Erro na descompactação do arquivo {new_filename}. ***\n")
                    return False
        except:
            print(f"\n*** Erro na descompactação do arquivo {new_filename}. ***\n")
            return False

    def sentinel_image_request_rgb(self):
        """ 
        Requisição para API do Sentinel Hub através de comando curl, dados de entrada e saída são setados nesse comando. 
        Após a requisição uma imagem RGB deve ser salva na pasta /media/files/output_rgb
        """   
        
        """
        Requisição com parâmetros para se obter o RGB.
        """
        request_rgb = {
            "input": {
                "bounds": {
                    "properties": {
                        "crs": "http://www.opengis.net/def/crs/EPSG/0/4326"
                    },
                    "bbox": self.bbox
                },
                "data": [
                    {
                        "type": "sentinel-2-l2a",
                        "dataFilter": {
                            "timeRange": {
                                "from": self.date_start.strftime("%Y-%m-%dT%H:%M:%SZ"),
                                "to": self.date_end.strftime("%Y-%m-%dT%H:%M:%SZ")
                            }
                        },
                        "maxCloudCoverage": 0,
                    }
                ]
            },
            "output": {
                "width": 2500,
                "height": 2500,
                "responses": [
                    {
                        "identifier": "default",
                        "format": {
                            "type": "image/tiff",
                            "quality": 80,
                        }
                    },
                    {
                        "identifier": "userdata",
                        "format": {
                            "type": "application/json"
                        }
                    }
                ],
                "upsampling": "NEAREST"
            }
        }
        evalscript_rgb='''//VERSION=3
        function setup() {
            return {
                input: ["B02", "B03", "B04"],
                mosaicking: Mosaicking.ORBIT,
                output: { 
                    bands: 3, 
                    sampleType: "AUTO" // default value - scales the output values from [0,1] to [0,255].
                }
            }
        }

        function updateOutputMetadata(scenes, inputMetadata, outputMetadata) {
           outputMetadata.userData = { "scenes":  scenes.orbits }   
        }

        function evaluatePixel(sample) {
            return [2.5 * sample[0].B04, 2.5 * sample[0].B03, 2.5 * sample[0].B02]
        }
        '''
    
        request = json.dumps(request_rgb)
        
        curl_command = f'''curl -X POST \
        https://services.sentinel-hub.com/api/v1/process \
        -H 'Authorization: Bearer {self.token}' \
        -H 'accept: application/tar' \
        -F 'request={request}' \
        -F 'evalscript={evalscript_rgb}' -o media/files/output_rgb/{self.filename}.tar '''  #  
        # print(json.dumps(curl_command, indent=4))

        result = subprocess.run(curl_command, shell=True, capture_output=True)

        """
        Verifica se a requisição foi bem sucedida ou não, por exemplo, token expirado, portanto acesso negado.
        Não funciona pois a saída stdout vêm através do .tar
        """
        # stdout = result.stdout.decode('utf-8')
        # stdout = json.loads(stdout)
        # if stdout["error"]["status"] and stdout["error"]["status"] != 200:
        #     return False

        if result.returncode != 0:
            print(f"\n*** Erro na requisição do arquivo {self.filename}.tar ao Sentinel. ***\n.")
            # print(result)
            return False
        else:
            print(f"\n*** Sucesso na requisição do arquivo {self.filename}.tar ao Sentinel. ***\n.") 
            # print(result)
            return True

    def image_request_rgb(self):
        """
        Ajusta dados do request e realiza requisição.
        """    
        pass

    def ndvi_subtraction(self):
        """ 
        Abre os arquivos GeoTIFF, obtém bandas raster e lê os valores de pixel em uma matriz NumPy.
        """
        pass

    def sentinel_image_request_ndvi(self):
        """ 
        Requisição para API do Sentinel Hub através de comando curl, dados de entrada e saída são setados nesse comando. 
        Após a requisição uma imagem NDVI deve ser salva na pasta /media/files/output_ndvi
        """   
        pass

        """
        Requisição com parâmetros para se obter o NDVI.
        """

        """
        Verifica se a requisição foi bem sucedida ou não, por exemplo, token expirado, portanto acesso negado.
        Não funciona pois a saída stdout vêm através do .tar
        """
        

    def image_request_ndvi(self):
        """
        Ajusta dados do request e realiza requisição.
        """
        pass
        
        """
        Extrai arquivos da requisição.
        """
        
    def get_bbox(self, coordinates, type):
        """
        Percorre todo array ou multi-array de coordenadas e monta o BBOX correspondente.
        """
        pass
    
    def search_coordinates_utm(self, id):
        """
        Busca coordenadas do Banco de Dados e monta o BBOX.
        """
        pass

    def search_coordinates_geo(self, id, checker=None):
        """
        Busca coordenadas do Banco de Dados e monta o BBOX.
        """
        pass

    def sentinel_authentication(self):
        """
        Autenticação com API do Sentinel Hub, é necessário se cadastrar no site do Sentinel Hub, posteriormente obter um token.
        """
        client_id = settings.SENTINEL_CLIENT_ID
        client_secret = settings.SENTINEL_CLIENT_SECRET

        configuration = SHConfig()
        configuration.sh_client_id = client_id
        configuration.sh_client_secret = client_secret
        configuration.save()

        client = BackendApplicationClient(client_id=client_id)
        oauth = OAuth2Session(client=client)
        
        try:
            token = oauth.fetch_token(token_url="https://services.sentinel-hub.com/oauth/token", client_secret=client_secret)
        except:
            return False 

        """
        Verifica se o token foi obtido.
        """
        config = SHConfig()
        config.sh_client_id = client_id
        config.sh_client_secret = client_secret
        config.save()

        client = BackendApplicationClient(client_id=client_id)
        oauth = OAuth2Session(client=client)
        
        try:
            token = oauth.fetch_token(token_url="https://services.sentinel-hub.com/oauth/token", client_secret=client_secret)
        except:
            return False 

        self.token = token["access_token"]

        # resp = oauth.get("https://services.sentinel-hub.com/oauth/tokeninfo")
        return True  
    
class DetectChange(APIView, SentinelRequests):
    """
    Responsável por varrer todas propriedades, distrito por distrito, detectar alteração e informar ao frontend todas regiões detectadas. 
    """
    pass

    """
    Setando variáveis
    """

    """
    Varrendo SEDE-CENTRO, dados que terão que ser DINÂMICOS posteriormente.
    """

    """
    Pegar todos gids e cordenadas referente ao distrito em execução.
    """
    
    """
    SEDE-NORTE, SEDE-CENTRO, SEDE-SUL devem referenciar SEDE
    """
    
    """
    Obtém dados estatísticos referente aquela propriedade em execução.
    """
    
    """
    Realiza comparação através do desvio padrão.
    """
    
    """
    Salva novos dados estatísticos na tabela de imóveis
    """
    
    """
    Salva novos dados estatísticos na tabela de estatísticas
    """   
        
    """
    Verifica se imagem existe no bucket, se sim baixar, senão realiza uma requisição a mais.
    """ 
    
    """
    Busca por última imagem no banco de dados.
    """
    
    """
    Baixar imagem IMAGE_RGB_OLD do bucket. OBS.: PERMISSÃO AO BUCKET DEVER SER PÚBLICA
    """
    
    """
    Busca coordenadas do Banco de Dados e monta o BBOX.
    """
    
    """
    Erro ao realizar requisição.
    """
        
    """
    Ajusta as datas.
    """
    
    """
    Requisição RGB_NEW.
    """
    
    """
    Erro ao realizar requisição.
    """
        
    """
    Procura pelos metadados corretos no JSON da requisição RGB_NEW.
    """
    
    """
    Verifica cobertura de nuvem.
    """
    
    """
    Ajusta variáveis para serem salvas no banco de dados.
    """
    
    """
    Realiza a primeira requisição.
    """
        
    """
    Busca coordenadas do Banco de Dados e monta o BBOX.
    """

    """
    Erro ao realizar requisição.
    """
    
    """
    Requisição RGB_OLD
    """

    """
    Erro ao realizar requisição.
    """
        
    """
    Procura pelos metadados corretos no JSON da requisição RGB_OLD.
    """

    """
    Verifica cobertura de nuvem.
    """

    """
    Requisição RGB_NEW.
    """

    """
    Erro ao realizar requisição.
    """
        
    """
    Procura pelos metadados corretos no JSON da requisição RGB_NEW.
    """

    """
    Verifica cobertura de nuvem.
    """
    
    """
    Converte imagem(ns) RGB, de EPSG 4326 para EPSG 3857.
    """

    """
    Erro ao realizar conversão.
    """

    """
    Salvar imagem(ns) no banco de dados.
    """
    
    """
    Adiciona dados ao array de resposta
    """

    """
    Verifica se imagem existe no bucket, se sim baixar, senão realiza uma requisição a mais.
    """

    """
    Busca por última imagem no banco de dados.
    """

    """
    Baixar imagem IMAGE_NDVI_OLD do bucket. OBS.: PERMISSÃO AO BUCKET DEVER SER PÚBLICA
    """

    """
    Busca coordenadas do Banco de Dados e monta o BBOX.
    """

    """
    Erro ao realizar requisição.
    """
        

    """
    Ajusta as datas.
    """

    """
    Requisição NDVI_NEW.
    """

    """
    Erro ao realizar requisição.
    """
        
    """
    Procura pelos metadados corretos no JSON da requisição NDVI_NEW.
    """

    """
    Verifica cobertura de nuvem.
    """

    """
    Ajusta variáveis para serem salvas no banco de dados.
    """

    """
    Realiza a primeira requisição.
    """
        
    """
    Busca coordenadas do Banco de Dados e monta o BBOX.
    """

    """
    Erro ao realizar requisição.
    """

    """
    Requisição NDVI_OLD
    """

    """
    Erro ao realizar requisição.
    """
        
    """
    Procura pelos metadados corretos no JSON da requisição NDVI_OLD.
    """

    """
    Verifica cobertura de nuvem.
    """

    """
    Requisição NDVI_NEW.
    """

    """
    Erro ao realizar requisição.
    """
        
    """
    Procura pelos metadados corretos no JSON da requisição NDVI_NEW.
    """

    """
    Verifica cobertura de nuvem.
    """
    
    """
    Seta range de datas que serão salvo as estatísticas.
    """

    """
    Subtração NDVI.
    """

    """
    Salvar imagem(ns) no banco de dados.
    """

    """
    Ajusta as datas.
    """

    """
    Realiza autenticação com API Sentinel Hub.
    """
    
    """
    Percorre distrito por distrito
    """

    """
    Requisita imagens NDVI para comparação de dados estatísticos dos pixels. 
    """

    """
    Obtém dados estatísticos dos pixels da subtração de imagens NDVI e atualiza banco de dados. 
    """

    """
    Requisita imagens RGB para devolução ao frontend. 
    """
        
    """
    Limpa variável global que representa o token da requisição ao sentinel.
    """
    
    """
    Prepara dados de resposta ao usuário e retorna ao frontend.
    """
    
class GetImageRgb(DetectChange):
    """
    Retorna RGB_NEW.png e RGB_OLD.png para distritos ou imóveis.
    """
    pass 

    """
    Verifica as variáveis.
    """
    
    """
    Ajusta as datas.
    """

    """
    Realiza autenticação com API Sentinel Hub.
    """
    
    """
    Requisita imagens RGB para devolução ao frontend. 
    """            
    
    """
    Limpa variável global que representa o token da requisição ao sentinel.
    """
    
    """
    Prepara dados de resposta ao usuário e retorna ao frontend.
    """