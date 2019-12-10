import React, { Component } from 'react'
import Table from 'react-bootstrap/Table'

class Attendance extends Component {
    constructor(props) {
        super(props)

        this.state = {
            students: {}
        }

        this.dataListener = undefined

        this.updateStudents = this.updateStudents.bind(this)
    }

    updateStudents(students) {
        this.setState(prev => ({
            students
        }))
    }

    componentDidMount() {
        this.dataListener = this.props.firebase.onUsersListener(this.updateStudents)
    }


    componentWillUnmount() {
        this.props.firebase.users().off('value', this.dataListener)
    }

    render() {
        const { students } = this.state
        return (
            <Table className="table" striped bordered hover>
                <thead>
                    <tr>
                        <th>Student</th>
                        <th>NetId</th>
                    </tr>
                </thead>
                <tbody>

                    {Object.keys(students).map(netId =>
                        <tr key={netId}>
                            <td>{students[netId]}</td>
                            <td>{netId}</td>
                        </tr>
                    )}

                </tbody>
            </Table>
        )
    }
}

export default Attendance;