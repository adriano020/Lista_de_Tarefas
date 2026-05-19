import streamlit as st

st.title("Lista de Tarefas")

#Criar lista na memoria

if "tarefas" not in st.session_state:
    st.session_state.tarefas = []

#Campo de texto
nova_tarefa = st.text_input("Digite uma tarefa")

#Botao Adicionar
if st.buton("Adicionar"):

    if nova_tarefa != "":

        tarefa = {
            "nome": nova_tarefa,
            "concluida": False
        }
        st.session_state.tarefas.append(tarefa)

#verificação de campo vazio
if st.button("adicionar"):

    if nova_tarefa != "":

        tarefa = {
            "nome": nova_tarefa,
            "concluida": False
        }
        st.session_state.tarefas.append(tarefa)

#Criando Dicionario

if st.button("adicionar"):

    if nova_tarefa != "":

        tarefa = {
            "nome": nova_tarefa,
            "concluida": False
        }
        st.session_state.tarefas.append(tarefa)

#Adicionar na lista

if st.button("adicionar"):

    if nova_tarefa != "":

        tarefa = {
            "nome": nova_tarefa,
            "concluida": False
        }
        st.session_state.tarefas.append(tarefa)

#Subtitulo

st.subheader("Minhas Tarefas")

for i, tarefa in enumerate(st.session_state.tarefas):

#Estrutura de reptição

st.subheader("Minhas Tarefas")

for i, tarefa in enumerate(st.session_state.tarefas):
    col1, col2 = st.columns([5, 1])

    with col1:
        concluida = st.checkbox(
            tarefa["nome"],
            value = tarefa["concluida"]
            key = i
        )

        tarefa["concluida"] = concluida
    
    with col2:
        if st.button("x", key=f["delete{i}"]):
            st.session_state.tarefas.pop("i")
            st.rerun()
