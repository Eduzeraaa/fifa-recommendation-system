import streamlit as st
import pandas as pd
import plotly.express as px
from parser_llm import parser
from llm_response import resposta_chatbot


st.title('Dashboard FIFA 23')
df = pd.read_csv('FIFA23_official_data.csv')
df = df[~df['Position'].isin(['RES', 'SUB'])]



tab1, tab2, tab3 = st.tabs(['Faixa de Overall', 'Tops', 'Sugestão de Jogador'])

with tab1:

    bins = [0, 60, 70, 80, 90, 100]

    labels = ['0-60', '61-70', '71-80', '81-90', '91-99']

    df['Faixa de Overall'] = pd.cut(df['Overall'], bins=bins, labels=labels) #!Criar coluna com faixas

    contagem = df['Faixa de Overall'].value_counts().sort_index()

    fig = px.bar(contagem, text_auto=True)
    
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)

    st.plotly_chart(fig)


with tab2:

    tab2_1, tab2_2, tab2_3, tab2_4 = st.tabs(['Mais Caros', 'Mais Overall', 'Melhores por posição', 'Maiores potenciais'])

    with tab2_1:

        st.subheader('Top 50 jogadores mais caros')

        df['Valor'] = df['Value'].str.replace('€', '', regex=False)

        df['Valor'] = df['Valor'].str.replace('M', '', regex=False)
        df['Valor'] = df['Valor'].str.replace('K', '', regex=False)

        df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')

        df.loc[df['Value'].str.contains('M'), 'Valor'] *= 1_000_000
        top50 = df[['Name', 'Valor', 'Overall', 'Age', 'Nationality', 'Club']].nlargest(50, 'Valor').reset_index(drop=True)

        st.write(top50)

    with tab2_2:
        
        st.subheader('Top 50 jogadores com mais overall')

        top50 = df[['Name', 'Overall', 'Valor', 'Age', 'Nationality', 'Club']].nlargest(50, 'Overall').reset_index(drop=True)

        st.write(top50)

    with tab2_3: #! melhores por posicao

        posicoes = pd.DataFrame({
            'Posicao': ['Escolha uma posição','Goleiro', 'Zagueiro', 'Lateral Direito', 'Lateral Esquerdo', 'Volante', 'Meio Campo', 'Ponta Direita', 'Ponta Esquerda', 'Atacante']
        })

        posicao = st.selectbox('Escolha a posição:', posicoes['Posicao'])

        if posicao == 'Goleiro': 
            st.subheader('Top 10 Goleiros')
            goleiros = df[df['Position'].str.contains('GK', na=False)]
            top10 = goleiros[['Name', 'Valor', 'Overall', 'Age', 'Nationality', 'Club']].nlargest(10, 'Overall').reset_index(drop=True)

            st.write(top10)

        if posicao == 'Zagueiro': 

            st.subheader('Top 10 zagueiros')
            zagueiros = df[df['Position'].str.contains('CB', na=False)]
            top10 = zagueiros[['Name', 'Valor', 'Overall', 'Age', 'Nationality', 'Club']].nlargest(10, 'Overall').reset_index(drop=True)

            st.write(top10)

        if posicao == 'Lateral Direito': 

            st.subheader('Top 10 Laterais Direitos')

            lat_dir = df[df['Position'].str.contains('RB' or 'RWB', na=False)]
            top10 = lat_dir[['Name', 'Valor', 'Overall', 'Age', 'Nationality', 'Club']].nlargest(10, 'Overall').reset_index(drop=True)

            st.write(top10)

        if posicao == 'Lateral Esquerdo': 
            
            st.subheader('Top 10 Laterais Esquerdos')

            lat_esq = df[df['Position'].str.contains('LB' or 'LWB', na=False)]
            top10 = lat_esq[['Name', 'Valor', 'Overall', 'Age', 'Nationality', 'Club']].nlargest(10, 'Overall').reset_index(drop=True)

            st.write(top10)

        if posicao == 'Volante':

            st.subheader('Top 10 volantes')

            volante = df[df['Position'].str.contains('CDM', na=False)]
            top10 = volante[['Name', 'Valor', 'Overall', 'Age', 'Nationality', 'Club']].nlargest(10, 'Overall').reset_index(drop=True)

            st.write(top10)

        if posicao == 'Meio Campo': 

            st.subheader('Top 10 Meio campistas')

            mc = df[df['Position'].str.contains('CM' or 'CAM', na=False)]
            top10 = mc[['Name', 'Valor', 'Overall', 'Age', 'Nationality', 'Club']].nlargest(10, 'Overall').reset_index(drop=True)

            st.write(top10)

        if posicao == 'Ponta Direita': 
            
            st.subheader('Top 10 Pontas Esquerdas')

            ponta_esq = df[df['Position'].str.contains('LW', na=False)]
            top10 = ponta_esq[['Name', 'Valor', 'Overall', 'Age', 'Nationality', 'Club']].nlargest(10, 'Overall').reset_index(drop=True)

            st.write(top10)

        if posicao == 'Ponta Esquerda':

            st.subheader('Top 10 Pontas Direitas')

            ponta_dir = df[df['Position'].str.contains('RW', na=False)]
            top10 = ponta_dir[['Name', 'Valor', 'Overall', 'Age', 'Nationality', 'Club']].nlargest(10, 'Overall').reset_index(drop=True)

            st.write(top10)

        if posicao == 'Atacante':

            st.subheader('Top 10 Atacantes')

            atacante = df[df['Position'].str.contains('ST' or 'CF', na=False)]
            top10 = atacante[['Name', 'Valor', 'Overall', 'Age', 'Nationality', 'Club']].nlargest(10, 'Overall').reset_index(drop=True)

            st.write(top10)



    with tab2_4: #! potencial geral / ganho de over

        modos = pd.DataFrame({
            'Modo': ['Escolha um modo','Geral', 'Ganho de Overall']
        })

        modo = st.selectbox('Escolha o modo', modos['Modo'])

        if modo == 'Geral':

            st.subheader('Top 50 maiores potenciais')

            top50 = df[['Name', 'Overall', 'Potential', 'Value', 'Age', 'Nationality', 'Club']].nlargest(50, 'Potential').reset_index(drop=True)

            st.write(top50)

        if modo == 'Ganho de Overall':

            st.subheader('Top 50 jogadores que mais ganharão overall')

            df['Geral'] = pd.to_numeric(df['Overall'])
            df['Potencial'] = pd.to_numeric(df['Potential'])

            df['Ganho de Overall'] = df['Potencial'] - df['Geral']

            top50 = df[['Name', 'Overall', 'Potential', 'Ganho de Overall', 'Value', 'Age', 'Nationality', 'Club']].nlargest(50, 'Ganho de Overall').reset_index(drop=True)

            st.write(top50)


df["Score"] = (df["Overall"] * 0.65 + df["Potential"] * 0.5 - df["Age"] * 0.7 - (df["Valor"] / 1_000_000) * 0.3)

score = df['Score']


with tab3: #! chatbot
    st.subheader('Qual jogador eu devo contratar?')
    df['Geral'] = pd.to_numeric(df['Overall'])
    df['Potencial'] = pd.to_numeric(df['Potential'])
    df['Ganho de Overall'] = df['Potencial'] - df['Geral']

    if "messages" not in st.session_state:
        st.session_state.messages = []

    chat_container = st.container()
    mapa_posicoes = {
                "goleiro": ["GK"],
                "zagueiro": ["CB", "LCB", "RCB"],
                "lateral direito": ["RB", "RWB"],
                "lateral esquerdo": ["LB", "LWB"],
                "volante": ["CDM", "LDM", "RDM"],
                "meia": ["CM", "CAM", "LCM", "RCM"],
                "ponta esquerda": ["LW", "LM"],
                "ponta direita": ["RW", "RM"],
                "atacante": ["ST", "CF", "RS", "LS"]
            }

    if prompt := st.chat_input('Digite sua mensagem, contendo seu orçamento (em euros) e a posição desejada: '):
        with chat_container:
            st.session_state.messages.append({"role": "user", "content": prompt})
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])
    

            try:

                obj_mensagem = parser(prompt)
                orcamento = obj_mensagem.orcamento
                posicao = obj_mensagem.posicao.lower().strip()



                df['Position'] = df['Position'].str.split('>').str[-1].str.strip()


                df_filtrado = df[(df['Valor'] <= orcamento) & (df['Position'].isin(mapa_posicoes[posicao]))]

                resposta_chat = resposta_chatbot(st.session_state.messages, df_filtrado, prompt)
                st.chat_message("assistant").markdown(resposta_chat)
                st.session_state.messages.append({"role": "assistant", "content": resposta_chat})


            except Exception as e:
                st.error(e)

