import React from 'react'
import { Routes, Route, Navigate } from 'react-router-dom'
import Login from './pages/Login'
import Clientes from './pages/Clientes'
import Polizas from './pages/Polizas'
import Siniestros from './pages/Siniestros'
import Pagos from './pages/Pagos'
import Navbar from './components/Navbar'

function App(){
  const token = localStorage.getItem('token')
  return (
    <div>
      <Navbar />
      <div className="max-w-6xl mx-auto p-6">
        <Routes>
          <Route path="/" element={<Navigate to={token?'/clientes':'/login'} />} />
          <Route path="/login" element={<Login/>} />
          <Route path="/clientes" element={<Clientes />} />
          <Route path="/polizas" element={<Polizas />} />
          <Route path="/siniestros" element={<Siniestros />} />
          <Route path="/pagos" element={<Pagos />} />
        </Routes>
      </div>
    </div>
  )
}

export default App
