import React from 'react';

export default function Stats({ stats }) {
  if (!stats) return null;
  return (
    <div className="stats" style={{ marginTop: 16, fontSize: 18 }}>
      <span style={{ marginRight: 24 }}>Comparisons: <b>{stats.comparisons}</b></span>
      <span style={{ marginRight: 24 }}>Swaps: <b>{stats.swaps}</b></span>
      <span>Time: <b>{stats.time ? stats.time.toFixed(4) : 0} s</b></span>
    </div>
  );
} 