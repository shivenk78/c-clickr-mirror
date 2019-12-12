import app from 'firebase/app'
import 'firebase/firestore'

const firebaseConfig = {
    apiKey: "AIzaSyDvYZ7icT00ubEYAhptum6-I7f4mlpCfWQ",
    authDomain: "c-clickr-bde73.firebaseapp.com",
    databaseURL: "https://c-clickr-bde73.firebaseio.com",
    projectId: "c-clickr-bde73",
    storageBucket: "c-clickr-bde73.appspot.com",
    messagingSenderId: "854419252517",
    appId: "1:854419252517:web:fce9b12ea2531c2dc766cc",
    measurementId: "G-BX5TWK681G"
}

const usersURL = 'users/'

class Firebase {
    constructor() {
        app.initializeApp(firebaseConfig)

        this.firestore = app.firestore()
    }

    users = (date) => this.firestore.collection('Dates').doc(date)

    dates = () => this.firestore.collection('Dates')

    onDatesListener = (callback) => {
        return this.dates().onSnapshot(querySnap => {
            const entries = []
            querySnap.forEach(doc => {
                entries.push({ id: doc.id, data: doc.data() })
            })
            callback(entries)
        })
    }

    onAttendanceListener = (date, callback) => {
        if (date) {
            return this.users(date).onSnapshot(doc => {
                callback(doc.data())
            })
        }
        else {
            return undefined
        }
    }

}

export default Firebase
