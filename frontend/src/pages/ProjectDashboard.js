import React, { useState } from "react";
import axios from "axios";
import MapboxLocationPicker from "../components/MapboxLocationPicker";

const ProjectDashboard = () => {
    const [location, setLocation] = useState({ longitude: null, latitude: null });

    const handleLocationSelect = (lng, lat) => {
        setLocation({ longitude: lng, latitude: lat });
    };

    const registerProjectLocation = async () => {
        if (!location.longitude || !location.latitude) {
            alert("Please select a location on the map.");
            return;
        }

        try {
            const response = await axios.post("http://127.0.0.1:8000/api/projects/register/", {
                name: "Project Name",  // Replace with actual project name input
                location: "Eindhoven", // Replace with actual address input
                longitude: location.longitude,
                latitude: location.latitude
            }, {
                headers: { Authorization: `Bearer ${localStorage.getItem("token")}` }
            });

            alert("Project location registered successfully!");
        } catch (error) {
            alert("Failed to register project location.");
        }
    };

    return (
        <div>
            <h2>Project User Dashboard</h2>
            <p>Select your project location on the map.</p>
            <MapboxLocationPicker onLocationSelect={handleLocationSelect} />
            <button onClick={registerProjectLocation}>Register Project Location</button>
        </div>
    );
};

export default ProjectDashboard;
