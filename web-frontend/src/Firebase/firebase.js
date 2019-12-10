import app from 'firebase/app'
import 'firebase/database'

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

        this.db = app.database()
    }

    user = netId => this.db.ref(usersURL + netId)
    users = () => this.db.ref(usersURL)

    onUsersListener = (callback) => {
        return this.users().on('value', (snapshot) => {
            callback(snapshot.val())
        })
    }

    getUsers = (callback) => {
        return this.users().once('value').then((snapshot) => {
            callback(snapshot.val())
        });

    }
}

export default Firebase
