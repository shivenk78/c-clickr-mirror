const firebase = require("firebase");
// Required for side-effects
require("firebase/firestore");

var firebaseConfig = {
    apiKey: "AIzaSyDvYZ7icT00ubEYAhptum6-I7f4mlpCfWQ",
    authDomain: "c-clickr-bde73.firebaseapp.com",
    databaseURL: "https://c-clickr-bde73.firebaseio.com",
    projectId: "c-clickr-bde73",
    storageBucket: "c-clickr-bde73.appspot.com",
    messagingSenderId: "854419252517",
    appId: "1:854419252517:web:fce9b12ea2531c2dc766cc",
    measurementId: "G-BX5TWK681G"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);
var db = firebase.firestore();
