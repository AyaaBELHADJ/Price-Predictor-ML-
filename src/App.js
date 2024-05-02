/*import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Button from './Button';
import CarForm from './CarForm';
import { Canvas } from '@react-three/fiber';
import { Scene } from './Scene'; // Import the Scene component


function Home() {
  return (
    <>
       <Canvas style={{ width: '100vw', height: '100vh' }}>
        <Scene /> {/* Include the Scene component here *//*}
      </Canvas>
      <Button />
    </>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        {/* Render the Home component on the home route *//*}
        <Route path="/" element={<Home />} />
        <Route path="/car-form" element={<CarForm />} />
      </Routes>
    </Router>
  );
}

export default App;

/*function Home() {
  return (
    <Canvas style={{ width: '100vw', height: '100vh' }}>
        
      <Scene />

    </Canvas>
  );
} */





// App.js
/*import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Button from './Button';
import CarForm from './CarForm';
import { Canvas } from '@react-three/fiber';
import { Scene } from './Scene'; // Assuming you have a Scene component

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/car-form" element={<CarForm />} />
        <Route path="/" element={<Home />} />
      </Routes>
    </Router>
  );
}

function Home() {
  return (
    <>
      <Scene />
      <Button />
    </>
  );
}

export default App;*/
/*import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Button from './Button';
import CarForm from './CarForm';
import { Canvas } from '@react-three/fiber';
import { Physics } from '@react-three/cannon'; // Import Physics
import { Scene } from './Scene'; // Import the Scene component

function Home() {
  return (
    <>
      {/* Wrap the Scene component with Physics *//*}
      <Physics gravity={[0, -30, 0]}>
        <Canvas style={{ width: '100vw', height: '100vh' }}>
          <Scene /> {/* Include the Scene component here *//*}
        </Canvas>
      </Physics>
      <Button />
    </>
  );
} 

function App() {
  return (
    <Router>
      <Routes>
        {/* Render the Home component on the home route *//*}
        <Route path="/" element={<Home />} />
        <Route path="/car-form" element={<CarForm />} />
      </Routes>
    </Router>
  );
}

export default App;*/
// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import R3FButton from './R3FButton'; // Importez R3FButton au lieu de Button
import CarForm from './CarForm';
import { Canvas } from '@react-three/fiber';
import { Physics } from '@react-three/cannon';
import { Scene } from './Scene';

function Home() {
  return (
    <>
      <Canvas style={{ width: '100vw', height: '100vh' }}>
        <Physics gravity={[0, -2, 0]}>
          <Scene />
          <R3FButton /> {/* Utilisez R3FButton au lieu de Button */}
        </Physics>
        
      </Canvas>
      <div className="controls">
        <p>press w a s d to move</p>
        <p>press k to swap camera</p>
        <p>press r to reset</p>
        <p>press arrows for flips</p>
      </div>
    </>
  );
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/car-form" element={<CarForm />} />
      </Routes>
    </Router>
  );
}

export default App;
