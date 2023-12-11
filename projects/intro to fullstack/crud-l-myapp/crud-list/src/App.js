import React from 'react';
import './App.css';
import RestaurantTable from './Restaurant.js';
import { useState } from 'react';


function App() {
  // const url = "localhost:4000";
  // const [data, setData] = useState([]);
  // rows={data} setRows={setData}

  return (
    <div className="App">
      <RestaurantTable/> 
    </div>
  );
}

export default App;

