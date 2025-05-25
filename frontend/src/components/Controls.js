import React, { useState } from 'react';

const ALGORITHMS = [
  { value: 'bubble', label: 'Bubble Sort' },
  { value: 'merge', label: 'Merge Sort' },
  { value: 'quick', label: 'Quick Sort' },
];
const DATA_STRUCTURES = [
  { value: 'array', label: 'Array' },
  { value: 'linked_list', label: 'Linked List' },
];

export default function Controls({
  array,
  setArray,
  algorithm,
  setAlgorithm,
  dataStructure,
  setDataStructure,
  onStart,
  isSorting,
}) {
  const [input, setInput] = useState(array.join(','));

  const handleInputChange = (e) => {
    setInput(e.target.value);
    const arr = e.target.value
      .split(',')
      .map((v) => parseInt(v.trim(), 10))
      .filter((v) => !isNaN(v));
    setArray(arr);
  };

  const handleRandom = () => {
    const len = 10 + Math.floor(Math.random() * 10);
    const arr = Array.from({ length: len }, () => Math.floor(Math.random() * 80) + 10);
    setArray(arr);
    setInput(arr.join(','));
  };

  return (
    <div className="controls" style={{ marginBottom: 24 }}>
      <label>
        Array:
        <input
          type="text"
          value={input}
          onChange={handleInputChange}
          disabled={isSorting}
          style={{ width: 300, marginLeft: 8 }}
        />
      </label>
      <button onClick={handleRandom} disabled={isSorting} style={{ marginLeft: 8 }}>
        Random
      </button>
      <label style={{ marginLeft: 16 }}>
        Algorithm:
        <select
          value={algorithm}
          onChange={(e) => setAlgorithm(e.target.value)}
          disabled={isSorting}
          style={{ marginLeft: 8 }}
        >
          {ALGORITHMS.map((alg) => (
            <option key={alg.value} value={alg.value}>
              {alg.label}
            </option>
          ))}
        </select>
      </label>
      <label style={{ marginLeft: 16 }}>
        Data Structure:
        <select
          value={dataStructure}
          onChange={(e) => setDataStructure(e.target.value)}
          disabled={isSorting}
          style={{ marginLeft: 8 }}
        >
          {DATA_STRUCTURES.map((ds) => (
            <option key={ds.value} value={ds.value}>
              {ds.label}
            </option>
          ))}
        </select>
      </label>
      <button
        onClick={onStart}
        disabled={isSorting || array.length === 0}
        style={{ marginLeft: 16 }}
      >
        Start Sorting
      </button>
    </div>
  );
} 