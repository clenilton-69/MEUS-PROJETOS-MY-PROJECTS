import streamlit as st

st.set_page_config(page_title="Dicas Empresariais", layout="wide")

pagina = st.sidebar.radio("Navegue pelo app", ["Início", "Marketing", "Financeiro", "Equipe"])

if pagina == "Início":
    st.title("💼 DICAS EMPRESARIAIS")
    st.markdown("💡 Aqui você encontra estratégias para impulsionar seu negócio")
    st.write('Onde você pode encontrar dicas valiosas para o seu negócio, desde estratégias de marketing até gestão financeira.')
    st.image("stonks.jpg", use_container_width=True)
    st.markdown("**Quem Desenvolveu o Projeto Foi:**")
    st.write("**Rafael de Paula**")
    st.write("**Gustavo de Antony**")
    st.write("**Gabriel Silva**")

elif pagina == "Marketing":
    st.title("📣 Estratégias de Marketing")
    st.image("marketing.jpg", use_container_width=True)
    st.write("Dicas para atrair mais clientes e fortalecer sua marca.")

elif pagina == "Financeiro":
    st.title("💰 Gestão Financeira")
    st.image("finacias.jpg", use_container_width=True)
    st.write("Controle de custos, fluxo de caixa e planejamento financeiro.")

elif pagina == "Equipe":
    st.title("👨‍💻 Equipe do Projeto")
    st.image("equipe.jpg", use_container_width=True)
    st.write("Conheça quem está por trás do projeto.")