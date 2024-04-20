import React, { useState } from 'react';
import { Button, View, Text, StyleSheet, TextInput, Image, FlatList } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

function HomeScreen({ navigation }) {
  const [query, inputQuery] = useState('')

  return (
    <View style={styles.container}>
      <Text> Search-Engine</Text>
      <Image
        source={{
          uri: 'https://www.billboard.com/wp-content/uploads/2021/07/IDK-cr-Jack-McKain-press-2021-billboard-1548-1626710172.jpg'}}
          style={{width: 400, height: 400}} />
      <TextInput
        style={styles.input}
        placeholder='Input query here'
        onChangeText={(text) => inputQuery(text)}
        value={query}
      />
      <Button
        title="Search"
        onPress={() => navigation.navigate('Query', { query: query })} // Pass query state as parameter
        style={styles.button}
      />
    </View>
  );
}

function QueryScreen({ route }) {
  const { query } = route.params;

  const aaa = [
    [1, 3],
    [1,2]
  ];

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Text> Searched: {query}</Text>
      <FlatList
        data={aaa}
        renderItem={({ item }) => (
          <View style={styles.item}>
            <Text>{item[0]}: {item[1]}</Text>
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
  },
  input: {
    width: '100%', // Set input width to 100%
    backgroundColor: 'gray',
    margin: 10,
    padding:5,
  },
  button: {
    margin: 10,
    flex: 1, // Make button expand to fill available space horizontally
  }
});


export default App;
