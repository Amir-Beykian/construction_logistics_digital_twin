import React, { useState } from "react";
import axios from "axios";
import MapboxLocationPicker from "../components/MapboxLocationPicker";

const SupplierDashboard = () => {
    const [location, setLocation] = useState({ longitude: null, latitude: null });

    const handleLocationSelect = (lng, lat) => {
        setLocation({ longitude: lng, latitude: lat });
    };

    const registerSupplierLocation = async () => {
        if (!location.longitude || !location.latitude) {
            alert("Please select a location on the map.");
            return;
        }

        try {
            const response = await axios.post("http://127.0.0.1:8000/api/suppliers/register/", {
                name: "Supplier Name",
                location: "Eindhoven",
                longitude: location.longitude,
                latitude: location.latitude
            }, {
                headers: { Authorization: `Bearer ${localStorage.getItem("token")}` }
            });

            alert("Supplier location registered successfully!");
        } catch (error) {
            alert("Failed to register supplier location.");
        }
    };

    return (
        <div>
            <h2>Supplier Dashboard</h2>
            <p>Select your supplier location on the map.</p>
            <MapboxLocationPicker onLocationSelect={handleLocationSelect} />
            <button onClick={registerSupplierLocation}>Register Supplier Location</button>
        </div>
    );
};

export default SupplierDashboard;
