import { useState } from 'react'
import './App.css'
import Car from './component/Car.jsx'

function App() {
  const [count, setCount] = useState(0)
  const [color, setColor] = useState("");

  const carInfo = {name: "Ford", model: "Mustang"};

  const handleColor = (newColor) => {
    setColor(newColor);
  };

  return (
    <>
      <Car model={carInfo.model}/>
      <h1>Car color in Parent: {color}</h1>
      <Car onColorChange={handleColor} />
    </>
  )
}

export default App
