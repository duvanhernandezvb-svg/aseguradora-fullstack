import React from "react";
import { Link, useNavigate } from "react-router-dom";

export default function Navbar() {
  const nav = useNavigate();
  const token = localStorage.getItem("token");
  function logout() {
    localStorage.removeItem("token");
    nav("/login");
  }

  return (
    <header className="bg-indigo-600 text-white shadow-lg">
      <div className="max-w-6xl mx-auto flex justify-between items-center p-4">
        <div className="flex items-center gap-3">
          <img src="/logo192.png" alt="logo" className="w-10 h-10" />
          <h1 className="text-2xl font-bold">Aseguradora</h1>
        </div>
        <nav className="flex gap-3 text-sm md:text-base">
          <Link to="/clientes" className="hover:bg-indigo-700 px-3 py-2 rounded-lg transition">
            Clientes
          </Link>
          <Link to="/polizas" className="hover:bg-indigo-700 px-3 py-2 rounded-lg transition">
            Pólizas
          </Link>
          <Link to="/siniestros" className="hover:bg-indigo-700 px-3 py-2 rounded-lg transition">
            Siniestros
          </Link>
          <Link to="/pagos" className="hover:bg-indigo-700 px-3 py-2 rounded-lg transition">
            Pagos
          </Link>
          {token ? (
            <button onClick={logout} className="bg-red-500 hover:bg-red-600 px-3 py-2 rounded-lg">
              Salir
            </button>
          ) : (
            <Link to="/login" className="hover:bg-indigo-700 px-3 py-2 rounded-lg">
              Login
            </Link>
          )}
        </nav>
      </div>
    </header>
  );
}

