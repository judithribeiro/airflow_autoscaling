import math
import boto3
from botocore.config import Config
import requests
import json
import time
from datetime import datetime
import logging
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable

AWS_REGION = Variable.get('AWS_DEFAULT_REGION')
AWS_ACCESS_KEY_ID = Variable.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY= Variable.get('AWS_SECRET_ACCESS_KEY')
logger = logging.getLogger(__name__)

default_args = {
    'owner': 'judith',
    'start_date': datetime(2020, 12, 28),
    'depends_on_past': False,
    'provide_context': True
}

my_config = Config(
    region_name = AWS_REGION,
    signature_version = 'v4',
    retries = {
        'max_attempts': 10,
        'mode': 'standard'
    }
)
client = boto3.client('firehose', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, config=my_config)


dag = DAG('scraping_api_zapimovel_dag',
          description='scraping api site zapimoveis',
          schedule_interval=None,
          # schedule_interval='0 0 1 * *',
          catchup=False,
          default_args=default_args)


def put_record(event):
    data = (json.dumps(event) + '\n').encode('utf-8')
    response = client.put_record(
        DeliveryStreamName='kinesis-firehose-delivery-stream-zapimovel',
        Record={
            'Data': data
        }
    )
    print(response)

def get_imovel(imovel) -> json:
    json_data = {
        "listingtype": imovel['listing']['listingType'],
        "description": imovel['listing']['description'],
        "title": imovel['listing']['title'],
        "createdat": imovel['listing']['createdAt'],
        "id": imovel['listing']['id'],
        "portal": imovel['listing']['portal'],
        "country": imovel['listing']['address']['country'],
        "addresscity": imovel['listing']['address']['city'],
        "addresslevel": imovel['listing']['address']['level'],
        "stateacronym": imovel['listing']['address']['stateAcronym'],
        "district": imovel['listing']['address']['district'],
        "state": imovel['listing']['address']['state'],
        "locationid": imovel['listing']['address']['locationId'],
        "zipcode": imovel['listing']['address']['zipCode'],
        "price": imovel['listing']['pricingInfos'][0]['price'],
        "status": imovel['listing']['status'],
        "link": imovel["link"]["href"]
    }
    json_data['parkingspaces'] = 0
    json_data['bathrooms'] = 0
    json_data['bedrooms'] = 0
    json_data['suites'] = 0
    json_data['totalareas'] = 0
    json_data['pricingiptu'] = 0
    json_data['monthlycondofee'] = 0
    if len(imovel['listing']['totalAreas']) > 0:
        json_data['totalareas'] = imovel['listing']['totalAreas'][0]
    if len(imovel['listing']['suites']) > 0:
        json_data['suites'] = imovel['listing']['suites'][0]
    if len(imovel['listing']['bathrooms']) > 0:
        json_data['bathrooms'] = imovel['listing']['bathrooms'][0]
    if len(imovel['listing']['bedrooms']) > 0:
        json_data['bedrooms'] = imovel['listing']['bedrooms'][0]
    if len(imovel['listing']['parkingSpaces']) > 0:
        json_data['parkingspaces'] = imovel['listing']['parkingSpaces'][0]
    if 'yearlyIptu' in imovel['listing']['pricingInfos'][0]:
        json_data['pricingiptu'] = imovel['listing']['pricingInfos'][0]['yearlyIptu']
    if 'monthlyCondoFee' in imovel['listing']['pricingInfos'][0]:
        json_data['monthlycondofee'] = imovel['listing']['pricingInfos'][0]['monthlyCondoFee']
    return json_data

def getImoveis(page: str):
    url = "https://glue-api.zapimoveis.com.br/v2/listings?0=U&1=n&2=i&3=t&4=T&5=y&6=p&7=e&8=_&9=N&10=O&11=N&12=E&categoryPage=RESULT&business=SALE&listingType=USED&parentId=null&size=24&from=24&page={}&includeFields=search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount),page,fullUriFragments,developments(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),superPremium(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),owners(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),nearby(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),expansion(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount))&cityWiseStreet=1&developmentsSize=3&superPremiumSize=3&addressCountry=&addressState=&addressCity=&addressZone=&addressNeighborhood=&addressStreet=&addressAccounts=&addressType=&addressLocationId=&addressPointLat=&addressPointLon=&__zt=rnk_gz:rescore_ctr_default".format(
        page)
    payload = {}
    headers = get_headers()
    response = requests.request("GET", url, headers=headers, data=payload)
    return json.loads(response.text)

def get_headers():
    return {
        'authority': 'glue-api.zapimoveis.com.br',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'x-domain': 'www.zapimoveis.com.br',
        'origin': 'https://www.zapimoveis.com.br',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.zapimoveis.com.br/venda/',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': '__cfduid=d8da87424c4dc614737b3bf25401d93b91606339089; __cfruid=3fc9d94fd8ab079e4b75c01aeee0e1c591a8ec22-1607214346'
    }


def task_1(**kwargs):
    output = {'output': 'start', 'execution_time': str(datetime.now())}
    logger.info(output)
    url = "https://glue-api.zapimoveis.com.br/v2/listings?0=U&1=n&2=i&3=t&4=T&5=y&6=p&7=e&8=_&9=N&10=O&11=N&12=E&categoryPage=RESULT&business=SALE&listingType=USED&parentId=null&size=24&from=24&page=1&includeFields=search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount),page,fullUriFragments,developments(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),superPremium(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),owners(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),nearby(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount)),expansion(search(result(listings(listing(displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId),medias,accountLink,link)),totalCount))&cityWiseStreet=1&developmentsSize=3&superPremiumSize=3&addressCountry=&addressState=&addressCity=&addressZone=&addressNeighborhood=&addressStreet=&addressAccounts=&addressType=&addressLocationId=&addressPointLat=&addressPointLon=&__zt=rnk_gz:rescore_ctr_default"
    payload = {}
    headers = get_headers()
    response = requests.request("GET", url, headers=headers, data=payload)
    json_data = json.loads(response.text)
    total = json_data['search']['totalCount']
    # paginas = 10
    paginas = math.ceil(total / 21)
    x = range(paginas)
    logger.info("total de paginas: {}".format(x))    
    for n in x:        
        logger.info("pagina {}/{}".format(x, total))
        time.sleep(3)
        json_data = getImoveis(str(n))
        for imovel in json_data['search']['result']['listings']:
            put_record(get_imovel(imovel))
    return output


def task_2(**kwargs):
    ti = kwargs['ti']
    output_task_1 = ti.xcom_pull(key='return_value', task_ids='task_1')
    logger.info(output_task_1)
    return {'output': 'stop', 'execution_time': str(datetime.now())}


t1 = PythonOperator(
    task_id='task_1',
    dag=dag,
    python_callable=task_1
)
t2 = PythonOperator(
    task_id='task_2',
    dag=dag,
    python_callable=task_2
)

t1 >> t2
