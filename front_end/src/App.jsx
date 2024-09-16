import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Login from './pages/Login.jsx';
import SignUp from './pages/SignUp.jsx';
import Home from './pages/Home.jsx';
import 'react-loading-skeleton/dist/skeleton.css';

function App () {

  return (
    <>
        <Router>
           <Routes>
			  <Route path={'/'} element={<Home />}></Route>
              <Route path={'/login'} element={<Login />}></Route>
              <Route path={'/signup'} element={<SignUp />}></Route>
           </Routes>
        </Router>
    </>
  )
}

export default App
