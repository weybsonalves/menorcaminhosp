import streamlit as st
from graph_utils import make_graph, dijkstra

st.set_page_config(page_title='menorcaminhosp')

def main():
    g = make_graph('municipios_sp.txt', 'distancias_municipios_sp.txt')
    st.title('Menor caminho entre municípios de São Paulo')
    st.header('Definição do problema')
    st.write('''João mora em Pindamonhangaba e gostaria de viajar com seu fusca e conhecer vários municípios
     do estado de São Paulo, entretanto, como João não possui experiência com viagens e nem muito dinheiro, 
     ele quer garantir que está se deslocando de uma cidade a outra pelo menor caminho. Além disso, ele 
     gostaria de, ao decorrer da sua jornada, passar apenas por municípios do estado de São Paulo.''')
    st.write('''Desse modo, para auxiliá-lo nessa jornada, João criou um programa que retorna o menor 
    caminho entre duas cidades e a distância desse caminho.''')
    st.image('map.png')
    st.header('Selecine a origem e o destino:')
    city1 = st.selectbox('Cidade 1', list(g.adjacency_list.keys()))
    city2 = st.selectbox('Cidade 2', list(g.adjacency_list.keys()))
    if st.button('Encontrar menor caminho'):
        distance, path = dijkstra(g, city1, city2)
        st.subheader(f'O menor caminho entre {city1} e {city2} é:')
        st.success(" -> ".join(path))
        st.subheader(f'A distância desse caminho é de:')
        st.success(f'{distance:.1f} Km')
    st.sidebar.info('''This database is made available under the [Open Database License](http://opendatacommons.org/licenses/odbl/1.0/). 
    Any rights in individual contents of the database are licensed under the [MIT License](https://mit-license.org). 
    © contribuidores do OpenStreetMap. Weybson Alves da Silva.''')


if __name__ == '__main__':
    main()
