import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import './App.css'
import Login from "./pages/Login.jsx";

function App() {

  return (
    <>
        <Router>
           <Routes>
              <Route path={'/login'} element={<Login />}></Route>
           </Routes>
        </Router>
    </>
  )
}

export default App
