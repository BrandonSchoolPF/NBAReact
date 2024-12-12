import React from 'react';
import Header from './components/header/AppHeader.jsx';
import Title from './components/title/Title.jsx'

function App() {
  return (
    <>
      <Title text="MagicBot 2.0" style={{ color: 'grey' }} />
      <Header />
    </>
  );
}

export default App;
