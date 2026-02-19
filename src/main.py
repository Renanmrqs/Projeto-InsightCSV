from langchain.chat_models import init_chat_model
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
import pandas as pd
import streamlit as st
load_dotenv()


st.title('InsightCSV')

envio_arquivo = st.file_uploader(
    'Envie seu arquivo CSV', accept_multiple_files=False, type='csv')

st.warning('Esse é um projeto de estudo. Fique atento ao limite de arquivos enviados. Os arquivos estão sendo enviados para o Google Gemini. Não nos responsabilizamos pelo seu arquivo.')
botao_buscar = st.button('Analisar Arquivo')


caminho = envio_arquivo
llm = init_chat_model('google_genai:gemini-2.5-flash')


def analise_dados(caminho=caminho):
    caminho.seek(0)
    dados = pd.read_csv(caminho, encoding='latin')
    colunas_texto = dados.select_dtypes(
        include=['object']).columns.to_list()
    return dados, colunas_texto

if envio_arquivo is not None:
    st.divider()
    a, b, c = st.columns(3)
    dados, colunas_texto = analise_dados()
    
    a.metric('Linhas', dados.shape[0], border=True)
    b.metric('Colunas', dados.shape[1], border=True)
    c.metric('Duplicadas', dados.duplicated().sum(), border=True)
    st.dataframe(dados.head())

def buscar():
    if envio_arquivo is None:
        return None
    
    try:
        dados, colunas_texto = analise_dados()
        dados_organizados = dados[colunas_texto].head(50).to_markdown()
        instrucao_maquina = f'Voce e um analista de dados senior, use os dados tecnicos abaixo para responder as duvidas do usuario com precisão. DADOS DO CSV:{dados_organizados}'
        pergunta_usuario = 'Analise esse arquivo, caso ele tenha algum erro, fale sobre ele e resuma o arquivo, caso contrario apenas resuma.'

        mensagens = [
            SystemMessage(content=instrucao_maquina),
            HumanMessage(content=pergunta_usuario)
        ]
        return mensagens

    except Exception as e:
        return 'erro'


if 'analise_ia' not in st.session_state:
    st.session_state.analise_ia = None

if botao_buscar:
    if envio_arquivo is not None:
        with st.spinner('Analisando...'):
            resultado_busca = buscar()

        if resultado_busca == 'erro':
            st.error('Erro ao ler o arquivo. Por favor verifique o formato.')
        elif resultado_busca is not None:
            resposta = llm.invoke(resultado_busca)
            st.session_state.analise_ia = resposta.content
    else:
        st.warning('Por favor, Envie um arquivo CSV.')

if st.session_state.analise_ia:
    st.subheader('Arquivo analisado: ')
    st.info(st.session_state.analise_ia)
