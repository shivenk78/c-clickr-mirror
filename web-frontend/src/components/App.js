import React, { Component } from 'react';
import '../styles/App.css';

import Attendance from './Attendance'

import { useState } from 'react';

let students = []

const useSignUpForm = () => {
  const [inputs, setInputs] = useState({ name: '', netId: '' });
  const handleSubmit = (event) => {
    if (event) {
      event.preventDefault()
    }
    students.push({ name: inputs.name, netId: inputs.netId })
    setInputs(inputs => ({ name: '', netId: '' }))
  }
  const handleInputChange = (event) => {
    event.persist()
    setInputs(inputs => ({ ...inputs, [event.target.name]: event.target.value }))
  }
  return {
    handleSubmit,
    handleInputChange,
    inputs
  }
}

function App() {
  const { inputs, handleInputChange, handleSubmit } = useSignUpForm()
  return (
    <div className="App" >
      <form onSubmit={handleSubmit}>
        <input type="text" name="name" onChange={handleInputChange} value={inputs.name} />
        <input type="text" name="netId" onChange={handleInputChange} value={inputs.netId} />
        <button type="submit">Add Student</button>
      </form>
      <Attendance students={students} />
    </div>
  )
}

export default App;
