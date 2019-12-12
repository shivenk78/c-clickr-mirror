import React, { Component } from 'react';
import '../styles/App.css';

import { FirebaseContext } from '../Firebase';

import Attendance from './Attendance'
import Dates from './Dates';

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      currentDate: undefined
    }
    this.setCurrentDate = this.setCurrentDate.bind(this)
  }

  setCurrentDate(date) {
    this.setState({ currentDate: date })
  }

  render() {
    return (
      <FirebaseContext.Consumer>
        {firebase => {
          return <div className="App" >
            <h1>Attendance</h1>
            <Dates firebase={firebase} setCurrentDate={this.setCurrentDate} />
            <Attendance firebase={firebase} date={this.state.currentDate} />
          </div>
        }}

      </FirebaseContext.Consumer>
    )
  }
}


export default App;
