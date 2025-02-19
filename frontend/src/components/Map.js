import React, { useRef, useEffect } from 'react';
import mapboxgl from 'mapbox-gl';
import './Map.css'; // We'll create this file for styling

mapboxgl.accessToken = 'pk.eyJ1IjoiYW1pcmhhc3NhbiIsImEiOiJjbTdiczg4OTUwaGxwMmpzZzZ4azZ0dXk2In0.LFXEgHBqbGgCsr_PDhpRew';

const Map = () => {
  const mapContainerRef = useRef(null);

  useEffect(() => {
    const map = new mapboxgl.Map({
      container: mapContainerRef.current,
      style: 'mapbox://styles/mapbox/streets-v11',
      center: [6.8937, 52.237], // Coordinates for Enschede, Netherlands
      zoom: 12,
    });

    // Add navigation control (zoom buttons)
    map.addControl(new mapboxgl.NavigationControl(), 'top-right');

    // Clean up on unmount
    return () => map.remove();
  }, []);

  return <div className="map-container" ref={mapContainerRef} />;
};

export default Map;
