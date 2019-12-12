import React, { Component } from 'react'
import Table from 'react-bootstrap/Table'

class UpdatingTable extends Component {
    constructor(props) {
        super(props)

        this.state = {
            data: {}
        }

        this.dataListener = undefined

        this.updateTable = this.updateTable.bind(this)
    }

    updateTable(data) {
        this.setState(prev => ({
            data
        }))
    }

    renderTable(data) { }

    componentDidMount() {
        this.dataListener = this.initListener()
    }

    initListener() { }

    componentWillUnmount() {
        this.dataListener()
    }

    render() {
        return (
            <Table className="table" striped bordered hover>
                {this.renderTable()}
            </Table>
        )
    }
}

export default UpdatingTable;