import React from 'react';

export default function CardForm({ title, children }) {
  return (
    <div className="bg-white rounded-2xl shadow-lg p-6 border border-gray-200">
      <h3 className="text-xl font-semibold text-indigo-700 mb-4">{title}</h3>
      {children}
    </div>
  );
}
