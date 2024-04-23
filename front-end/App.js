import React, { useState, useEffect } from 'react';
import { Button, View, Text, StyleSheet, TextInput, Image, FlatList } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

function HomeScreen({ navigation }) {
  const searchTypes = ['cosine', 'SVD1000']
  const results_nums = [10, 20, 30]
  const [query, inputQuery] = useState('')
  const [searchID, setSearchType] = useState(0)
  const [results_numID, setResults_num] = useState(0)

  return (
    <View style={styles.container}>
      <Text style={styles.title}> Search-Engine</Text>
      <Image
        source={{
          uri: 'https://www.billboard.com/wp-content/uploads/2021/07/IDK-cr-Jack-McKain-press-2021-billboard-1548-1626710172.jpg'}}
          style={{width: 300, height: 300}} />
      <TextInput
        style={styles.input}
        placeholder='Input query here'
        onChangeText={(text) => inputQuery(text)}
        value={query}
      />
      <View style={styles.options}>
        <Button
          title={searchTypes[searchID]}
          onPress={() => setSearchType((searchID + 1) % searchTypes.length)}
          style={{ margin: 10 }}
        />
        <Button
          title={results_nums[results_numID].toString()}
          onPress={() => setResults_num((results_numID + 1) % results_nums.length)}
          style={{ margin: 10 }}
        />
      </View>
      <Button
        title="Search"
        onPress={() => navigation.navigate('Query', { query: query, searchType: searchTypes[searchID], results_num: results_nums[results_numID]})}
      />
    </View>
  );
}

function QueryScreen({ route }) {
  const { query } = route.params;
  const { searchType } = route.params;
  const { results_num } = route.params;
  const [data, setData] = useState([])

  useEffect(() => {
    getResults();
  }, []);

  const getResults = async () => {
    fetch(`http://localhost:5000/${searchType}?query=${query}&results_num=${results_num}`, {
      method: 'GET',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
      }
    }).then(response => {console.log(response);response.json()})
    .then(json => Promise.resolve(json['result']))
    .then(result => setData(result))
    console.log(data)
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}> Searched: {query}</Text>
      <FlatList
        data={data}
        renderItem={({ item }) => (
          <View style={styles.item}>
            <Text>{item[0]} - {item[1]}</Text>
          </View>
        )}
      />
    </View>
  );
}

const Stack = createNativeStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Search Engine">
        <Stack.Screen name="Search Engine" component={HomeScreen} />
        <Stack.Screen name="Query" component={QueryScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#8B8786',
  },
  title: {
    fontSize: 30,
    fontWeight: 'bold',
    textAlign: 'center',
  },
  input: {
    width: '100%',
    backgroundColor: 'darkgray',
    margin: 10,
    padding:5,
  },
  button: {
    margin: 10,
    flex: 1,
  },
  options: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    margin: 10,
  },
});


export default App;
