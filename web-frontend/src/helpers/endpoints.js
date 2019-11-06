import axios from 'axios'

const apikey = ''

let restdb = axios.create({
    baseURL: '',
    timeout: 1000,
    headers: { 'x-apikey': apikey }
})

const realtimeURL = ''

export { apikey, restdb, realtimeURL } 