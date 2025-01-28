import UserFavoriteAnimals from "./UserFavoriteAnimals";
import Exercise from './Exercise3.js'


// Exercise 1: With JSX
const myelement = <h1>I LoVE JSX!</h1>;
const sum = 5+5;

// Exercise 2 : Object
const user = {
  firstName: 'Bob',
  lastName: 'Dylan',
  favAnimals : ['Horse','Turtle','Elephant','Monkey']
};



function App() {
  return (
   <>
      <h1>Hello World!</h1>
      {myelement}
      <h3>React is {sum} times better with JSX</h3>


      <h3>{user.firstName}</h3>
      <h3>{user.lastName}</h3>
      <h4>This is Awosme</h4>
      <UserFavoriteAnimals/>
      <Exercise/>

   </>
  );
}

export default App;
