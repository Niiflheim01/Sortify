import React, { useState, useRef } from 'react';
import Controls from './components/Controls';
import ArrayVisualizer from './components/ArrayVisualizer';
import Stats from './components/Stats';
import './App.css';

const API_URL = process.env.REACT_APP_API_URL || 'http://127.0.0.1:8000/sort';

function App() {
  const [array, setArray] = useState([30, 10, 50, 20, 60, 40]);
  const [algorithm, setAlgorithm] = useState('bubble');
  const [dataStructure, setDataStructure] = useState('array');
  const [steps, setSteps] = useState([]);
  const [currentStep, setCurrentStep] = useState(0);
  const [stats, setStats] = useState(null);
  const [isSorting, setIsSorting] = useState(false);
  const timerRef = useRef(null);

  const startSorting = async () => {
    setIsSorting(true);
    setStats(null);
    setSteps([]);
    setCurrentStep(0);
    try {
      const res = await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          array,
          algorithm,
          data_structure: dataStructure,
        }),
      });
      const data = await res.json();
      setSteps(data.steps);
      setStats(data.stats);
      animateSteps(data.steps, data.stats);
    } catch (err) {
      alert('Error connecting to backend!');
      setIsSorting(false);
    }
  };

  const animateSteps = (stepsArr, statsObj) => {
    let i = 0;
    function next() {
      setCurrentStep(i);
      i++;
      if (i < stepsArr.length) {
        timerRef.current = setTimeout(next, 350);
      } else {
        setIsSorting(false);
      }
    }
    next();
  };

  React.useEffect(() => {
    return () => clearTimeout(timerRef.current);
  }, []);

  const step = steps[currentStep] || { array, compare: [], swap: [] };

  return (
    <div className="App">
      <h1>Sortify: Visual Sorting Simulator</h1>
      <Controls
        array={array}
        setArray={setArray}
        algorithm={algorithm}
        setAlgorithm={setAlgorithm}
        dataStructure={dataStructure}
        setDataStructure={setDataStructure}
        onStart={startSorting}
        isSorting={isSorting}
      />
      <ArrayVisualizer array={step.array} compare={step.compare} swap={step.swap} />
      <Stats stats={stats} />
      <footer style={{ marginTop: 40, color: '#888' }}>
        <small>Made for students &amp; developers | <b>Sortify</b></small>
      </footer>
    </div>
  );
}

export default App;
