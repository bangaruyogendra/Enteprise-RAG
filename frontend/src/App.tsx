import { useState } from 'react'
import {useEffect} from 'react'
import axios from 'axios'


function App() {
  
  const [message,setMessage] = useState('') 
  useEffect(()=>{
     axios.get('http://localhost:8000/health').then((response)=>{
      setMessage(response.data.status)
      }).catch((error)=>{
        console.error('Error fetching message:', error);
      })
  },[])
  return (
    <>
     <div className="App">
      <h1>{message}</h1>
     </div>
    </>
  )
}

export default App
