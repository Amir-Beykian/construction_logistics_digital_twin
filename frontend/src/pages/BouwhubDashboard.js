import React, { useState } from "react";
import axios from "axios";
import MapboxLocationPicker from "../components/MapboxLocationPicker";

const BouwhubDashboard = () => {
    const [location, setLocation] = useState({ longitude: null, latitude: null });

    const handleLocationSelect = (lng, lat) => {
        setLocation({ longitude: lng, latitude: lat });
    };

    const registerBouwhubLocation = async () => {
        if (!location.longitude || !location.latitude) {
            alert("Please select a location on the map.");
            return;
        }

        try {
            const response = await axios.post("http://127.0.0.1:8000/api/bouwhubs/register/", {
                name: "Bouwhub Name",
                location: "Eindhoven",
                longitude: location.longitude,
                latitude: location.latitude
            }, {
                headers: { Authorization: `Bearer ${localStorage.getItem("token")}` }
            });

            alert("Bouwhub location registered successfully!");
        } catch (error) {
            alert("Failed to register bouwhub location.");
        }
    };

    return (
        <div>
            <h2>Bouwhub Dashboard</h2>
            <p>Select your Bouwhub location on the map.</p>
            <MapboxLocationPicker onLocationSelect={handleLocationSelect} />
            <button onClick={registerBouwhubLocation}>Register Bouwhub Location</button>
        </div>
    );
};

export default BouwhubDashboard;
