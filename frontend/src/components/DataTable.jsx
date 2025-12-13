export default function DataTable({ columns, data }) {
  return (
    <div className="overflow-auto bg-white rounded-2xl shadow-lg border border-gray-200">
      <table className="min-w-full">
        <thead className="bg-indigo-50">
          <tr>
            {columns.map((c, i) => (
              <th
                key={i}
                className="p-3 text-left text-sm font-semibold text-indigo-600"
              >
                {c}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.map((row, idx) => (
            <tr key={idx} className="odd:bg-white even:bg-indigo-50">
              {Object.values(row).map((v, i) => (
                <td key={i} className="p-3 text-sm text-gray-700">
                  {String(v)}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

