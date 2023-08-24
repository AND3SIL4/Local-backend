import { initializeApp } from 'firebase/app'
import {
  getFirestore, collection, onSnapshot,
  addDoc, deleteDoc, doc,
  query, where,
  orderBy, serverTimestamp, 
  getDoc, updateDoc
} from 'firebase/firestore'

import {
  getAuth,
  createUserWithEmailAndPassword,
  signOut, signInWithEmailAndPassword,
  onAuthStateChanged
} from 'firebase/auth'

const firebaseConfig = {
  apiKey: "AIzaSyBXQR7tIRSD71uhPPjFzHy8Mc8zE3B4Lzk",
  authDomain: "fir-9-dojo-6f8c9.firebaseapp.com",
  projectId: "fir-9-dojo-6f8c9",
  storageBucket: "fir-9-dojo-6f8c9.appspot.com",
  messagingSenderId: "14790925081",
  appId: "1:14790925081:web:f4e2ab403341626db60388"
};
// init firebase app
initializeApp(firebaseConfig)

// init services 
const db = getFirestore()
const auth = getAuth()

// collection ref 
const colRef = collection(db, 'books')

// query 

const q = query(colRef, orderBy('createdAt'))

// real time collection data 
const unsubCol = onSnapshot(q, (snapshot) => {
  let books = []
  snapshot.docs.forEach((doc) => {
    books.push({ ...doc.data(), id: doc.id })
  })
  console.log(books);
})

// adding documents

const addBookForm = document.querySelector('.add')

addBookForm.addEventListener('submit', (e) => {
  e.preventDefault()

  addDoc(colRef, {
    title: addBookForm.title.value,
    author: addBookForm.author.value,
    createdAt: serverTimestamp()
  })
    .then(() => {
      addBookForm.reset()
    })
})

// deleting documents

const deleteBookForm = document.querySelector('.delete')

deleteBookForm.addEventListener('submit', (e) => {
  e.preventDefault()

  const docRef = doc(db, 'books', deleteBookForm.id.value)

  deleteDoc(docRef)
    .then(() => {
      deleteBookForm.reset()
    })
})

// get a single document 

const docRef = doc(db, 'books', 'KGPjH5YjWObYwHMHnvk4')

getDoc(docRef)
  .then((doc) => {
    console.log(doc.data(), doc.id);
  })

const unsubDoc = onSnapshot(docRef, (doc) => {
  console.log(doc.data(), doc.id)
})

const updateForm = document.querySelector('.update')

updateForm.addEventListener('submit', (e) => {
  e.preventDefault()

  const docRef = doc(db, 'books', updateForm.id.value)

  updateDoc(docRef,  {
    title: 'updated title'
  })
  .then(() => {
    updateForm.reset()
  })
})

// signing user up

const signupForm = document.querySelector('.signup')
signupForm.addEventListener('submit', (e) => {
  e.preventDefault()

  const email = signupForm.email.value
  const password = signupForm.password.value
  
  createUserWithEmailAndPassword(auth, email, password)
    .then((cred) => {
      // console.log('user created:', cred.user);
      signupForm.reset()
    })
    .catch((err) => {
      console.log(err.message);
    })

})

// Login and logout 

const logoutButton = document.querySelector('.logout')
logoutButton.addEventListener('click', () => {
  signOut(auth)
    .then(() => {
      // console.log('user singned out');
    })
    .catch((err) => {
      console.log(err.message);
    })
})

const loginForm = document.querySelector('.login')
loginForm.addEventListener('submit', (e) => {
  e.preventDefault()

  const email = loginForm.email.value
  const password = loginForm.password.value

  signInWithEmailAndPassword(auth, email, password)
    .then((cred) => {
      // console.log('user logged in: ', cred.user);

    })
    .catch((err) => {
      console.log(err.message);
    })
})

// subscribing to auth changes

const unsubAuth = onAuthStateChanged(auth, (user) => {
  console.log('user status change: ', user );
})

// unsusbcribing from changes (auth & db)
const unsubButton = document.querySelector('.unsub')
unsubButton.addEventListener('click', () => {
  console.log('unsubscribing');
  unsubCol()
  unsubDoc()
  unsubAuth()
})