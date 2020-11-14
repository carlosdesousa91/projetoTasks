import React, {useState} from 'react';
import './App.css';
import Login from './components/login';
import Tasks from './components/tasks';

function App() {

  const [token, setToken] = useState('');

  const userLogin = (tok) => {
    setToken(tok);
    //console.log(tok);
    //console.log(token);

  }
  return (
    <div className="App">
      < Login userLogin={userLogin}/>
      <Tasks token={token}/>
    </div>
  );
}

export default App;
