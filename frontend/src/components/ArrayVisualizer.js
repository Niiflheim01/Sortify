import React from 'react';
import './ArrayVisualizer.css';

const BAR_COLOR = '#4f8cff';
const COMPARE_COLOR = '#ffb347';
const SWAP_COLOR = '#ff4f4f';

export default function ArrayVisualizer({ array, compare = [], swap = [] }) {
  return (
    <div className="array-visualizer">
      {array.map((value, idx) => {
        let color = BAR_COLOR;
        if (swap && swap.includes(idx)) color = SWAP_COLOR;
        else if (compare && compare.includes(idx)) color = COMPARE_COLOR;
        return (
          <div
            key={idx}
            className="array-bar"
            style={{ height: `${value * 3}px`, background: color }}
            title={value}
          >
            <span className="bar-label">{value}</span>
          </div>
        );
      })}
    </div>
  );
} 