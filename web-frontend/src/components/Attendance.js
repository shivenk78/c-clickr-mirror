import React, { Component } from 'react'

import { restdb, realtimeURL } from '../helpers/endpoints'

class Attendance extends Component {
    constructor(props) {
        super(props)

        this.state = {
            ping: new Date(),
            event: '',
            students: []
        }

        this.eventSource = new EventSource(realtimeURL)
        this.addPingWatch = this.addPingWatch.bind(this)
    }

    addPingWatch() {
        this.eventSource.addEventListener('ping', e => {
            this.setState(prev => {
                ping: new Date(e.data)
            })
        })
    }

    componentDidMount() {
        this.interval = setInterval(() => {
            let now = new Date().getTime()
            let diff = (now - this.state.ping.getTime()) / 1000

            if (diff > 20) {
                window.location.reload();
            }
        }, 10000)

        this.addPingWatch()
    }


    componentWillUnmount() {
        clearInterval(this.interval)
    }

    render() {
        return (
            <div className="students">
                <table className="table">
                    <thead>
                        <tr>
                            <th>Student</th>
                            <th>NetId</th>
                        </tr>
                    </thead>
                    <tbody>

                        {this.state.students.map(student =>

                            <tr key={student.id}>
                                <td>{student.netId}</td>
                                <td>{student.name}</td>
                            </tr>
                        )}

                    </tbody>
                </table>
            </div>
        )
    }
}

export default Attendance;