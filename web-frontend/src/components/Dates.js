import React, { Component } from 'react'
import Dropdown from 'react-bootstrap/Dropdown'
import DropdownButton from 'react-bootstrap/DropdownButton'

class Dates extends Component {
    constructor(props) {
        super(props)
        this.state = {
            dates: []
        }
        this.dateListener = undefined;

        this.updateDates = this.updateDates.bind(this)
    }

    updateDates(data) {
        const dates = []
        data.forEach(date => {
            dates.push(date.id)
        })
        this.setState({ dates })
    }

    componentDidMount() {
        this.dateListener = this.props.firebase.onDatesListener(this.updateDates)
    }

    render() {
        return (
            <DropdownButton
                title='dates'
                variant='primary'
                id={'dropdown-variants-primary'}
                key='primary'
            >
                {this.state.dates.map(date => (
                    <Dropdown.Item key={date} onClick={() => this.props.setCurrentDate(date)}>{date}</Dropdown.Item>
                ))}
            </DropdownButton>
        )
    }
}

export default Dates;