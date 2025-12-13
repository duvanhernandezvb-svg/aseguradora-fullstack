import { useState, useEffect } from "react";
import api from "../api/axios";

export default function Polizas() {
  const [polizas, setPolizas] = useState([]);
  const [form, setForm] = useState({
    cliente_id: "",
    numero_poliza: "",
    tipo: "",
    placa: "",
    fecha_inicio: "",
    fecha_fin: "",
    valor: "",
  });

  const loadPolizas = async () => {
    try {
      const res = await api.get("/polizas/");
      setPolizas(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    loadPolizas();
  }, []);

  const createPoliza = async (e) => {
    e.preventDefault();
    try {
      const data = {
        cliente_id: parseInt(form.cliente_id),
        numero_poliza: form.numero_poliza,
        tipo: form.tipo,
        placa: form.placa || null,
        fecha_inicio: form.fecha_inicio,
        fecha_fin: form.fecha_fin,
        valor: parseInt(form.valor.toString().replace(/\./g, "")),
      };
      await api.post("/polizas/", data);
      setForm({
        cliente_id: "",
        numero_poliza: "",
        tipo: "",
        placa: "",
        fecha_inicio: "",
        fecha_fin: "",
        valor: "",
      });
      loadPolizas();
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div className="space-y-8">
      <div className="bg-white p-6 rounded-2xl shadow-xl border border-gray-200">
        <h2 className="text-2xl font-bold text-indigo-600 mb-4">
          Crear Póliza
        </h2>
        <form className="grid grid-cols-1 md:grid-cols-2 gap-4" onSubmit={createPoliza}>
          {[
            ["Cliente ID", "cliente_id"],
            ["Número de Póliza", "numero_poliza"],
            ["Tipo", "tipo"],
            ["Placa", "placa"],
            ["Fecha Inicio", "fecha_inicio", "date"],
            ["Fecha Fin", "fecha_fin", "date"],
            ["Valor", "valor"],
          ].map(([label, key, type]) => (
            <input
              key={key}
              type={type || "text"}
              placeholder={label}
              value={form[key]}
              onChange={(e) => setForm({ ...form, [key]: e.target.value })}
              className="p-3 border rounded-lg focus:ring-indigo-500"
              required={["cliente_id", "numero_poliza", "tipo", "fecha_inicio", "fecha_fin", "valor"].includes(key)}
            />
          ))}
          <button className="col-span-full bg-indigo-600 text-white p-3 rounded-lg hover:bg-indigo-700 transition">
            Crear Póliza
          </button>
        </form>
      </div>

      <div className="grid gap-6 md:grid-cols-3">
        {polizas.map((p) => (
          <div
            key={p.id}
            className="bg-white shadow-md rounded-xl p-4 border border-gray-200"
          >
            <h3 className="font-bold text-indigo-700 text-lg">{p.numero_poliza}</h3>
            <p className="text-gray-600">Tipo: {p.tipo}</p>
            <p className="text-gray-600">Cliente: {p.cliente_id}</p>
            <p className="text-gray-600">
              Valor: ${p.valor.toLocaleString()}
            </p>
            <p className="text-gray-500 text-sm">
              {p.fecha_inicio} → {p.fecha_fin}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}
