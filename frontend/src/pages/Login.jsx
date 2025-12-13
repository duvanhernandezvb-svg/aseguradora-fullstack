import React, { useState } from "react";
import api from "../api/axios";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const [username, setUsername] = useState("admin");
  const [password, setPassword] = useState("admin");
  const [msg, setMsg] = useState("");
  const nav = useNavigate();

  async function submit(e) {
    e.preventDefault();
    try {
      const res = await api.post("/login", { username, password });
      localStorage.setItem("token", res.data.access_token);
      nav("/clientes");
    } catch (err) {
      const errorMsg =
        typeof err?.response?.data === "object"
          ? JSON.stringify(err?.response?.data)
          : err?.response?.data?.detail;
      setMsg(errorMsg || "Error al conectar");
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="bg-white p-8 rounded-2xl shadow-xl w-full max-w-sm">
        <h2 className="text-2xl font-bold text-center text-indigo-700 mb-6">Iniciar Sesión</h2>
        <form onSubmit={submit} className="space-y-4">
          <input
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            placeholder="Usuario"
            className="w-full p-3 border rounded-lg focus:ring-indigo-500"
          />
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Contraseña"
            className="w-full p-3 border rounded-lg focus:ring-indigo-500"
          />
          <button className="w-full bg-indigo-600 text-white p-3 rounded-lg hover:bg-indigo-700 transition">
            Entrar
          </button>
        </form>
        {msg && <p className="text-red-500 text-sm mt-3 text-center">{msg}</p>}
      </div>
    </div>
  );
}

