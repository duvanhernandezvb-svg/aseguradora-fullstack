import React, { useEffect, useState } from "react";
import api from "../api/axios";
import CardForm from "../components/CardForm";

export default function Clientes() {
  const [list, setList] = useState([]);
  const [form, setForm] = useState({
    documento: "",
    nombre: "",
    apellido: "",
    telefono: "",
    email: "",
    direccion: "",
  });
  const [msg, setMsg] = useState("");

  async function fetchList() {
    try {
      const res = await api.get("/clientes");
      setList(res.data);
    } catch (err) {
      setMsg("Error al obtener clientes");
    }
  }

  useEffect(() => {
    fetchList();
  }, []);

  async function submit(e) {
    e.preventDefault();
    try {
      await api.post("/clientes", form);
      setMsg("Cliente creado ✓");
      setForm({
        documento: "",
        nombre: "",
        apellido: "",
        telefono: "",
        email: "",
        direccion: "",
      });
      fetchList();
    } catch (err) {
      setMsg(err?.response?.data?.detail || "Error");
    }
  }

  return (
    <div className="space-y-8">
      <CardForm title="Crear Cliente">
        <form className="space-y-3" onSubmit={submit}>
          {[
            ["Documento", "documento"],
            ["Nombre", "nombre"],
            ["Apellido", "apellido"],
            ["Teléfono", "telefono"],
            ["Email", "email"],
            ["Dirección", "direccion"],
          ].map(([label, key]) => (
            <input
              key={key}
              placeholder={label}
              required={["documento", "nombre", "apellido"].includes(key)}
              value={form[key]}
              onChange={(e) => setForm({ ...form, [key]: e.target.value })}
              className="w-full p-3 border rounded-lg focus:ring-indigo-500"
            />
          ))}
          <button className="w-full bg-indigo-600 text-white p-3 rounded-lg hover:bg-indigo-700">
            Crear Cliente
          </button>
        </form>
        {msg && <p className="mt-2 text-sm text-indigo-600">{msg}</p>}
      </CardForm>

      <div className="grid gap-4">
        {list.map((c) => (
          <div
            key={c.id}
            className="bg-white shadow rounded-xl p-4 border border-gray-200"
          >
            <p className="font-semibold text-indigo-600">
              {c.documento} — {c.nombre} {c.apellido}
            </p>
            <p className="text-sm text-gray-600">{c.email}</p>
            <p className="text-sm text-gray-600">{c.telefono}</p>
            <p className="text-sm text-gray-600">{c.direccion}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
