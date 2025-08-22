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
    st.markdown("OS 4PS DO MARKETING")
    st.write('O marketing se baseia no conceito dos 4Ps para verificar as informações primárias do cliente, para então analisar soluções viáveis em cada negócio. Esse nome existe pelo fato de as informações estarem divididas em 4 pilares básicos das estratégias. Eles são referentes as seguintes palavras iniciadas com a letra “P”:')

    st.write('- 👜Produto: apesar do nome, deve-se incluir também os serviços ofertados. Dentro de produto deve-se incluir as características do que é vendido. É preciso definir quais as necessidades que o produto resolve, como ele é, como funciona e onde será utilizado. ')

    st.write('- 💲Preço: é preciso definir o valor do produto, como ele será pago, quais as condições de pagamento e se haverá descontos. O preço deve ser competitivo e atrativo para o cliente, mas também rentável para a empresa.')

    st.write('- 🏪Praça: é o local onde o produto será vendido, que pode ser uma loja física, um site de e-commerce ou uma plataforma de redes sociais. É importante escolher os canais de venda mais adequados para o público-alvo e garantir que o produto esteja disponível onde o cliente espera encontrá-lo.')

    st.write('- ⚠️Promoção: envolve as estratégias de divulgação e comunicação do produto, como publicidade, promoções, eventos e redes sociais. O objetivo é atrair a atenção do cliente, gerar interesse e estimular a compra. É importante escolher os canais de promoção mais adequados para o público-alvo e criar mensagens que ressoem com suas necessidades e desejos.')

    st.markdown('**E Porque o Marketing é tão importante?**')

    st.write('- 📱Atrai clientes e aumenta as vendas')
    st.write('- 💻Constrói a imagem da marca')
    st.write('- 📈Ajuda a entender o mercado e a concorrência')
    st.write('- 🛜Conecta com outras áreas da empresa, como vendas e atendimento.')
    st.image("marketing.jpg", use_container_width=True)

elif pagina == "Financeiro":
    st.title("💰 Gestão Financeira")
    st.write('Nos países em desenvolvimento há um grande número de micro e pequenas empresas em fase de expansão. Porém, nem sempre vivemos em bonança. Há também períodos de recessão, como o que parece nos assombrar atualmente, no qual quem não estiver devidamente preparado, e ciente de que é preciso ter uma boa gestão financeira, terá dificuldades em se manter no mercado.')

    st.write('A gestão financeira é o processo de planejamento, organização, direção e controle dos recursos financeiros de uma empresa. Ela envolve a análise e o controle das receitas e despesas, a elaboração de orçamentos, a gestão do fluxo de caixa e a tomada de decisões financeiras estratégicas.')

    st.markdown('**💼 Por que e Impotante o Financimento da Empresa**')

    st.write('- 📊 Ajuda a tomar decisões informadas: A gestão financeira fornece dados e informações que ajudam os gestores a tomar decisões estratégicas, como investimentos, cortes de custos e expansão.')

    st.write('- 💰 Melhora a rentabilidade: Uma boa gestão financeira ajuda a identificar oportunidades de redução de custos e aumento de receitas, melhorando a rentabilidade da empresa.')

    st.write('- 📈 Aumenta a eficiência operacional: A gestão financeira ajuda a identificar ineficiências nos processos e a implementar melhorias, aumentando a eficiência operacional da empresa.')

    st.write('- 📉 Reduz riscos financeiros: A gestão financeira ajuda a identificar e gerenciar riscos financeiros, como flutuações de mercado, inadimplência de clientes e variações cambiais.')

    st.write('- 📅 Melhora o planejamento: A gestão financeira ajuda a elaborar orçamentos e projeções financeiras, permitindo um planejamento mais eficaz e estratégico.')
    st.image("finacias.jpg", use_container_width=True)

elif pagina == "Equipe":
    st.title("👨‍💻 Equipe do Projeto")
    st.markdown('Monte uma Equipe Alinhada e Motivada')

    st.write('- 🤑Contrate com Propósito:\n Contratar com propósito ajuda a formar equipes alinhadas com os valores da empresa, aumentando o engajamento, a produtividade e a retenção de talentos. É uma forma inteligente de fortalecer a cultura e garantir crescimento sustentável')

    st.write('- 🤑 Invista em Capacitação:\n Profissionais bem treinados trabalham com mais eficiência, cometem menos erros e se sentem mais motivados. Além disso, a capacitação estimula a inovação, fortalece a cultura de aprendizado e ajuda a reter talentos, criando um ambiente mais produtivo e competitivo.')

    st.write('- 🤑 Crie uma cultura colaborativa:\n Criar uma cultura colaborativa é bom para a equipe porque promove um ambiente onde todos se sentem valorizados, compartilham ideias e trabalham juntos em busca de objetivos comuns. Isso fortalece o espírito de equipe, melhora a comunicação, aumenta a produtividade e estimula a inovação. Quando a colaboração é parte do dia a dia, os resultados são mais consistentes e o clima organizacional se torna mais positivo.')

    st.write('- 🤑 Lidere com empatia:\n Ser um líder com empatia é mais do que apenas ser gentil é sobre criar conexões reais, compreender as emoções dos outros e agir com sensibilidade e respeito. Esse estilo de liderança tem ganhado destaque por transformar ambientes de trabalho e fortalecer equipes de maneira profunda e duradoura ')

    st.write('- 🤑 Esse ditado bastante popular nos esportes coletivos pode ser muito bem aplicado no meio corporativo. Para que uma equipe de alta performance alcance seus objetivos, o caminho mais lógico é o do apoio e da colaboração, justamente pelas vantagens que isso pode trazer para o time.')
    st.image("equipe.jpg", use_container_width=True)