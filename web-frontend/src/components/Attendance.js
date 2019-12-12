import React, { Component } from 'react'
import Table from 'react-bootstrap/Table'
import _ from 'lodash'

const renderAttendance = (students) => {
    return (
        <Table className="table" striped bordered hover>
            <thead>
                <tr>
                    <th>NetId</th>
                    <th>Present?</th>
                </tr>
            </thead>
            <tbody>

                {Object.keys(students).map(id => {
                    const present = students[id] ? 'Yes' : 'No'
                    return id ?
                        <tr key={id}>
                            <td>{id}</td>
                            <td>{present}</td>
                        </tr> : null
                })}

            </tbody>
        </Table>
    )
}

class Attendance extends Component {
    constructor(props) {
        super(props)
        this.state = {
            students: {}
        }
        this.attendanceListener = undefined;

        this.updateTable = this.updateTable.bind(this)
    }

    componentDidUpdate() {
        this.attendanceListener = this.props.firebase.onAttendanceListener(this.props.date, this.updateTable)
    }

    updateTable(students) {
        if (!_.isEqual(this.state.students, students)) {
            console.log(this.state.students)
            console.log(students)
            this.setState(() => ({
                students
            }))
        }

    }

    render() {
        return renderAttendance(this.state.students)
    }
}

export default Attendance;