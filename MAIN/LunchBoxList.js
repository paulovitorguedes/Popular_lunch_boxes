import React, { useState, useEffect } from 'react';
import { FlatList, View, Text, TouchableOpacity, Button } from 'react-native';
import axios from 'axios';
import { useNavigation } from '@react-navigation/native';

// Componente principal que renderiza a lista de lunch boxes
const LunchBoxList = () => {
  // Estado para armazenar a lista de lunch boxes
  const [lunchBoxes, setLunchBoxes] = useState([]);
  
  // Estado para armazenar erros que possam ocorrer
  const [error, setError] = useState(null);
  
  // Estado para armazenar a ordem de sorteamento
  const [sortOrder, setSortOrder] = useState('asc');
  
  // Hook para obter a navegação
  const navigation = useNavigation();

  // Função para buscar a lista de lunch boxes da API
  const fetchLunchBoxes = async () => {
    try {
      // Faz uma requisição GET para a API para buscar a lista de lunch boxes
      const response = await axios.get('https://api.example.com/lunch-boxes');
      
      // Atualiza o estado com a lista de lunch boxes
      setLunchBoxes(response.data);
    } catch (error) {
      // Atualiza o estado com o erro que ocorreu
      setError(error.message);
    }
  };

  // Efeito para buscar a lista de lunch boxes quando o componente é montado
  useEffect(() => {
    fetchLunchBoxes();
  }, []);

  // Função para lidar com a navegação quando o usuário clica em um item da lista
  const handlePress = (item) => {
    // Navega para a tela de detalhes do lunch box selecionado
    navigation.navigate('LunchBoxDetails', { item });
  };

  // Função para lidar com a ordenação da lista de lunch boxes
  const handleSort = () => {
    if (sortOrder === 'asc') {
      // Ordena a lista de lunch boxes em ordem crescente de preço
      setLunchBoxes(lunchBoxes.sort((a, b) => a.price - b.price));
      
      // Atualiza o estado com a ordem de sorteamento
      setSortOrder('desc');
    } else {
      // Ordena a lista de lunch boxes em ordem decrescente de preço
      setLunchBoxes(lunchBoxes.sort((a, b) => b.price - a.price));
      
      // Atualiza o estado com a ordem de sorteamento
      setSortOrder('asc');
    }
  };

  // Se houver um erro, renderiza uma mensagem de erro
  if (error) {
    return (
      <View>
        <Text>Erro: {error}</Text>
      </View>
    );
  }

  // Renderiza a lista de lunch boxes com a ordenação e navegação
  return (
    <View>
      <FlatList
        data={lunchBoxes}
        renderItem={({ item }) => (
          <TouchableOpacity onPress={() => handlePress(item)}>
            <View>
              <Text>{item.name}</Text>
              <Text>R$ {item.price}</Text>
            </View>
          </TouchableOpacity>
        )}
      />
      <Button title="Ordenar por preço" onPress={handleSort} />
    </View>
  );
};

export default LunchBoxList;