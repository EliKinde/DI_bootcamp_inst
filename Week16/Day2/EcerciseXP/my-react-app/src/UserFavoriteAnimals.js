import userEvent from '@testing-library/user-event';
import { Component } from 'react';

class UserFavoriteAnimals extends Component {
    render() {
        return (
          <>
              <h3>The Favortei Animel is: {this.props.favAnimals}</h3>
          </>
        )
    }
}


export default UserFavoriteAnimals;