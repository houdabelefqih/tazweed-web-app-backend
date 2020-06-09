import React from 'react';
import ApolloClient from 'apollo-boost';
import { UserInfo } from './User'
import { ApolloProvider } from '@apollo/react-hooks';

const client = new ApolloClient({
  uri: 'http://localhost:8080/graphql/', // your GraphQL Server 
});
const App = () => (
  <ApolloProvider client={client}>
    <div style={{
      backgroundColor: '#00000008',
      display: 'flex',
      justifyContent:'center',
      alignItems:'center',
      height: '100vh',
      flexDirection: 'column',
    }}>
      <h2>My first Apollo app 🚀</h2>
    </div>

    <UserInfo/>
  </ApolloProvider>
);
export default App;