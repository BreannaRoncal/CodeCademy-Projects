import React from 'react';
import { fetchUserData, cancelFetch } from './dataFetcher';
import { Userlist } from './Userlist';

export class Profile extends React.Component {
  constructor(props){
    super(props);
    this.state = { userData: null };
    this.loadUserData = this.loadUserData.bind(this);
  }
  loadUserData(){
    this.setState({ userData: null });
    this.fetchID = fetchUserData(this.props.username,
    (userData) => {
      this.setState({ userData });
    });
  }
  render() {
    const isLoading = this.state.userData === null ? true : false;

    let className = 'Profile';
    if (isLoading) {
      className += ' loading';
    }

    let name = isLoading === true ? 'Loading...' : this.state.userData.name;
    let bio = isLoading === true ? 'Loading Bio...' : this.state.userData.bio;
    let friends = isLoading === true ? [] : this.state.userData.friends;

    return (
      <div className={className}>
        <div className="profile-picture">
          {!isLoading && (
            <img src={this.state.userData.profilePictureUrl} alt="profile picture" />
          )}
        </div>
        <div className="profile-body">
          <h2>{name}</h2>
          <h3>@{this.props.username}</h3>
          <p>{bio}</p>
          <h3>{friends}</h3>
          <Userlist usernames={friends} onChoose={this.props.onChoose} />
        </div>
      </div>
    );
  }
  componentDidMount(){
    this.loadUserData();
  }
  componentDidUpdate(prevProps){
    if (this.props.username !== prevProps.username){
      cancelFetch(this.fetchID);
      this.loadUserData();
    }
  }
  componentWillUnmount(){
    cancelFetch(this.fetchID);
  }
}
