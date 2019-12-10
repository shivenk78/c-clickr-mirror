import React from 'react';
import '../styles/App.css';

import Attendance from './Attendance'
import { FirebaseContext } from '../Firebase';

const App = () => (
  <FirebaseContext.Consumer>
    {firebase => {
      return <div className="App" >
        <h1>Attendance</h1>
        <Attendance firebase={firebase} />
      </div>
    }}

  </FirebaseContext.Consumer>
)


export default App;
