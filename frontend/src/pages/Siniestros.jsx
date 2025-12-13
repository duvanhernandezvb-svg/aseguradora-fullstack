import { useState, useEffect } from "react";
import api from "../api/axios";

export default function Siniestros() {
  const [siniestros, setSiniestros] = useState([]);
  const [form, setForm] = useState({
    cliente_id: "",
    poliza_id: "",
    fecha: "",
    descripcion: "",
    estado: "En revisión",
  });

  const loadData = async () => {
    try {
      const res = await api.get("/siniestros");
      setSiniestros(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    loadData();
  }, []);

  const create = async (e) => {
    e.preventDefault();
    try {
      await api.post("/siniestros", form);
      loadData();
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="space-y-8">
      <div className="bg-white p-6 rounded-2xl shadow-xl border border-gray-200">
        <h2 className="text-2xl font-bold text-indigo-600 mb-4">
          Reportar Siniestro
        </h2>
        <form className="grid grid-cols-1 md:grid-cols-2 gap-4" onSubmit={create}>
          {Object.entries(form).map(([field, value]) => (
            <input
              key={field}
              type={field === "fecha" ? "date" : "text"}
              placeholder={field.replace(/_/g, " ").toUpperCase()}
              value={value}
              onChange={(e) => setForm({ ...form, [field]: e.target.value })}
              className="p-3 border rounded-lg focus:ring-indigo-500"
            />
          ))}
          <button className="col-span-full bg-indigo-600 text-white p-3 rounded-lg hover:bg-indigo-700 transition">
            Crear Siniestro
          </button>
        </form>
      </div>

      <div className="grid gap-6 md:grid-cols-3">
        {siniestros.map((s) => (
          <div className="bg-white shadow-md rounded-xl p-4 border border-gray-200">
            <p className="font-semibold text-indigo-600">Cliente: {s.cliente_id}</p>
            <p className="text-gray-600">Póliza: {s.poliza_id}</p>
            <p className="text-gray-600">Estado: {s.estado}</p>
            <p className="text-gray-500">{s.descripcion}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
