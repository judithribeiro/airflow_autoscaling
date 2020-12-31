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
from netimovel.apinetimoveis import ApiNetiovelFactory
from netimovel.netimovel import NetimovelFactory


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


dag = DAG('scraping_api_netimovel_dag',
          description='scraping api site netimoveis',
          schedule_interval=None,
          catchup=False,
          default_args=default_args)


def put_record(event):
    data = (json.dumps(event) + '\n').encode('utf-8')
    response = client.put_record(
        DeliveryStreamName='kinesis-firehose-delivery-stream-netimovel',
        Record={
            'Data': data
        }
    )
    print(response)

def task_1(**kwargs):
    output = {'output': 'start', 'execution_time': str(datetime.now())}
    logger.info(output)
    netimovel = NetimovelFactory.get_netimovel()
    netimovel.migrate()
    api = ApiNetiovelFactory.get_api()
    api.page = 1
    api.get_records()
    #x = range(api.paginas)
    x = range(30)
    for n in x:
        api.page = n
        records = api.get_records()
        for record in records["lista"]:
            print(type(record))
            print(record.get('imovelSan_Id'))
            imovel = NetimovelFactory.get_netimovel()
            imovel.imovelsan_id = record.get('imovelSan_Id')
            print(record.get('dataHoraUltimoAtualisacao').get('descricao').get('pt'))
            imovel.find()
            if not imovel.id:
                imovel.datahora = record.get('dataHora')
                imovel.datahoraultimoatualisacao = record.get('dataHoraUltimoAtualisacao').get('descricao').get('pt')
                imovel.grupoimovel_id = record.get('grupoImovel_Id')
                imovel.status_id = record.get('status_Id')
                imovel.idadeimovel = record.get('idadeImovel')
                imovel.tipoimovel1_id = record.get('tipoImovel1_Id')
                imovel.tipoimovel2_id = record.get('tipoImovel2_Id')
                imovel.tipoimovel1 = record.get('tipoImovel1')
                imovel.tipoimovel1al = record.get('tipoImovel1Al')
                imovel.tipoimovel2 = record.get('tipoImovel2')
                imovel.tipoimovel2al = record.get('tipoImovel2Al')
                imovel.nomearquivo = record.get('nomeArquivo')
                imovel.nomearquivothumb = record.get('nomeArquivoThumb')
                imovel.valorimovel = record.get('valorImovel')
                imovel.valorimovelformat = record.get('valorImovelFormat')
                imovel.valorlocacao = record.get('valorLocacao')
                imovel.valorlocacaoformat = record.get('valorLocacaoFormat')
                imovel.valorcondominio = record.get('valorCondominio')
                imovel.valorcondominioformat = record.get('valorCondominioFormat')
                imovel.valoriptu = record.get('valorIPTU')
                imovel.valoriptuformat = record.get('valorIptuFormat')
                imovel.exibelocacao = record.get('exibeLocacao')
                imovel.exibevenda = record.get('exibeVenda')
                imovel.transacaolocacao = record.get('transacaoLocacao')
                imovel.transacaosigla = record.get('transacaoSigla')
                imovel.logradouropublico = record.get('logradouroPublico')
                imovel.logradouroautocomplete_url = record.get('logradouroAutoComplete_url')
                imovel.tipologradouro = record.get('tipoLogradouro')
                imovel.logradouroautocomplete = record.get('logradouroAutoComplete')
                imovel.transacaovenda = record.get('transacaoVenda')
                imovel.flagobras = record.get('flagObras')
                imovel.estado_id = record.get('estado_Id')
                imovel.siglaestado = record.get('siglaEstado')
                imovel.nomeestado = record.get('nomeEstado')
                imovel.nomeestadoal = record.get('nomeEstadoAl')
                imovel.cidade_id = record.get('cidade_Id')
                imovel.nomecidade = record.get('nomeCidade')
                imovel.nomecidadeal = record.get('nomeCidadeAl')
                imovel.regiao_id = record.get('regiao_Id')
                imovel.nomeregiao = record.get('nomeRegiao')
                imovel.bairro1_id = record.get('bairro1_Id')
                imovel.bairro2_id = record.get('bairro2_Id')
                imovel.nomebairro = record.get('nomeBairro')
                imovel.nomeregiaoal = record.get('nomeRegiaoAl')
                imovel.nomebairroal = record.get('nomeBairroAl')
                imovel.nomebairro2al = record.get('nomeBairro2Al')
                imovel.descricao = record.get('descricao')
                imovel.descricaoal = record.get('descricaoAl')
                imovel.arearealprivativa = record.get('areaRealPrivativa')
                imovel.metragem = record.get('metragem')
                imovel.latitude2 = record.get('latitude2')
                imovel.longitude2 = record.get('longitude2')
                imovel.agenciasan_id = record.get('agenciaSan_Id')
                imovel.celula_id = record.get('celula_Id')
                imovel.textocomplementar = record.get('textoComplementar')
                imovel.pontuacao = record.get('pontuacao')
                imovel.semfiador = record.get('semFiador')
                imovel.embed360 = record.get('embed360')
                imovel.embedvideo = record.get('embedVideo')
                imovel.parcelaiptu = record.get('parcelaIPTU')
                imovel.isentoiptu = record.get('isentoIptu')
                imovel.vagasgaragem = record.get('vagasGaragem')
                imovel.flagfinanciamento = record.get('flagFinanciamento')
                imovel.quartos = record.get('quartos')
                imovel.banho = record.get('banho')
                imovel.vagagaragem = record.get('vagaGaragem')
                imovel.suites = record.get('suites')
                imovel.varanda = record.get('varanda')
                imovel.dce = record.get('dce')
                imovel.piscina = record.get('piscina')
                imovel.playground = record.get('playGround')
                imovel.flaghabites = record.get('flagHabites')
                imovel.churrasqueira = record.get('churrasqueira')
                imovel.portariapermanente = record.get('portariaPermanente')
                imovel.elevadorsocial = record.get('elevadorSocial')
                imovel.quadradeesporte = record.get('quadraDeEsporte')
                imovel.academia = record.get('academia')
                imovel.salaodefestas = record.get('salaoDeFestas')
                imovel.salaodejogos = record.get('salaoDeJogos')
                imovel.sauna = record.get('sauna')
                imovel.jardim = record.get('jardim')
                imovel.mobiliado = record.get('mobiliado')
                imovel.cameraseguranca = record.get('cameraSeguranca')
                imovel.guarita = record.get('guarita')
                imovel.gascanalizado = record.get('gasCanalizado')
                imovel.interfone = record.get('interfone')
                imovel.proximoescolainfantil = record.get('proximoEscolaInfantil')
                imovel.proximofaculdade = record.get('proximoFaculdade')
                imovel.proximofarmacia = record.get('proximoFarmacia')
                imovel.proximohospital = record.get('proximoHospital')
                imovel.proximomercado = record.get('proximoMercado')
                imovel.sistemadealarme = record.get('sistemaDeAlarme')
                imovel.proximometro = record.get('proximoMetro')
                imovel.tag = record.get('tag')
                imovel.textoanuncio = record.get('textoAnuncio')
                imovel.complemento = record.get('complemento')
                imovel.nomecondominio = record.get('nomeCondominio')
                imovel.nomecondominio_url = record.get('nomecondominio_url')
                imovel.banhos = record.get('banhos')
                imovel.areaconstruida = record.get('areaConstruida')
                imovel.frentelote = record.get('frenteLote')
                imovel.areaexternaprivativa = record.get('areaExternaPrivativa')
                imovel.arealote = record.get('areaLote')
                imovel.numerodepavimentos = record.get('numeroDePavimentos')
                imovel.unidadesporandar = record.get('unidadesPorAndar')
                imovel.totaunidades = record.get('totaUnidades')
                imovel.sala = record.get('sala')
                imovel.flagdestaque = record.get('flagDestaque')
                imovel.flagimovelocupado = record.get('flagImovelOcupado')
                imovel.prediovazado = record.get('predioVazado')
                imovel.aquecimentosolar = record.get('aquecimentoSolar')
                imovel.arcondicionado = record.get('arCondicionado')
                imovel.portaoeletronico = record.get('portaoEletronico')
                imovel.circuitodetv = record.get('circuitoDeTv')
                imovel.elevadorcodificado = record.get('elevadorCodificado')
                imovel.elevadordeservico = record.get('elevadorDeServico')
                imovel.quartodedespejo = record.get('quartoDeDespejo')
                imovel.quartodemotorista = record.get('quartoDeMotorista')
                imovel.esquadriasdealuminio = record.get('esquadriasDeAluminio')
                imovel.salademassagem = record.get('salaDeMassagem')
                imovel.hallsocialdecorado = record.get('hallSocialDecorado')
                imovel.janelacomvenezianas = record.get('janelaComVenezianas')
                imovel.soldamanha = record.get('solDaManha')
                imovel.terrenomarinhaforeiro = record.get('terrenoMarinhaForeiro')
                imovel.laudemio = record.get('laudemio')
                imovel.terrenomarinhaocupante = record.get('terrenoMarinhaOcupante')
                imovel.medidordeaguaindividual = record.get('medidorDeAguaIndividual')
                imovel.rampaparacadeirante = record.get('rampaParaCadeirante')
                imovel.vistaparaomar = record.get('vistaParaOMar')
                imovel.andaralto = record.get('andarAlto')
                imovel.aguaencanada = record.get('aguaEncanada')
                imovel.aquecedor = record.get('aquecedor')
                imovel.arcondicionadocentral = record.get('arCondicionadoCentral')
                imovel.armariobanheiro = record.get('armarioBanheiro')
                imovel.armariocozinha = record.get('armarioCozinha')
                imovel.armarioembutido = record.get('armarioEmbutido')
                imovel.armarioquarto = record.get('armarioQuarto')
                imovel.banheira = record.get('banheira')
                imovel.bicicletario = record.get('bicicletario')
                imovel.canil = record.get('canil')
                imovel.caseiro = record.get('caseiro')
                imovel.closet = record.get('closet')
                imovel.deck = record.get('deck')
                imovel.disponivel = record.get('disponivel')
                imovel.escritorio = record.get('escritorio')
                imovel.espacozen = record.get('espacoZen')
                imovel.estacionamentocoberto = record.get('estacionamentoCoberto')
                imovel.estacionamentocommanobrista = record.get('estacionamentoComManobrista')
                imovel.estacionamentovagademarcada = record.get('estacionamentoVagaDemarcada')
                imovel.estacionamentovisitante = record.get('estacionamentoVisitante')
                imovel.habites = record.get('habites')
                imovel.idealparaagricultura = record.get('idealParaAgricultura')
                imovel.lareira = record.get('lareira')
                imovel.lavabo = record.get('lavabo')
                imovel.medidordegasindividual = record.get('medidorDeGasIndividual')
                imovel.mezanino = record.get('mezanino')
                imovel.permiteanimais = record.get('permiteAnimais')
                imovel.permutaimovel = record.get('permutaImovel')
                imovel.pocoartesiano = record.get('pocoArtesiano')
                imovel.pomar = record.get('pomar')
                imovel.proximocosta = record.get('proximoCosta')
                imovel.proximopadaria = record.get('proximoPadaria')
                imovel.proximoparque = record.get('proximoParque')
                imovel.proximoponto = record.get('proximoPonto')
                imovel.proximorestaurante = record.get('proximoRestaurante')
                imovel.quadrafutebol = record.get('quadraFutebol')
                imovel.quadratenis = record.get('quadraTenis')
                imovel.quantidadedevaga = record.get('quantidadeDeVaga')
                imovel.restaurante = record.get('restaurante')
                imovel.silo = record.get('silo')
                imovel.sistemacombateincendio = record.get('sistemaCombateIncendio')
                imovel.sobreloja = record.get('sobreLoja')
                imovel.spa = record.get('spa')
                imovel.vagacompartilhadapresa = record.get('vagaCompartilhadaPresa')
                imovel.vagalivre = record.get('vagaLivre')
                imovel.vagaparadeficiente = record.get('vagaParaDeficiente')
                imovel.vestiario = record.get('vestiario')
                imovel.vistamar = record.get('vistaMar')
                imovel.vistamontanha = record.get('vistaMontanha')
                imovel.acessivel = record.get('acessivel')
                imovel.paisnome = record.get('paisNome')
                imovel.paisurl = record.get('paisURL')
                imovel.pais_id = record.get('pais_Id')
                imovel.locale = record.get('locale')
                imovel.culturecurrency = record.get('cultureCurrency')
                imovel.desctopografia = record.get('descTopografia')
                imovel.datafimobra = record.get('dataFimObra')
                imovel.descricaovagas = record.get('descricaoVagas')
                imovel.fachadafrontal = record.get('fachadaFrontal')
                imovel.fachadalateral = record.get('fachadaLateral')
                imovel.aproveitamento = record.get('aproveitamento')
                imovel.arearealprivativacoberta = record.get('areaRealPrivativaCoberta')
                imovel.arearealprivativadescoberta = record.get('areaRealPrivativaDescoberta')
                imovel.telefonecontato = record.get('telefoneContato')
                imovel.emailcontato = record.get('emailContato')
                imovel.flagmostrartelefonepadrao = record.get('flagMostrarTelefonePadrao')
                imovel.grupoimovel = record.get('grupoImovel')
                imovel.nomecelula = record.get('nomeCelula')
                imovel.imovelmatriz = record.get('imovelMatriz')
                imovel.paramtransacao = record.get('paramTransacao')
                imovel.urldetalheimovel = record.get('urlDetalheImovel')
                imovel.save()
                print(f"save {imovel.imovelsan_id}")                                                         


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
