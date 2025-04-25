#python -m streamlit run form.py funcionamento da biblioteca
import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Tecnologia e a saúde física", layout="wide")

app_mode = st.sidebar.selectbox("Selecione a página", ["Pesquisa", "Resultados", "Compare os resultados"])

if app_mode == "Pesquisa":
    st.title("Os efeitos do Uso Excessivo de Tecnologia na Saúde Física")
    st.markdown("""
        <div style="font-size: 16px;">
            A tecnologia se tornou uma parte essencial do nosso dia a dia, transformando a maneira como trabalhamos, estudamos, nos divertimos e nos comunicamos. 
            No entanto, o uso excessivo e contínuo de dispositivos digitais pode ter consequências prejudiciais para a nossa saúde física. Dores nas costas, 
            cansaço visual, dores de cabeça e problemas posturais são apenas alguns dos desconfortos que muitos de nós enfrentamos devido ao tempo prolongado em 
            frente às telas.<br></br>
            Este estudo busca compreender como o uso de tecnologias impacta a saúde física das pessoas, explorando fatores como faixa etária, escolaridade, 
            renda e hábitos de atividade física. Através das respostas ao questionário, esperamos coletar dados valiosos para ajudar a identificar padrões e 
            promover melhores práticas no uso de tecnologias, visando à preservação do bem-estar físico.<br></br>
        </div>
        """, unsafe_allow_html=True)
    st.image("img\Capa_Form.png")

    sexo = st.radio("Gênero:",[
        "Masculino", "Feminino", "Outro", "Prefiro não dizer"])

    faixa_etaria = st.radio("Faixa etária:", [
        "Até 12 anos", "Entre 13 e 18 anos", "Entre 19 e 24 anos",
        "Entre 25 e 31 anos", "Entre 32 e 40 anos", "Acima de 40 anos"])

    escolaridade = st.radio("Grau de escolaridade:", [
        "Ensino Fundamental Incompleto", "Ensino Fundamental Completo",
        "Ensino Médio Incompleto", "Ensino Médio Completo",
        "Ensino Superior Incompleto", "Ensino Superior Completo"])

    renda = st.radio("Renda mensal:", [
        "Até 1 salário", "Entre 1 e 3 salários",
        "Entre 3 e 5 salários", "Acima de 5 salários"])

    tecnologias = st.multiselect("Tecnologias que você mais utiliza:", [
        "Smartphone", "Computador", "Tablet", "Câmera", "Eletrodomésticos",
        "Veículo", "Televisão", "Notebook", "Fone", "Outros"])

    motivo_uso = st.radio("Qual o maior motivo para o uso dessas tecnologias no seu dia a dia?", [
        "Trabalho", "Diversão / lazer", "Tédio", "Estudo", "Outro"])

    horas_uso = st.radio("Quantas horas por dia você utiliza essas tecnologias?", [
        "Menos de 3 horas", "Entre 3 horas e 6 horas",
        "Entre 6 horas e 8 horas", "Acima de 8 horas"])

    posicao_uso = st.radio("Durante o uso você permanece muito tempo sentado(a)?", [
        "Sim", "Não"])

    uso_continuo = st.radio("Você as utiliza de forma contínua ou faz pausas?", [
        "Forma contínua", "Faço pausas"])

    atv_fisica = st.radio("Você pratica alguma atividade física regularmente?", [
        "Sim", "Não"])

    frequencia_atividade = None
    if atv_fisica == "Sim":
        frequencia_atividade = st.radio("Se sim, quantas vezes por semana?",[
            "1 vez", "De 2 a 4 vezes", "De 4 a 6 vezes", "Todos os dias"])

    desconforto = st.radio("Você sente algum desconforto físico (dor nas costas, dor de cabeça, cansaço excessivo) relacionado ao uso prolongado de tecnologia?", [
        "Nunca", "Raramente", "De vez em quando", "Regularmente", "Sempre"])

    tipo_desconforto = st.multiselect("Quais são os desconfortos físicos que você sente?", [
        "Dor de cabeça", "Dor nas costas", "Dor muscular",
        "Cansaço excessivo", "Problemas de postura", "Fadiga ocular",
        "Distúrbios do sono", "Dor de ouvido (tímpanos)",
        "Sedentarismo", "Nenhum", "Outros"
    ])

    impacto = st.radio("Você percebe algum impacto no seu desempenho físico (como resistência e força) devido ao seu estilo de vida sedentário, causado pelo uso excessivo de tecnologia?", [
        "Sim", "Não"])

    motivo_continuar = st.radio("Por qual motivo você continua utilizando essas tecnologias, mesmo ciente dos danos físicos que elas podem causar à sua saúde?", [
        "Dependência", "Necessidade", "Isolamento social", 
        "Simplesmente por gostar", "Outros"])

    reduzir_tempo_uso = st.radio("Se fosse necessário, você estaria disposto(a) a reduzir o tempo de uso de tecnologia por motivos de saúde, mesmo que isso afetasse suas atividades de lazer ou trabalho?", [
        "Sim", "Não"])

    motivo_continuar = st.multiselect("Quais mudanças você acredita que poderiam ajudá-lo(a) a reduzir os danos à saúde causados pelo uso excessivo de tecnologia? (marque todas as opções aplicáveis)", [
        "Diminuir o tempo de uso", "Inserir atividades físicas em sua rotina",
        "Musculação", "Ajuda de um profissional fisioterapeuta",
        "Ergonomia (ciência que estuda a interação entre o ser humano e o ambiente de trabalho, com o objetivo de promover o conforto, a segurança e a eficiência)",
        "Outros"])


    if st.button("Enviar respostas"):
        dados = {
            "sexo": sexo,
            "faixa_etaria": faixa_etaria,
            "escolaridade": escolaridade,
            "renda": renda,
            "tecnologias": "; ".join(tecnologias),
            "motivo_uso": motivo_uso,
            "horas_uso": horas_uso,
            "posicao_uso": posicao_uso,
            "uso_continuo": uso_continuo,
            "atv_fisica": atv_fisica,
            "frequencia_atividade": frequencia_atividade if atv_fisica == "Sim" else "Não pratica",
            "desconforto": desconforto,
            "tipo_desconforto": "; ".join(tipo_desconforto),
            "impacto": impacto,
            "motivo_continuar": motivo_continuar,
            "reduzir_tempo_uso": reduzir_tempo_uso,
            "mudancas_necessarias": "; ".join(motivo_continuar),
            "data_envio": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }


        df = pd.DataFrame([dados])

        try:
            with open("respostas_formulario.csv", "a") as f:
                df.to_csv(f, index=False, header=f.tell() == 0)
            st.success("Resposta enviada com sucesso!")
            st.balloons()
        except Exception as e:
            st.error(f"Ocorreu um erro ao salvar os dados: {e}")

        

if app_mode == "Resultados":
    st.title("O que os dados revelam?")

    try:
        df = pd.read_csv("respostas_formulario.csv", encoding="latin1")
    except FileNotFoundError:
        st.warning("Nenhum dado foi enviado ainda.")
        st.stop()

    st.subheader("Faixa etária x Tipo de desconforto")
    sintomas_df = df.copy()
    sintomas_df = sintomas_df.explode("tipo_desconforto")
    sintomas_df["tipo_desconforto"] = sintomas_df["tipo_desconforto"].astype(str)

    faixa_desconforto = sintomas_df.groupby(["faixa_etaria", "tipo_desconforto"]).size().unstack(fill_value=0)
    st.area_chart(faixa_desconforto)
    with st.expander("📌 Veja nossa análise"):
        st.markdown("""
        <div style="font-size: 16px;">
            Você já parou para pensar se sua idade influencia nos <strong>tipos de desconfortos</strong> que sente ao usar tecnologia?<br><br>
            À medida que analisamos os dados por faixa etária, percebemos que o tipo de desconforto relatado muda consideravelmente.<br>
            Por exemplo, é comum observarmos que <b>faixas etárias mais elevadas</b>, como "Acima de 40 anos", mencionam com mais frequência <b>dores nas costas 
            e cansaço visual</b>, sintomas muitas vezes relacionados à postura e à sobrecarga no uso de tecnologias. Já entre os <b>mais jovens</b>, sintomas 
            como fadiga ocular e dor de cabeça</b> também aparecem com destaque — sinalizando que o uso intenso de telas está afetando todos, 
            independentemente da idade.<br></br>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("Uso contínuo x Sintomas físicos")
    uso_df = df.copy()
    uso_df = uso_df.explode("tipo_desconforto")
    uso_df["tipo_desconforto"] = uso_df["tipo_desconforto"].astype(str)

    uso_desconforto = uso_df.groupby(["uso_continuo", "tipo_desconforto"]).size().unstack(fill_value=0)
    st.area_chart(uso_desconforto)
    with st.expander("📌 Veja nossa análise"):
        st.markdown("""
        <div style="font-size: 16px;">
            Você costuma usar dispositivos por longos períodos sem pausas?<br></br>
            Este gráfico nos ajuda a entender como esse hábito pode afetar sua saúde. Os dados mostram que usuários que <b>mantêm um uso contínuo</b> 
            de tecnologia <b>apresentam maior incidência de sintomas físicos</b> como dores musculares, fadiga ocular e até distúrbios do sono. 
            Em contrapartida, aqueles que fazem pausas regulares relatam menos desconfortos. A mensagem aqui é clara: pausar também é 
            produtividade — e saúde!<br></br>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("Escolaridade x Tempo de uso")
    escolaridade_uso = df.groupby(["escolaridade", "horas_uso"]).size().unstack(fill_value=0)
    st.area_chart(escolaridade_uso)
    with st.expander("📌 Veja nossa análise"):
        st.markdown("""
        <div style="font-size: 16px;">
        A relação entre escolaridade e tempo de uso revela um comportamento interessante. Pessoas com <b>ensino superior</b>, por exemplo, 
        tendem a <b>utilizar mais as tecnologias por longos períodos</b> — o que pode estar diretamente ligado a exigências acadêmicas ou profissionais. 
        Já usuários com escolaridade fundamental ou média utilizam as tecnologias de forma mais distribuída, mas ainda assim, com presença 
        significativa nos maiores tempos de uso.<br></br>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("Renda x Tempo de uso")
    renda_uso = df.groupby(["renda", "horas_uso"]).size().unstack(fill_value=0)
    st.area_chart(renda_uso)
    with st.expander("📌 Veja nossa análise"):
        st.markdown("""
        <div style="font-size: 16px;">
            Será que quem tem maior renda também usa mais tecnologia?<br></br>
            Os dados indicam que sim. Perfis com <b>renda acima de 5 salários</b> tendem a 
            passar <b>mais de 6 horas por dia conectados</b>, o que pode estar associado a atividades profissionais que exigem presença constante 
            em plataformas digitais. Por outro lado, faixas de renda mais baixas também mostram presença considerável, o que sugere que o uso 
            da tecnologia está <b>amplamente distribuído e democratizado</b> — mas o motivo do uso pode variar bastante.<br></br>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("Frequência de atividade física x Sintomas físicos")
    freq_df = df.copy()
    freq_df = freq_df.explode("tipo_desconforto")
    freq_df["tipo_desconforto"] = freq_df["tipo_desconforto"].astype(str)
    freq_desconforto = freq_df.groupby(["frequencia_atividade", "tipo_desconforto"]).size().unstack(fill_value=0)
    st.area_chart(freq_desconforto)
    with st.expander("📌 Veja nossa análise"):
        st.markdown("""
        <div style="font-size: 16px;">
            Aqui temos uma das relações mais valiosas: o quanto praticar atividade física pode ajudar a reduzir os desconfortos causados pelo uso 
            excessivo da tecnologia. <br></br>
            Indivíduos que se <b>exercitam todos os dias</b> relatam significativamente <b>menos sintomas físicos</b>, especialmente 
            dores nas costas e cansaço excessivo. Já quem <b>não pratica atividades físicas</b> demonstra maior incidência de <b>problemas posturais, dores 
            musculares e fadiga</b>. A prática regular de exercícios se mostra, mais uma vez, um excelente aliado para o bem-estar digital.<br></br>
        </div>
        """, unsafe_allow_html=True)

elif app_mode == "Compare os resultados":
    st.title("Compare seu perfil com os dados coletados")

    try:
        df = pd.read_csv("respostas_formulario.csv", encoding="latin1")
    except FileNotFoundError:
        st.warning("Nenhum dado foi enviado ainda. Preencha o formulário primeiro.")
        st.stop()

    st.markdown("""
    <div style="font-size: 16px;">
        Agora, você tem a oportunidade de comparar suas respostas com os dados de outras pessoas que também participaram da pesquisa. Esta seção permite que você 
        visualize como o seu perfil se alinha com os padrões gerais e com as respostas de outros participantes em diferentes faixas etárias. Através de gráficos e 
        insights baseados em dados reais, você poderá observar os sintomas mais comuns relatados por pessoas com o mesmo perfil que o seu.<br></br>
    </div>
    """, unsafe_allow_html=True)

    idade_user = st.selectbox("Sua faixa etária:", sorted(df["faixa_etaria"].unique()))

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        sintomas_geral = df["tipo_desconforto"].str.split("; ").explode().value_counts().sort_values()
        st.bar_chart(sintomas_geral)
        st.caption("Desconfortos mais relatados (geral)")

    with col2:
        sintomas_idade = df[df["faixa_etaria"] == idade_user]["tipo_desconforto"].str.split("; ").explode().value_counts().sort_values()
        st.bar_chart(sintomas_idade)
        st.caption(f"Desconfortos mais relatados entre pessoas com {idade_user}")

    with st.expander("📌 Veja o que descobrimos sobre seu perfil"):
        top_sintoma_geral = sintomas_geral.idxmax() if not sintomas_geral.empty else "Nenhum"
        top_sintoma_idade = sintomas_idade.idxmax() if not sintomas_idade.empty else "Nenhum"
        st.markdown(f"""
        <div style="font-size: 16px;">
            Analisando o seu perfil (faixa etária: <b>{idade_user}</b>), observamos que o desconforto mais comum é <b>{top_sintoma_idade}</b>.<br><br>
            No geral, considerando todos os respondentes, o sintoma mais frequente é <b>{top_sintoma_geral}</b>.<br><br>
        </div>
        """, unsafe_allow_html=True)