import { useState } from 'react';

function Car(props) {

  const changeColor = ({ onColorChange }) => {
    console.log('blue');
    onColorChange('blue');
  };

  return(
    <>
      <h1>This car is {props.model}</h1>
      <button onClick={changeColor}>Change Car color</button>
    </>
  )
}

export default Car;
