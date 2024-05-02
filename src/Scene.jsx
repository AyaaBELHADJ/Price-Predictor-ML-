/*import React from "react";
import { OrbitControls, PerspectiveCamera, Environment } from "@react-three/drei";
import { Suspense } from "react";
import { Track } from "./Track";
import { Ground } from "./Ground";
import { Car } from "./Car";

export function Scene() {
  return (
    <Suspense fallback={null}>
      <Environment files={process.env.PUBLIC_URL + "/textures/envmap (1).hdr"} background={"both"} />
      <PerspectiveCamera makeDefault position={[-6, 3.9, 6.21]} fov={40} />
      <OrbitControls
        enableZoom={false}
        enablePan={false}
        enableDamping={true}
        dampingFactor={0.25}
        rotateSpeed={0.5}
        target={[-2.64, -0.71, 0.03]}
      />
      <Track />
      <Ground />
      <Car />
    </Suspense>
  );
} */
import {
  Environment,
  OrbitControls,
  PerspectiveCamera,
} from "@react-three/drei";
import { Suspense, useEffect, useState } from "react";
import { Car } from "./Car";
import { Ground } from "./Ground";
import { Track } from "./Track";
 import R3FButton from "./R3FButton";


export function Scene() {
  const [thirdPerson, setThirdPerson] = useState(false);
  const [cameraPosition, setCameraPosition] = useState([-6, 3.9, 6.21]);

  useEffect(() => {
    function keydownHandler(e) {
      if (e.key === "k") {
        // random is necessary to trigger a state change
        if(thirdPerson) setCameraPosition([-6, 3.9, 6.21 + Math.random() * 0.01]);
        setThirdPerson(!thirdPerson); 
      }
    }

    window.addEventListener("keydown", keydownHandler);
    return () => window.removeEventListener("keydown", keydownHandler);
  }, [thirdPerson]);

  return (
    <Suspense fallback={null}>
      <Environment
        files={process.env.PUBLIC_URL + "/textures/envmap (1).hdr"}
        background={"both"}
      />

      <PerspectiveCamera makeDefault position={cameraPosition} fov={40} />
      {!thirdPerson && (
        <OrbitControls    enableZoom={false}
        enablePan={false}
        enableDamping={true}
        dampingFactor={0.25}
        rotateSpeed={0.5}target={[-2.64, -0.71, 0.03]} />
      )}

      <Ground />
      <Track />
      <R3FButton />
      <Car thirdPerson={thirdPerson} />
    
    </Suspense>
  );
}