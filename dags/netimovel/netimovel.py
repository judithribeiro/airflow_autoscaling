from netimovel.connection import Connection
from abc import ABC, abstractclassmethod
from datetime import datetime


class NetimovelAbstract(ABC):
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def imovelsan_id(self):
        return self._imovelsan_id

    @imovelsan_id.setter
    def imovelsan_id(self, value):
        self._imovelsan_id = value

    @property
    def datahora(self):
        return self._datahora

    @datahora.setter
    def datahora(self, value):
        self._datahora = value

    @property
    def datahoraultimoatualisacao(self):
        return self._datahoraultimoatualisacao

    @datahoraultimoatualisacao.setter
    def datahoraultimoatualisacao(self, value):
        self._datahoraultimoatualisacao = value

    @property
    def grupoimovel_id(self):
        return self._grupoimovel_id

    @grupoimovel_id.setter
    def grupoimovel_id(self, value):
        self._grupoimovel_id = value

    @property
    def status_id(self):
        return self._status_id

    @status_id.setter
    def status_id(self, value):
        self._status_id = value

    @property
    def idadeimovel(self):
        return self._idadeimovel

    @idadeimovel.setter
    def idadeimovel(self, value):
        self._idadeimovel = value

    @property
    def tipoimovel1_id(self):
        return self._tipoimovel1_id

    @tipoimovel1_id.setter
    def tipoimovel1_id(self, value):
        self._tipoimovel1_id = value

    @property
    def tipoimovel2_id(self):
        return self._tipoimovel2_id

    @tipoimovel2_id.setter
    def tipoimovel2_id(self, value):
        self._tipoimovel2_id = value

    @property
    def tipoimovel1(self):
        return self._tipoimovel1

    @tipoimovel1.setter
    def tipoimovel1(self, value):
        self._tipoimovel1 = value

    @property
    def tipoimovel1al(self):
        return self._tipoimovel1al

    @tipoimovel1al.setter
    def tipoimovel1al(self, value):
        self._tipoimovel1al = value

    @property
    def tipoimovel2(self):
        return self._tipoimovel2

    @tipoimovel2.setter
    def tipoimovel2(self, value):
        self._tipoimovel2 = value

    @property
    def tipoimovel2al(self):
        return self._tipoimovel2al

    @tipoimovel2al.setter
    def tipoimovel2al(self, value):
        self._tipoimovel2al = value

    @property
    def nomearquivo(self):
        return self._nomearquivo

    @nomearquivo.setter
    def nomearquivo(self, value):
        self._nomearquivo = value

    @property
    def nomearquivothumb(self):
        return self._nomearquivothumb

    @nomearquivothumb.setter
    def nomearquivothumb(self, value):
        self._nomearquivothumb = value

    @property
    def valorimovel(self):
        return self._valorimovel

    @valorimovel.setter
    def valorimovel(self, value):
        self._valorimovel = value

    @property
    def valorimovelformat(self):
        return self._valorimovelformat

    @valorimovelformat.setter
    def valorimovelformat(self, value):
        self._valorimovelformat = value

    @property
    def valorlocacao(self):
        return self._valorlocacao

    @valorlocacao.setter
    def valorlocacao(self, value):
        self._valorlocacao = value

    @property
    def valorlocacaoformat(self):
        return self._valorlocacaoformat

    @valorlocacaoformat.setter
    def valorlocacaoformat(self, value):
        self._valorlocacaoformat = value

    @property
    def valorcondominio(self):
        return self._valorcondominio

    @valorcondominio.setter
    def valorcondominio(self, value):
        self._valorcondominio = value

    @property
    def valorcondominioformat(self):
        return self._valorcondominioformat

    @valorcondominioformat.setter
    def valorcondominioformat(self, value):
        self._valorcondominioformat = value

    @property
    def valoriptu(self):
        return self._valoriptu

    @valoriptu.setter
    def valoriptu(self, value):
        self._valoriptu = value

    @property
    def valoriptuformat(self):
        return self._valoriptuformat

    @valoriptuformat.setter
    def valoriptuformat(self, value):
        self._valoriptuformat = value

    @property
    def exibelocacao(self):
        return self._exibelocacao

    @exibelocacao.setter
    def exibelocacao(self, value):
        self._exibelocacao = value

    @property
    def exibevenda(self):
        return self._exibevenda

    @exibevenda.setter
    def exibevenda(self, value):
        self._exibevenda = value

    @property
    def transacaolocacao(self):
        return self._transacaolocacao

    @transacaolocacao.setter
    def transacaolocacao(self, value):
        self._transacaolocacao = value

    @property
    def transacaosigla(self):
        return self._transacaosigla

    @transacaosigla.setter
    def transacaosigla(self, value):
        self._transacaosigla = value

    @property
    def logradouropublico(self):
        return self._logradouropublico

    @logradouropublico.setter
    def logradouropublico(self, value):
        self._logradouropublico = value

    @property
    def logradouroautocomplete_url(self):
        return self._logradouroautocomplete_url

    @logradouroautocomplete_url.setter
    def logradouroautocomplete_url(self, value):
        self._logradouroautocomplete_url = value

    @property
    def tipologradouro(self):
        return self._tipologradouro

    @tipologradouro.setter
    def tipologradouro(self, value):
        self._tipologradouro = value

    @property
    def logradouroautocomplete(self):
        return self._logradouroautocomplete

    @logradouroautocomplete.setter
    def logradouroautocomplete(self, value):
        self._logradouroautocomplete = value

    @property
    def transacaovenda(self):
        return self._transacaovenda

    @transacaovenda.setter
    def transacaovenda(self, value):
        self._transacaovenda = value

    @property
    def flagobras(self):
        return self._flagobras

    @flagobras.setter
    def flagobras(self, value):
        self._flagobras = value

    @property
    def estado_id(self):
        return self._estado_id

    @estado_id.setter
    def estado_id(self, value):
        self._estado_id = value

    @property
    def siglaestado(self):
        return self._siglaestado

    @siglaestado.setter
    def siglaestado(self, value):
        self._siglaestado = value

    @property
    def nomeestado(self):
        return self._nomeestado

    @nomeestado.setter
    def nomeestado(self, value):
        self._nomeestado = value

    @property
    def nomeestadoal(self):
        return self._nomeestadoal

    @nomeestadoal.setter
    def nomeestadoal(self, value):
        self._nomeestadoal = value

    @property
    def cidade_id(self):
        return self._cidade_id

    @cidade_id.setter
    def cidade_id(self, value):
        self._cidade_id = value

    @property
    def nomecidade(self):
        return self._nomecidade

    @nomecidade.setter
    def nomecidade(self, value):
        self._nomecidade = value

    @property
    def nomecidadeal(self):
        return self._nomecidadeal

    @nomecidadeal.setter
    def nomecidadeal(self, value):
        self._nomecidadeal = value

    @property
    def regiao_id(self):
        return self._regiao_id

    @regiao_id.setter
    def regiao_id(self, value):
        self._regiao_id = value

    @property
    def nomeregiao(self):
        return self._nomeregiao

    @nomeregiao.setter
    def nomeregiao(self, value):
        self._nomeregiao = value

    @property
    def bairro1_id(self):
        return self._bairro1_id

    @bairro1_id.setter
    def bairro1_id(self, value):
        self._bairro1_id = value

    @property
    def bairro2_id(self):
        return self._bairro2_id

    @bairro2_id.setter
    def bairro2_id(self, value):
        self._bairro2_id = value

    @property
    def nomebairro(self):
        return self._nomebairro

    @nomebairro.setter
    def nomebairro(self, value):
        self._nomebairro = value

    @property
    def nomeregiaoal(self):
        return self._nomeregiaoal

    @nomeregiaoal.setter
    def nomeregiaoal(self, value):
        self._nomeregiaoal = value

    @property
    def nomebairroal(self):
        return self._nomebairroal

    @nomebairroal.setter
    def nomebairroal(self, value):
        self._nomebairroal = value

    @property
    def nomebairro2al(self):
        return self._nomebairro2al

    @nomebairro2al.setter
    def nomebairro2al(self, value):
        self._nomebairro2al = value

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, value):
        self._descricao = value

    @property
    def descricaoal(self):
        return self._descricaoal

    @descricaoal.setter
    def descricaoal(self, value):
        self._descricaoal = value

    @property
    def arearealprivativa(self):
        return self._arearealprivativa

    @arearealprivativa.setter
    def arearealprivativa(self, value):
        self._arearealprivativa = value

    @property
    def metragem(self):
        return self._metragem

    @metragem.setter
    def metragem(self, value):
        self._metragem = value

    @property
    def latitude2(self):
        return self._latitude2

    @latitude2.setter
    def latitude2(self, value):
        self._latitude2 = value

    @property
    def longitude2(self):
        return self._longitude2

    @longitude2.setter
    def longitude2(self, value):
        self._longitude2 = value

    @property
    def agenciasan_id(self):
        return self._agenciasan_id

    @agenciasan_id.setter
    def agenciasan_id(self, value):
        self._agenciasan_id = value

    @property
    def celula_id(self):
        return self._celula_id

    @celula_id.setter
    def celula_id(self, value):
        self._celula_id = value

    @property
    def textocomplementar(self):
        return self._textocomplementar

    @textocomplementar.setter
    def textocomplementar(self, value):
        self._textocomplementar = value

    @property
    def pontuacao(self):
        return self._pontuacao

    @pontuacao.setter
    def pontuacao(self, value):
        self._pontuacao = value

    @property
    def semfiador(self):
        return self._semfiador

    @semfiador.setter
    def semfiador(self, value):
        self._semfiador = value

    @property
    def embed360(self):
        return self._embed360

    @embed360.setter
    def embed360(self, value):
        self._embed360 = value

    @property
    def embedvideo(self):
        return self._embedvideo

    @embedvideo.setter
    def embedvideo(self, value):
        self._embedvideo = value

    @property
    def parcelaiptu(self):
        return self._parcelaiptu

    @parcelaiptu.setter
    def parcelaiptu(self, value):
        self._parcelaiptu = value

    @property
    def isentoiptu(self):
        return self._isentoiptu

    @isentoiptu.setter
    def isentoiptu(self, value):
        self._isentoiptu = value

    @property
    def vagasgaragem(self):
        return self._vagasgaragem

    @vagasgaragem.setter
    def vagasgaragem(self, value):
        self._vagasgaragem = value

    @property
    def flagfinanciamento(self):
        return self._flagfinanciamento

    @flagfinanciamento.setter
    def flagfinanciamento(self, value):
        self._flagfinanciamento = value

    @property
    def quartos(self):
        return self._quartos

    @quartos.setter
    def quartos(self, value):
        self._quartos = value

    @property
    def banho(self):
        return self._banho

    @banho.setter
    def banho(self, value):
        self._banho = value

    @property
    def vagagaragem(self):
        return self._vagagaragem

    @vagagaragem.setter
    def vagagaragem(self, value):
        self._vagagaragem = value

    @property
    def suites(self):
        return self._suites

    @suites.setter
    def suites(self, value):
        self._suites = value

    @property
    def varanda(self):
        return self._varanda

    @varanda.setter
    def varanda(self, value):
        self._varanda = value

    @property
    def dce(self):
        return self._dce

    @dce.setter
    def dce(self, value):
        self._dce = value

    @property
    def piscina(self):
        return self._piscina

    @piscina.setter
    def piscina(self, value):
        self._piscina = value

    @property
    def playground(self):
        return self._playground

    @playground.setter
    def playground(self, value):
        self._playground = value

    @property
    def flaghabites(self):
        return self._flaghabites

    @flaghabites.setter
    def flaghabites(self, value):
        self._flaghabites = value

    @property
    def churrasqueira(self):
        return self._churrasqueira

    @churrasqueira.setter
    def churrasqueira(self, value):
        self._churrasqueira = value

    @property
    def portariapermanente(self):
        return self._portariapermanente

    @portariapermanente.setter
    def portariapermanente(self, value):
        self._portariapermanente = value

    @property
    def elevadorsocial(self):
        return self._elevadorsocial

    @elevadorsocial.setter
    def elevadorsocial(self, value):
        self._elevadorsocial = value

    @property
    def quadradeesporte(self):
        return self._quadradeesporte

    @quadradeesporte.setter
    def quadradeesporte(self, value):
        self._quadradeesporte = value

    @property
    def academia(self):
        return self._academia

    @academia.setter
    def academia(self, value):
        self._academia = value

    @property
    def salaodefestas(self):
        return self._salaodefestas

    @salaodefestas.setter
    def salaodefestas(self, value):
        self._salaodefestas = value

    @property
    def salaodejogos(self):
        return self._salaodejogos

    @salaodejogos.setter
    def salaodejogos(self, value):
        self._salaodejogos = value

    @property
    def sauna(self):
        return self._sauna

    @sauna.setter
    def sauna(self, value):
        self._sauna = value

    @property
    def jardim(self):
        return self._jardim

    @jardim.setter
    def jardim(self, value):
        self._jardim = value

    @property
    def mobiliado(self):
        return self._mobiliado

    @mobiliado.setter
    def mobiliado(self, value):
        self._mobiliado = value

    @property
    def cameraseguranca(self):
        return self._cameraseguranca

    @cameraseguranca.setter
    def cameraseguranca(self, value):
        self._cameraseguranca = value

    @property
    def guarita(self):
        return self._guarita

    @guarita.setter
    def guarita(self, value):
        self._guarita = value

    @property
    def gascanalizado(self):
        return self._gascanalizado

    @gascanalizado.setter
    def gascanalizado(self, value):
        self._gascanalizado = value

    @property
    def interfone(self):
        return self._interfone

    @interfone.setter
    def interfone(self, value):
        self._interfone = value

    @property
    def proximoescolainfantil(self):
        return self._proximoescolainfantil

    @proximoescolainfantil.setter
    def proximoescolainfantil(self, value):
        self._proximoescolainfantil = value

    @property
    def proximofaculdade(self):
        return self._proximofaculdade

    @proximofaculdade.setter
    def proximofaculdade(self, value):
        self._proximofaculdade = value

    @property
    def proximofarmacia(self):
        return self._proximofarmacia

    @proximofarmacia.setter
    def proximofarmacia(self, value):
        self._proximofarmacia = value

    @property
    def proximohospital(self):
        return self._proximohospital

    @proximohospital.setter
    def proximohospital(self, value):
        self._proximohospital = value

    @property
    def proximomercado(self):
        return self._proximomercado

    @proximomercado.setter
    def proximomercado(self, value):
        self._proximomercado = value

    @property
    def sistemadealarme(self):
        return self._sistemadealarme

    @sistemadealarme.setter
    def sistemadealarme(self, value):
        self._sistemadealarme = value

    @property
    def proximometro(self):
        return self._proximometro

    @proximometro.setter
    def proximometro(self, value):
        self._proximometro = value

    @property
    def tag(self):
        return self._tag

    @tag.setter
    def tag(self, value):
        self._tag = value

    @property
    def textoanuncio(self):
        return self._textoanuncio

    @textoanuncio.setter
    def textoanuncio(self, value):
        self._textoanuncio = value

    @property
    def complemento(self):
        return self._complemento

    @complemento.setter
    def complemento(self, value):
        self._complemento = value

    @property
    def nomecondominio(self):
        return self._nomecondominio

    @nomecondominio.setter
    def nomecondominio(self, value):
        self._nomecondominio = value

    @property
    def nomecondominio_url(self):
        return self._nomecondominio_url

    @nomecondominio_url.setter
    def nomecondominio_url(self, value):
        self._nomecondominio_url = value

    @property
    def banhos(self):
        return self._banhos

    @banhos.setter
    def banhos(self, value):
        self._banhos = value

    @property
    def areaconstruida(self):
        return self._areaconstruida

    @areaconstruida.setter
    def areaconstruida(self, value):
        self._areaconstruida = value

    @property
    def frentelote(self):
        return self._frentelote

    @frentelote.setter
    def frentelote(self, value):
        self._frentelote = value

    @property
    def areaexternaprivativa(self):
        return self._areaexternaprivativa

    @areaexternaprivativa.setter
    def areaexternaprivativa(self, value):
        self._areaexternaprivativa = value

    @property
    def arealote(self):
        return self._arealote

    @arealote.setter
    def arealote(self, value):
        self._arealote = value

    @property
    def numerodepavimentos(self):
        return self._numerodepavimentos

    @numerodepavimentos.setter
    def numerodepavimentos(self, value):
        self._numerodepavimentos = value

    @property
    def unidadesporandar(self):
        return self._unidadesporandar

    @unidadesporandar.setter
    def unidadesporandar(self, value):
        self._unidadesporandar = value

    @property
    def totaunidades(self):
        return self._totaunidades

    @totaunidades.setter
    def totaunidades(self, value):
        self._totaunidades = value

    @property
    def sala(self):
        return self._sala

    @sala.setter
    def sala(self, value):
        self._sala = value

    @property
    def flagdestaque(self):
        return self._flagdestaque

    @flagdestaque.setter
    def flagdestaque(self, value):
        self._flagdestaque = value

    @property
    def flagimovelocupado(self):
        return self._flagimovelocupado

    @flagimovelocupado.setter
    def flagimovelocupado(self, value):
        self._flagimovelocupado = value

    @property
    def prediovazado(self):
        return self._prediovazado

    @prediovazado.setter
    def prediovazado(self, value):
        self._prediovazado = value

    @property
    def aquecimentosolar(self):
        return self._aquecimentosolar

    @aquecimentosolar.setter
    def aquecimentosolar(self, value):
        self._aquecimentosolar = value

    @property
    def arcondicionado(self):
        return self._arcondicionado

    @arcondicionado.setter
    def arcondicionado(self, value):
        self._arcondicionado = value

    @property
    def portaoeletronico(self):
        return self._portaoeletronico

    @portaoeletronico.setter
    def portaoeletronico(self, value):
        self._portaoeletronico = value

    @property
    def circuitodetv(self):
        return self._circuitodetv

    @circuitodetv.setter
    def circuitodetv(self, value):
        self._circuitodetv = value

    @property
    def elevadorcodificado(self):
        return self._elevadorcodificado

    @elevadorcodificado.setter
    def elevadorcodificado(self, value):
        self._elevadorcodificado = value

    @property
    def elevadordeservico(self):
        return self._elevadordeservico

    @elevadordeservico.setter
    def elevadordeservico(self, value):
        self._elevadordeservico = value

    @property
    def quartodedespejo(self):
        return self._quartodedespejo

    @quartodedespejo.setter
    def quartodedespejo(self, value):
        self._quartodedespejo = value

    @property
    def quartodemotorista(self):
        return self._quartodemotorista

    @quartodemotorista.setter
    def quartodemotorista(self, value):
        self._quartodemotorista = value

    @property
    def esquadriasdealuminio(self):
        return self._esquadriasdealuminio

    @esquadriasdealuminio.setter
    def esquadriasdealuminio(self, value):
        self._esquadriasdealuminio = value

    @property
    def salademassagem(self):
        return self._salademassagem

    @salademassagem.setter
    def salademassagem(self, value):
        self._salademassagem = value

    @property
    def hallsocialdecorado(self):
        return self._hallsocialdecorado

    @hallsocialdecorado.setter
    def hallsocialdecorado(self, value):
        self._hallsocialdecorado = value

    @property
    def janelacomvenezianas(self):
        return self._janelacomvenezianas

    @janelacomvenezianas.setter
    def janelacomvenezianas(self, value):
        self._janelacomvenezianas = value

    @property
    def soldamanha(self):
        return self._soldamanha

    @soldamanha.setter
    def soldamanha(self, value):
        self._soldamanha = value

    @property
    def terrenomarinhaforeiro(self):
        return self._terrenomarinhaforeiro

    @terrenomarinhaforeiro.setter
    def terrenomarinhaforeiro(self, value):
        self._terrenomarinhaforeiro = value

    @property
    def laudemio(self):
        return self._laudemio

    @laudemio.setter
    def laudemio(self, value):
        self._laudemio = value

    @property
    def terrenomarinhaocupante(self):
        return self._terrenomarinhaocupante

    @terrenomarinhaocupante.setter
    def terrenomarinhaocupante(self, value):
        self._terrenomarinhaocupante = value

    @property
    def medidordeaguaindividual(self):
        return self._medidordeaguaindividual

    @medidordeaguaindividual.setter
    def medidordeaguaindividual(self, value):
        self._medidordeaguaindividual = value

    @property
    def rampaparacadeirante(self):
        return self._rampaparacadeirante

    @rampaparacadeirante.setter
    def rampaparacadeirante(self, value):
        self._rampaparacadeirante = value

    @property
    def vistaparaomar(self):
        return self._vistaparaomar

    @vistaparaomar.setter
    def vistaparaomar(self, value):
        self._vistaparaomar = value

    @property
    def andaralto(self):
        return self._andaralto

    @andaralto.setter
    def andaralto(self, value):
        self._andaralto = value

    @property
    def aguaencanada(self):
        return self._aguaencanada

    @aguaencanada.setter
    def aguaencanada(self, value):
        self._aguaencanada = value

    @property
    def aquecedor(self):
        return self._aquecedor

    @aquecedor.setter
    def aquecedor(self, value):
        self._aquecedor = value

    @property
    def arcondicionadocentral(self):
        return self._arcondicionadocentral

    @arcondicionadocentral.setter
    def arcondicionadocentral(self, value):
        self._arcondicionadocentral = value

    @property
    def armariobanheiro(self):
        return self._armariobanheiro

    @armariobanheiro.setter
    def armariobanheiro(self, value):
        self._armariobanheiro = value

    @property
    def armariocozinha(self):
        return self._armariocozinha

    @armariocozinha.setter
    def armariocozinha(self, value):
        self._armariocozinha = value

    @property
    def armarioembutido(self):
        return self._armarioembutido

    @armarioembutido.setter
    def armarioembutido(self, value):
        self._armarioembutido = value

    @property
    def armarioquarto(self):
        return self._armarioquarto

    @armarioquarto.setter
    def armarioquarto(self, value):
        self._armarioquarto = value

    @property
    def banheira(self):
        return self._banheira

    @banheira.setter
    def banheira(self, value):
        self._banheira = value

    @property
    def bicicletario(self):
        return self._bicicletario

    @bicicletario.setter
    def bicicletario(self, value):
        self._bicicletario = value

    @property
    def canil(self):
        return self._canil

    @canil.setter
    def canil(self, value):
        self._canil = value

    @property
    def caseiro(self):
        return self._caseiro

    @caseiro.setter
    def caseiro(self, value):
        self._caseiro = value

    @property
    def closet(self):
        return self._closet

    @closet.setter
    def closet(self, value):
        self._closet = value

    @property
    def deck(self):
        return self._deck

    @deck.setter
    def deck(self, value):
        self._deck = value

    @property
    def disponivel(self):
        return self._disponivel

    @disponivel.setter
    def disponivel(self, value):
        self._disponivel = value

    @property
    def escritorio(self):
        return self._escritorio

    @escritorio.setter
    def escritorio(self, value):
        self._escritorio = value

    @property
    def espacozen(self):
        return self._espacozen

    @espacozen.setter
    def espacozen(self, value):
        self._espacozen = value

    @property
    def estacionamentocoberto(self):
        return self._estacionamentocoberto

    @estacionamentocoberto.setter
    def estacionamentocoberto(self, value):
        self._estacionamentocoberto = value

    @property
    def estacionamentocommanobrista(self):
        return self._estacionamentocommanobrista

    @estacionamentocommanobrista.setter
    def estacionamentocommanobrista(self, value):
        self._estacionamentocommanobrista = value

    @property
    def estacionamentovagademarcada(self):
        return self._estacionamentovagademarcada

    @estacionamentovagademarcada.setter
    def estacionamentovagademarcada(self, value):
        self._estacionamentovagademarcada = value

    @property
    def estacionamentovisitante(self):
        return self._estacionamentovisitante

    @estacionamentovisitante.setter
    def estacionamentovisitante(self, value):
        self._estacionamentovisitante = value

    @property
    def habites(self):
        return self._habites

    @habites.setter
    def habites(self, value):
        self._habites = value

    @property
    def idealparaagricultura(self):
        return self._idealparaagricultura

    @idealparaagricultura.setter
    def idealparaagricultura(self, value):
        self._idealparaagricultura = value

    @property
    def lareira(self):
        return self._lareira

    @lareira.setter
    def lareira(self, value):
        self._lareira = value

    @property
    def lavabo(self):
        return self._lavabo

    @lavabo.setter
    def lavabo(self, value):
        self._lavabo = value

    @property
    def medidordegasindividual(self):
        return self._medidordegasindividual

    @medidordegasindividual.setter
    def medidordegasindividual(self, value):
        self._medidordegasindividual = value

    @property
    def mezanino(self):
        return self._mezanino

    @mezanino.setter
    def mezanino(self, value):
        self._mezanino = value

    @property
    def permiteanimais(self):
        return self._permiteanimais

    @permiteanimais.setter
    def permiteanimais(self, value):
        self._permiteanimais = value

    @property
    def permutaimovel(self):
        return self._permutaimovel

    @permutaimovel.setter
    def permutaimovel(self, value):
        self._permutaimovel = value

    @property
    def pocoartesiano(self):
        return self._pocoartesiano

    @pocoartesiano.setter
    def pocoartesiano(self, value):
        self._pocoartesiano = value

    @property
    def pomar(self):
        return self._pomar

    @pomar.setter
    def pomar(self, value):
        self._pomar = value

    @property
    def proximocosta(self):
        return self._proximocosta

    @proximocosta.setter
    def proximocosta(self, value):
        self._proximocosta = value

    @property
    def proximopadaria(self):
        return self._proximopadaria

    @proximopadaria.setter
    def proximopadaria(self, value):
        self._proximopadaria = value

    @property
    def proximoparque(self):
        return self._proximoparque

    @proximoparque.setter
    def proximoparque(self, value):
        self._proximoparque = value

    @property
    def proximoponto(self):
        return self._proximoponto

    @proximoponto.setter
    def proximoponto(self, value):
        self._proximoponto = value

    @property
    def proximorestaurante(self):
        return self._proximorestaurante

    @proximorestaurante.setter
    def proximorestaurante(self, value):
        self._proximorestaurante = value

    @property
    def quadrafutebol(self):
        return self._quadrafutebol

    @quadrafutebol.setter
    def quadrafutebol(self, value):
        self._quadrafutebol = value

    @property
    def quadratenis(self):
        return self._quadratenis

    @quadratenis.setter
    def quadratenis(self, value):
        self._quadratenis = value

    @property
    def quantidadedevaga(self):
        return self._quantidadedevaga

    @quantidadedevaga.setter
    def quantidadedevaga(self, value):
        self._quantidadedevaga = value

    @property
    def restaurante(self):
        return self._restaurante

    @restaurante.setter
    def restaurante(self, value):
        self._restaurante = value

    @property
    def silo(self):
        return self._silo

    @silo.setter
    def silo(self, value):
        self._silo = value

    @property
    def sistemacombateincendio(self):
        return self._sistemacombateincendio

    @sistemacombateincendio.setter
    def sistemacombateincendio(self, value):
        self._sistemacombateincendio = value

    @property
    def sobreloja(self):
        return self._sobreloja

    @sobreloja.setter
    def sobreloja(self, value):
        self._sobreloja = value

    @property
    def spa(self):
        return self._spa

    @spa.setter
    def spa(self, value):
        self._spa = value

    @property
    def vagacompartilhadapresa(self):
        return self._vagacompartilhadapresa

    @vagacompartilhadapresa.setter
    def vagacompartilhadapresa(self, value):
        self._vagacompartilhadapresa = value

    @property
    def vagalivre(self):
        return self._vagalivre

    @vagalivre.setter
    def vagalivre(self, value):
        self._vagalivre = value

    @property
    def vagaparadeficiente(self):
        return self._vagaparadeficiente

    @vagaparadeficiente.setter
    def vagaparadeficiente(self, value):
        self._vagaparadeficiente = value

    @property
    def vestiario(self):
        return self._vestiario

    @vestiario.setter
    def vestiario(self, value):
        self._vestiario = value

    @property
    def vistamar(self):
        return self._vistamar

    @vistamar.setter
    def vistamar(self, value):
        self._vistamar = value

    @property
    def vistamontanha(self):
        return self._vistamontanha

    @vistamontanha.setter
    def vistamontanha(self, value):
        self._vistamontanha = value

    @property
    def acessivel(self):
        return self._acessivel

    @acessivel.setter
    def acessivel(self, value):
        self._acessivel = value

    @property
    def paisnome(self):
        return self._paisnome

    @paisnome.setter
    def paisnome(self, value):
        self._paisnome = value

    @property
    def paisurl(self):
        return self._paisurl

    @paisurl.setter
    def paisurl(self, value):
        self._paisurl = value

    @property
    def pais_id(self):
        return self._pais_id

    @pais_id.setter
    def pais_id(self, value):
        self._pais_id = value

    @property
    def locale(self):
        return self._locale

    @locale.setter
    def locale(self, value):
        self._locale = value

    @property
    def culturecurrency(self):
        return self._culturecurrency

    @culturecurrency.setter
    def culturecurrency(self, value):
        self._culturecurrency = value

    @property
    def desctopografia(self):
        return self._desctopografia

    @desctopografia.setter
    def desctopografia(self, value):
        self._desctopografia = value

    @property
    def datafimobra(self):
        return self._datafimobra

    @datafimobra.setter
    def datafimobra(self, value):
        self._datafimobra = value

    @property
    def descricaovagas(self):
        return self._descricaovagas

    @descricaovagas.setter
    def descricaovagas(self, value):
        self._descricaovagas = value

    @property
    def fachadafrontal(self):
        return self._fachadafrontal

    @fachadafrontal.setter
    def fachadafrontal(self, value):
        self._fachadafrontal = value

    @property
    def fachadalateral(self):
        return self._fachadalateral

    @fachadalateral.setter
    def fachadalateral(self, value):
        self._fachadalateral = value

    @property
    def aproveitamento(self):
        return self._aproveitamento

    @aproveitamento.setter
    def aproveitamento(self, value):
        self._aproveitamento = value

    @property
    def arearealprivativacoberta(self):
        return self._arearealprivativacoberta

    @arearealprivativacoberta.setter
    def arearealprivativacoberta(self, value):
        self._arearealprivativacoberta = value

    @property
    def arearealprivativadescoberta(self):
        return self._arearealprivativadescoberta

    @arearealprivativadescoberta.setter
    def arearealprivativadescoberta(self, value):
        self._arearealprivativadescoberta = value

    @property
    def telefonecontato(self):
        return self._telefonecontato

    @telefonecontato.setter
    def telefonecontato(self, value):
        self._telefonecontato = value

    @property
    def emailcontato(self):
        return self._emailcontato

    @emailcontato.setter
    def emailcontato(self, value):
        self._emailcontato = value

    @property
    def flagmostrartelefonepadrao(self):
        return self._flagmostrartelefonepadrao

    @flagmostrartelefonepadrao.setter
    def flagmostrartelefonepadrao(self, value):
        self._flagmostrartelefonepadrao = value

    @property
    def grupoimovel(self):
        return self._grupoimovel

    @grupoimovel.setter
    def grupoimovel(self, value):
        self._grupoimovel = value

    @property
    def nomecelula(self):
        return self._nomecelula

    @nomecelula.setter
    def nomecelula(self, value):
        self._nomecelula = value

    @property
    def imovelmatriz(self):
        return self._imovelmatriz

    @imovelmatriz.setter
    def imovelmatriz(self, value):
        self._imovelmatriz = value

    @property
    def paramtransacao(self):
        return self._paramtransacao

    @paramtransacao.setter
    def paramtransacao(self, value):
        self._paramtransacao = value

    @property
    def urldetalheimovel(self):
        return self._urldetalheimovel

    @urldetalheimovel.setter
    def urldetalheimovel(self, value):
        self._urldetalheimovel = value


class Netimovel(NetimovelAbstract):

    def __init__(self):
        self.id = None
        self.created_at = datetime.now().isoformat()

    def find(self):
        connection = Connection()
        conn = connection.get_connection()
        cur = conn.cursor()
        cur.execute(f"select * from public.netimoveis where imovelsan_id = '{self.imovelsan_id}'")
        record = cur.fetchone()
        if record:
            self.id = record[0]
        return record

    def save(self):
        connection = Connection()
        conn = connection.get_connection()
        cur = conn.cursor()
        cur.execute(f"INSERT INTO public.netimoveis (imovelsan_id, datahora, datahoraultimoatualisacao, grupoimovel_id, status_id, idadeimovel, tipoimovel1_id,         tipoimovel2_id, tipoimovel1, tipoimovel1al, tipoimovel2, tipoimovel2al, nomearquivo, nomearquivothumb,         valorimovel, valorimovelformat, valorlocacao, valorlocacaoformat, valorcondominio, valorcondominioformat,         valoriptu, valoriptuformat, exibelocacao, exibevenda, transacaolocacao, transacaosigla, logradouropublico,logradouroautocomplete_url, tipologradouro, logradouroautocomplete, transacaovenda, flagobras, estado_id,         siglaestado, nomeestado, nomeestadoal, cidade_id, nomecidade, nomecidadeal, regiao_id, nomeregiao, bairro1_id,         bairro2_id, nomebairro, nomeregiaoal, nomebairroal, nomebairro2al, descricao, descricaoal, arearealprivativa,         metragem, latitude2, longitude2, agenciasan_id, celula_id, textocomplementar, pontuacao, semfiador, embed360,         embedvideo, parcelaiptu, isentoiptu, vagasgaragem, flagfinanciamento, quartos, banho, vagagaragem, suites, varanda, dce, piscina, playground, flaghabites, churrasqueira, portariapermanente, elevadorsocial,         quadradeesporte, academia, salaodefestas, salaodejogos, sauna, jardim, mobiliado, cameraseguranca, guarita,         gascanalizado, interfone, proximoescolainfantil, proximofaculdade, proximofarmacia, proximohospital,         proximomercado, sistemadealarme, proximometro, tag, textoanuncio, complemento, nomecondominio,         nomecondominio_url, banhos, areaconstruida, frentelote, areaexternaprivativa, arealote, numerodepavimentos,         unidadesporandar, totaunidades, sala, flagdestaque, flagimovelocupado, prediovazado, aquecimentosolar,         arcondicionado, portaoeletronico, circuitodetv, elevadorcodificado, elevadordeservico, quartodedespejo,         quartodemotorista, esquadriasdealuminio, salademassagem, hallsocialdecorado, janelacomvenezianas, soldamanha,         terrenomarinhaforeiro, laudemio, terrenomarinhaocupante, medidordeaguaindividual, rampaparacadeirante,         vistaparaomar, andaralto, aguaencanada, aquecedor, arcondicionadocentral, armariobanheiro, armariocozinha,        armarioembutido, armarioquarto, banheira, bicicletario, canil, caseiro, closet, deck, disponivel, escritorio,        espacozen, estacionamentocoberto, estacionamentocommanobrista, estacionamentovagademarcada,         estacionamentovisitante, habites, idealparaagricultura, lareira, lavabo, medidordegasindividual, mezanino,         permiteanimais, permutaimovel, pocoartesiano, pomar, proximocosta, proximopadaria, proximoparque, proximoponto,         proximorestaurante, quadrafutebol, quadratenis, quantidadedevaga, restaurante, silo, sistemacombateincendio,         sobreloja, spa, vagacompartilhadapresa, vagalivre, vagaparadeficiente, vestiario, vistamar, vistamontanha,         acessivel, paisnome, paisurl, pais_id, locale, culturecurrency, desctopografia, datafimobra, descricaovagas,         fachadafrontal, fachadalateral, aproveitamento, arearealprivativacoberta, arearealprivativadescoberta,        telefonecontato, emailcontato, flagmostrartelefonepadrao, grupoimovel, nomecelula, imovelmatriz, paramtransacao, urldetalheimovel) VALUES('{self.imovelsan_id}','{self.datahora}','{self.datahoraultimoatualisacao}','{self.grupoimovel_id}','{self.status_id}','{self.idadeimovel}','{self.tipoimovel1_id}','{self.tipoimovel2_id}','{self.tipoimovel1}','{self.tipoimovel1al}','{self.tipoimovel2}','{self.tipoimovel2al}','{self.nomearquivo}','{self.nomearquivothumb}','{self.valorimovel}','{self.valorimovelformat}','{self.valorlocacao}','{self.valorlocacaoformat}','{self.valorcondominio}','{self.valorcondominioformat}','{self.valoriptu}','{self.valoriptuformat}','{self.exibelocacao}','{self.exibevenda}','{self.transacaolocacao}','{self.transacaosigla}','{self.logradouropublico}','{self.logradouroautocomplete_url}','{self.tipologradouro}','{self.logradouroautocomplete}','{self.transacaovenda}','{self.flagobras}','{self.estado_id}','{self.siglaestado}','{self.nomeestado}','{self.nomeestadoal}','{self.cidade_id}','{self.nomecidade}','{self.nomecidadeal}','{self.regiao_id}','{self.nomeregiao}','{self.bairro1_id}','{self.bairro2_id}','{self.nomebairro}','{self.nomeregiaoal}','{self.nomebairroal}','{self.nomebairro2al}','{self.descricao}','{self.descricaoal}','{self.arearealprivativa}','{self.metragem}','{self.latitude2}','{self.longitude2}','{self.agenciasan_id}','{self.celula_id}','{self.textocomplementar}','{self.pontuacao}','{self.semfiador}','{self.embed360}','{self.embedvideo}','{self.parcelaiptu}','{self.isentoiptu}','{self.vagasgaragem}','{self.flagfinanciamento}','{self.quartos}','{self.banho}','{self.vagagaragem}','{self.suites}','{self.varanda}','{self.dce}','{self.piscina}','{self.playground}','{self.flaghabites}','{self.churrasqueira}','{self.portariapermanente}','{self.elevadorsocial}','{self.quadradeesporte}','{self.academia}','{self.salaodefestas}','{self.salaodejogos}','{self.sauna}','{self.jardim}','{self.mobiliado}','{self.cameraseguranca}','{self.guarita}','{self.gascanalizado}','{self.interfone}','{self.proximoescolainfantil}','{self.proximofaculdade}','{self.proximofarmacia}','{self.proximohospital}','{self.proximomercado}','{self.sistemadealarme}','{self.proximometro}','{self.tag}','{self.textoanuncio}','{self.complemento}','{self.nomecondominio}','{self.nomecondominio_url}','{self.banhos}','{self.areaconstruida}','{self.frentelote}','{self.areaexternaprivativa}','{self.arealote}','{self.numerodepavimentos}','{self.unidadesporandar}','{self.totaunidades}','{self.sala}','{self.flagdestaque}','{self.flagimovelocupado}','{self.prediovazado}','{self.aquecimentosolar}','{self.arcondicionado}','{self.portaoeletronico}','{self.circuitodetv}','{self.elevadorcodificado}','{self.elevadordeservico}','{self.quartodedespejo}','{self.quartodemotorista}','{self.esquadriasdealuminio}','{self.salademassagem}','{self.hallsocialdecorado}','{self.janelacomvenezianas}','{self.soldamanha}','{self.terrenomarinhaforeiro}','{self.laudemio}','{self.terrenomarinhaocupante}','{self.medidordeaguaindividual}','{self.rampaparacadeirante}','{self.vistaparaomar}','{self.andaralto}','{self.aguaencanada}','{self.aquecedor}','{self.arcondicionadocentral}','{self.armariobanheiro}','{self.armariocozinha}','{self.armarioembutido}','{self.armarioquarto}','{self.banheira}','{self.bicicletario}','{self.canil}','{self.caseiro}','{self.closet}','{self.deck}','{self.disponivel}','{self.escritorio}','{self.espacozen}','{self.estacionamentocoberto}','{self.estacionamentocommanobrista}','{self.estacionamentovagademarcada}','{self.estacionamentovisitante}','{self.habites}','{self.idealparaagricultura}','{self.lareira}','{self.lavabo}','{self.medidordegasindividual}','{self.mezanino}','{self.permiteanimais}','{self.permutaimovel}','{self.pocoartesiano}','{self.pomar}','{self.proximocosta}','{self.proximopadaria}','{self.proximoparque}','{self.proximoponto}','{self.proximorestaurante}','{self.quadrafutebol}','{self.quadratenis}','{self.quantidadedevaga}','{self.restaurante}','{self.silo}','{self.sistemacombateincendio}','{self.sobreloja}','{self.spa}','{self.vagacompartilhadapresa}','{self.vagalivre}','{self.vagaparadeficiente}','{self.vestiario}','{self.vistamar}','{self.vistamontanha}','{self.acessivel}','{self.paisnome}','{self.paisurl}','{self.pais_id}','{self.locale}','{self.culturecurrency}','{self.desctopografia}','{self.datafimobra}','{self.descricaovagas}','{self.fachadafrontal}','{self.fachadalateral}','{self.aproveitamento}','{self.arearealprivativacoberta}','{self.arearealprivativadescoberta}','{self.telefonecontato}','{self.emailcontato}','{self.flagmostrartelefonepadrao}','{self.grupoimovel}','{self.nomecelula}','{self.imovelmatriz}','{self.paramtransacao}','{self.urldetalheimovel}');")

    def migrate(self):
        connection = Connection()
        conn = connection.get_connection()
        cur = conn.cursor()
        sql = "CREATE TABLE IF NOT EXISTS public.netimoveis (	id serial NOT NULL,	imovelsan_id int4 NULL,	datahora timestamp NULL,	datahoraultimoatualisacao varchar(255) NULL,	grupoimovel_id int4 NULL,	status_id int4 NULL,	idadeimovel int4 NULL,	tipoimovel1_id int4 NULL,	tipoimovel2_id int4 NULL,	tipoimovel1 varchar(255) NULL,	tipoimovel1al varchar(255) NULL,	tipoimovel2 varchar(255) NULL,	tipoimovel2al varchar(255) NULL,	nomearquivo varchar(255) NULL,	nomearquivothumb text NULL,	valorimovel numeric(13,2) NULL,	valorimovelformat varchar(200) NULL,	valorlocacao numeric(13,2) NULL,	valorlocacaoformat varchar(200) NULL,	valorcondominio numeric(13,2) NULL,	valorcondominioformat varchar(200) NULL,	valoriptu numeric(13,2) NULL,	valoriptuformat varchar(200) NULL,	exibelocacao int4 NULL,	exibevenda int4 NULL,	transacaolocacao int4 NULL,	transacaosigla varchar(20) NULL,	logradouropublico varchar(255) NULL,	logradouroautocomplete_url varchar(255) NULL,	tipologradouro varchar(20) NULL,	logradouroautocomplete varchar(255) NULL,	transacaovenda int4 NULL,	flagobras bool NULL,	estado_id int4 NULL,	siglaestado bpchar(2) NULL,	nomeestado varchar(255) NULL,	nomeestadoal varchar(255) NULL,	cidade_id int4 NULL,	nomecidade varchar(200) NULL,	nomecidadeal varchar(200) NULL,	regiao_id int4 NULL,	nomeregiao varchar(255) NULL,	bairro1_id int4 NULL,	bairro2_id int4 NULL,	nomebairro varchar(255) NULL,	nomeregiaoal varchar(255) NULL,	nomebairroal varchar(255) NULL,	nomebairro2al varchar(255) NULL,	descricao varchar(255) NULL,	descricaoal varchar(255) NULL,	arearealprivativa numeric(13,2) NULL,	metragem varchar(20) NULL,	latitude2 varchar(255) NULL,longitude2 varchar(255) NULL,	agenciasan_id int4 NULL,	celula_id int4 NULL,	textocomplementar text NULL,	pontuacao numeric(13,2) NULL,	semfiador int4 NULL,	embed360 varchar(255) NULL,	embedvideo varchar(255) NULL,	parcelaiptu int4 NULL,	isentoiptu bool NULL,	vagasgaragem varchar(10) NULL,	flagfinanciamento bool NULL,	quartos int4 NULL,	banho int4 NULL,	vagagaragem int4 NULL,	suites int4 NULL,	varanda int4 NULL,	dce int4 NULL,	piscina bool NULL,	playground bool NULL,	flaghabites bool NULL,	churrasqueira bool NULL,	portariapermanente bool NULL,	elevadorsocial bool NULL,	quadradeesporte bool NULL,	academia bool NULL,	salaodefestas bool NULL,	salaodejogos bool NULL,	sauna bool NULL,	jardim bool NULL,	mobiliado bool NULL,	cameraseguranca bool NULL,	guarita bool NULL,	gascanalizado bool NULL,	interfone bool NULL,	proximoescolainfantil bool NULL,	proximofaculdade bool NULL,	proximofarmacia bool NULL,	proximohospital bool NULL,	proximomercado bool NULL,	sistemadealarme bool NULL,	proximometro bool NULL,	tag text NULL,	textoanuncio varchar(255) NULL,	complemento varchar(255) NULL,	nomecondominio varchar(255) NULL,nomecondominio_url varchar(255) NULL,	banhos int4 NULL,	areaconstruida numeric(13,2) NULL,	frentelote numeric(13,2) NULL,	areaexternaprivativa numeric(13,2) NULL,	arealote numeric(13,2) NULL,	numerodepavimentos int4 NULL,	unidadesporandar int4 NULL,	totaunidades int4 NULL,	sala int4 NULL,	flagdestaque bool NULL,	flagimovelocupado bool NULL,	prediovazado bool NULL,	aquecimentosolar bool NULL,	arcondicionado bool NULL,	portaoeletronico bool NULL,	circuitodetv bool NULL,	elevadorcodificado bool NULL,	elevadordeservico bool NULL,	quartodedespejo bool NULL,	quartodemotorista bool NULL,	esquadriasdealuminio bool NULL,	salademassagem bool NULL,	hallsocialdecorado bool NULL,	janelacomvenezianas bool NULL,	soldamanha bool NULL,	terrenomarinhaforeiro bool NULL,	laudemio bool NULL,	terrenomarinhaocupante bool NULL,	medidordeaguaindividual bool NULL,	rampaparacadeirante bool NULL,	vistaparaomar bool NULL,	andaralto bool NULL,	aguaencanada bool NULL,	aquecedor bool NULL,	arcondicionadocentral bool NULL,	armariobanheiro bool NULL,	armariocozinha bool NULL,	armarioembutido bool NULL,	armarioquarto bool NULL,	banheira bool NULL,	bicicletario bool NULL,	canil bool NULL,	caseiro bool NULL,	closet bool NULL,	deck bool NULL,	disponivel bool NULL,	escritorio bool NULL,	espacozen bool NULL,	estacionamentocoberto bool NULL,	estacionamentocommanobrista bool NULL,	estacionamentovagademarcada bool NULL,	estacionamentovisitante bool NULL,	habites bool NULL,	idealparaagricultura bool NULL,	lareira bool NULL,	lavabo bool NULL,	medidordegasindividual bool NULL,	mezanino bool NULL,	permiteanimais bool NULL,	permutaimovel bool NULL,	pocoartesiano bool NULL,	pomar bool NULL,	proximocosta bool NULL,	proximopadaria bool NULL,	proximoparque bool NULL,	proximoponto bool NULL,	proximorestaurante bool NULL,	quadrafutebol bool NULL,	quadratenis bool NULL,	quantidadedevaga bool NULL,	restaurante bool NULL,	silo bool NULL,	sistemacombateincendio bool NULL,	sobreloja bool NULL,	spa bool NULL,	vagacompartilhadapresa bool NULL,	vagalivre bool NULL,	vagaparadeficiente bool NULL,	vestiario bool NULL,	vistamar bool NULL,	vistamontanha bool NULL,	acessivel bool NULL,	paisnome varchar(20) NULL,	paisurl varchar(20) NULL,	pais_id int4 NULL,	locale varchar(255) NULL,	culturecurrency varchar(255) NULL,	desctopografia varchar(255) NULL,	datafimobra varchar(255) NULL,	descricaovagas varchar(255) NULL,	fachadafrontal varchar(255) NULL,	fachadalateral varchar(255) NULL,	aproveitamento varchar(255) NULL,	arearealprivativacoberta varchar(255) NULL,	arearealprivativadescoberta varchar(255) NULL,	telefonecontato varchar(255) NULL,	emailcontato varchar(255) NULL,	flagmostrartelefonepadrao bool NULL,	grupoimovel varchar(255) NULL,	nomecelula varchar(255) NULL,	imovelmatriz bool NULL,	paramtransacao varchar(20) NULL,	urldetalheimovel varchar(255) NULL);"
        cur.execute(sql)


class NetimovelFactory:
    @staticmethod
    def get_netimovel() -> NetimovelAbstract:
        return Netimovel()


# if __name__ == '__main__':
#      imovel = NetimovelFactory.get_netimovel()
#      imovel.id = 1
#      print(imovel)