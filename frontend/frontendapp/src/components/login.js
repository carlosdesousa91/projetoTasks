import React, {Component} from 'react';

class Login extends Component {

    state = {
        credentials: {username: '', password: ''}
    }

    login = event => {
        console.log(this.state.credentials);
    }
    inputChanged = event => {
        const cred = this.state.credentials;
        cred[event.target.name] = event.target.value;
        this.setState({credentials: cred});
    }

    render() {

        return (
            <div >
            <h1>Login user form</h1>
            <labe>
                username:
                <input type="text" name="username" 
                value={this.state.credentials.username}
                onChange={this.inputChanged}
                />
            </labe>
            <br/>
            <labe>
                senha:
                <input type="password" name="password" 
                value={this.state.credentials.password}
                onChange={this.inputChanged}
                />
            </labe>
            <br/>
            <button onClick={this.login}>Login</button>
            </div>
        );

  }
  
}

export default Login;
