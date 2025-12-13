import React, { useState, useEffect } from "react";
import api from "../api/axios";

export default function Pagos() {
  const [pagos, setPagos] = useState([]);
  const [form, setForm] = useState({
    cliente_id: "",
    poliza_id: "",
    fecha_pago: "",
    valor_pagado: "",
    pagado: false,
  });

  // Carga de pagos
  const loadData = async () => {
    try {
      const res = await api.get("/pagos");
      setPagos(res.data);
    } catch (err) {
      console.error("Error cargando pagos:", err);
    }
  };

  useEffect(() => {
    loadData();
  }, []);

  // Crear pago
  const createPago = async (e) => {
    e.preventDefault();

    try {
      const data = {
        cliente_id: parseInt(form.cliente_id),
        poliza_id: parseInt(form.poliza_id),
        fecha_pago: form.fecha_pago,
        valor_pagado: parseInt(form.valor_pagado),
        pagado: form.pagado,
      };

      await api.post("/pagos", data);
      setForm({
        cliente_id: "",
        poliza_id: "",
        fecha_pago: "",
        valor_pagado: "",
        pagado: false,
      });
      loadData();
    } catch (err) {
      console.error("Error creando pago:", err);
    }
  };

  return (
    <div className="space-y-8">
      <div className="bg-white p-6 rounded-2xl shadow-xl border border-gray-200">
        <h2 className="text-2xl font-bold text-indigo-600 mb-4">Registrar Pago</h2>
        <form
          className="grid grid-cols-1 md:grid-cols-2 gap-4"
          onSubmit={createPago}
        >
          <input
            type="number"
            placeholder="Cliente ID"
            value={form.cliente_id}
            onChange={(e) => setForm({ ...form, cliente_id: e.target.value })}
            className="p-3 border rounded-lg focus:ring-indigo-500"
            required
          />

          <input
            type="number"
            placeholder="Póliza ID"
            value={form.poliza_id}
            onChange={(e) => setForm({ ...form, poliza_id: e.target.value })}
            className="p-3 border rounded-lg focus:ring-indigo-500"
            required
          />

          <input
            type="date"
            placeholder="Fecha de Pago"
            value={form.fecha_pago}
            onChange={(e) => setForm({ ...form, fecha_pago: e.target.value })}
            className="p-3 border rounded-lg focus:ring-indigo-500"
            required
          />

          <input
            type="number"
            placeholder="Valor Pagado"
            value={form.valor_pagado}
            onChange={(e) =>
              setForm({ ...form, valor_pagado: e.target.value })
            }
            className="p-3 border rounded-lg focus:ring-indigo-500"
            required
          />

          <select
            value={form.pagado}
            onChange={(e) =>
              setForm({ ...form, pagado: e.target.value === "true" })
            }
            className="p-3 border rounded-lg focus:ring-indigo-500"
          >
            <option value={false}>No pagado</option>
            <option value={true}>Pagado</option>
          </select>

          <button className="col-span-full bg-indigo-600 text-white p-3 rounded-lg hover:bg-indigo-700 transition">
            Registrar Pago
          </button>
        </form>
      </div>

      <div className="grid gap-6 md:grid-cols-3">
        {pagos.map((p) => (
          <div
            key={p.id}
            className="bg-white shadow-md rounded-xl p-4 border border-gray-200"
          >
            <p className="font-semibold text-indigo-600">Cliente: {p.cliente_id}</p>
            <p className="text-gray-600">Póliza: {p.poliza_id}</p>
            <p className="text-gray-600">
              Valor Pagado: ${p.valor_pagado.toLocaleString()}
            </p>
            <p className="text-gray-500">
              Pagado: {p.pagado ? "Sí" : "No"}
            </p>
            <p className="text-gray-500">Fecha: {p.fecha_pago}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

