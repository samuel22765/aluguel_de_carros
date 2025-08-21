import streamlit as st


#---------------------------------------------- sidebar
st.sidebar.title("Kayak")
st.sidebar.image("logo.png")
st.sidebar.title("Aluguel De Carros ")
carros  = ['Civic','BMW', 'Porshe','Mercedes']

opcao = st.sidebar.selectbox('Escolha seu carro para alugar', carros )









#----------------------------------------------- principal 
st.title("Kayak")
st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')

dias = st.text_input(f'por quantos dias o {opcao} foi alugado')
km = st.text_input(f'Quantos km voce rodou com o {opcao}?')

if opcao == 'BMW':
    diaria = 900

elif opcao == 'Mercedes':
    diaria = 800 

elif opcao == 'Porshe':
    diaria = 1000 

elif opcao == 'Civic':
    diaria = 750


if  st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria 
    total_km = km * 0.15
    aluguel_total = total_dias+total_km

    st.warning(f'Você alugou o {opcao} por {dias} dias e rodou {km}km. O valor total a pagar é R${aluguel_total}')






