import React, { Component } from 'react'
import Table from 'react-bootstrap/Table'

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
            this.setState(prev => ({
                ping: new Date(e.data),
                students: this.props.students
            }))
        })
    }

    componentDidMount() {
        this.interval = setInterval(() => {
            let now = new Date().getTime()
            let diff = (now - this.state.ping.getTime()) / 1000

            if (diff > 20) {
                //window.location.reload();
            }
        }, 1000)

        this.addPingWatch()
    }


    componentWillUnmount() {
        clearInterval(this.interval)
    }

    render() {
        console.log('attendance render')
        return (
            <Table className="table" striped bordered hover>
                <thead>
                    <tr>
                        <th>Student</th>
                        <th>NetId</th>
                    </tr>
                </thead>
                <tbody>

                    {this.props.students.map(student =>

                        <tr key={student.netId}>
                            <td>{student.name}</td>
                            <td>{student.netId}</td>
                        </tr>
                    )}

                </tbody>
            </Table>
        )
    }
}

export default Attendance;