import React, { useRef, useEffect, useState } from 'react';
import mapboxgl from 'mapbox-gl';
import axios from 'axios';
import './Map.css';

mapboxgl.accessToken = 'pk.eyJ1IjoiYW1pcmhhc3NhbiIsImEiOiJjbTdiczg4OTUwaGxwMmpzZzZ4azZ0dXk2In0.LFXEgHBqbGgCsr_PDhpRew';

const Map = () => {
    const mapContainerRef = useRef(null);
    const [projects, setProjects] = useState([]);
    const [suppliers, setSuppliers] = useState([]);
    const [bouwhubs, setBouwhubs] = useState([]);

    useEffect(() => {
        const map = new mapboxgl.Map({
            container: mapContainerRef.current,
            style: 'mapbox://styles/mapbox/streets-v11',
            center: [5.4697, 51.4416], // Eindhoven, Netherlands
            zoom: 12,
        });

        map.addControl(new mapboxgl.NavigationControl(), 'top-right');

        // Fetch project locations
        axios.get("http://127.0.0.1:8000/api/projects/locations/")
            .then(response => {
                setProjects(response.data);
                response.data.forEach(project => {
                    new mapboxgl.Marker({ color: "blue" }) // Projects: Blue markers
                        .setLngLat([project.longitude, project.latitude])
                        .setPopup(new mapboxgl.Popup().setHTML(`<h3>${project.name}</h3>`))
                        .addTo(map);
                });
            });

        // Fetch supplier locations
        axios.get("http://127.0.0.1:8000/api/suppliers/locations/")
            .then(response => {
                setSuppliers(response.data);
                response.data.forEach(supplier => {
                    new mapboxgl.Marker({ color: "red" }) // Suppliers: Red markers
                        .setLngLat([supplier.longitude, supplier.latitude])
                        .setPopup(new mapboxgl.Popup().setHTML(`<h3>${supplier.name}</h3>`))
                        .addTo(map);
                });
            });

        // Fetch bouwhub locations
        axios.get("http://127.0.0.1:8000/api/bouwhubs/locations/")
            .then(response => {
                setBouwhubs(response.data);
                response.data.forEach(bouwhub => {
                    new mapboxgl.Marker({ color: "green" }) // Bouwhubs: Green markers
                        .setLngLat([bouwhub.longitude, bouwhub.latitude])
                        .setPopup(new mapboxgl.Popup().setHTML(`<h3>${bouwhub.name}</h3>`))
                        .addTo(map);
                });
            });

        return () => map.remove();
    }, []);

    return <div className="map-container" ref={mapContainerRef} />;
};

export default Map;
