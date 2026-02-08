import streamlit as st
import google.generativeai as genai

# Configuração da página
st.set_page_config(page_title="Viralizar Instagram", page_icon="🚀")
st.title("🚀 Gerador de Conteúdo Viral")

# Aqui você cola sua API KEY que pegou no AI Studio
# Para teste rápido, você pode colar entre as aspas, 
# mas o ideal é usar os 'Secrets' do Streamlit depois.
api_key = st.sidebar.text_input("Cole sua API Key do Gemini aqui:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt_usuario = st.text_input("Sobre o que você quer criar um post hoje?")

    if st.button("Gerar Ideias"):
        if prompt_usuario:
            response = model.generate_content(f"Crie um post viral para Instagram sobre: {prompt_usuario}")
            st.write(response.text)
        else:
            st.warning("Por favor, digite um tema.")
else:
    st.info("Por favor, insira sua API Key na barra lateral para começar.")
