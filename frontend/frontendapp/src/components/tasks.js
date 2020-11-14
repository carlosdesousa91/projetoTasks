import React, {Component} from 'react';

class Tasks extends Component {

    state = {
        tasks: []
    }

    loadBooks = () => {

        fetch('http://localhost:8000/api/tasks/', {
            method:'GET',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(this.state.credentials)
        })
        .then(data => data.json())
        .then(
            data => {
                this.setState({tasks: data})
            }
        ).catch(error => console.error(error))
    }

    render() {

        return (
            <div >
                <h1>Tasks</h1>
                { this.state.tasks.map(task => {
                    return <h3 key={task.id}>{task.title}</h3>
                 }) }
                <button onClick={this.loadBooks}>Load Tasks</button>
            </div>
        );

  }
  
}

export default Tasks;
