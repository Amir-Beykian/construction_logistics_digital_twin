import React, { useEffect, useState } from "react";
import axios from "axios";
import Map, { Marker, Popup } from "react-map-gl";

const MAPBOX_TOKEN = "your-mapbox-access-token-here"; // Replace with your API key

const AdminDashboard = () => {
    const [locations, setLocations] = useState([]);
    const [selectedLocation, setSelectedLocation] = useState(null);

    useEffect(() => {
        const fetchLocations = async () => {
            try {
                const [projectsRes, suppliersRes, bouwhubsRes] = await Promise.all([
                    axios.get("http://127.0.0.1:8000/api/projects/locations/", {
                        headers: { Authorization: `Bearer ${localStorage.getItem("token")}` }
                    }),
                    axios.get("http://127.0.0.1:8000/api/suppliers/locations/", {
                        headers: { Authorization: `Bearer ${localStorage.getItem("token")}` }
                    }),
                    axios.get("http://127.0.0.1:8000/api/bouwhubs/locations/", {
                        headers: { Authorization: `Bearer ${localStorage.getItem("token")}` }
                    })
                ]);

                setLocations([
                    ...projectsRes.data.map(l => ({ ...l, type: "project" })),
                    ...suppliersRes.data.map(l => ({ ...l, type: "supplier" })),
                    ...bouwhubsRes.data.map(l => ({ ...l, type: "bouwhub" })),
                ]);
            } catch (error) {
                console.error("Failed to fetch locations:", error);
            }
        };

        fetchLocations();
    }, []);

    return (
        <div>
            <h2>Admin Dashboard</h2>
            <p>View all project, supplier, and Bouwhub locations on the map.</p>
            <Map
                initialViewState={{
                    latitude: 51.4416,
                    longitude: 5.4697,
                    zoom: 10
                }}
                style={{ width: "100%", height: "500px" }}
                mapStyle="mapbox://styles/mapbox/streets-v11"
                mapboxAccessToken={MAPBOX_TOKEN}
            >
                {locations.map((loc, index) => (
                    <Marker key={index} longitude={loc.longitude} latitude={loc.latitude}
                        color={loc.type === "project" ? "blue" : loc.type === "supplier" ? "green" : "red"}
                        onClick={() => setSelectedLocation(loc)}
                    />
                ))}

                {selectedLocation && (
                    <Popup
                        longitude={selectedLocation.longitude}
                        latitude={selectedLocation.latitude}
                        onClose={() => setSelectedLocation(null)}
                    >
                        <h3>{selectedLocation.name}</h3>
                        <p>Type: {selectedLocation.type}</p>
                        <p>Location: {selectedLocation.location}</p>
                    </Popup>
                )}
            </Map>
        </div>
    );
};

export default AdminDashboard;
