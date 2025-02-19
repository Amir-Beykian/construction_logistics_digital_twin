import React, { useState } from "react";
import Map, { Marker } from "react-map-gl";
import "mapbox-gl/dist/mapbox-gl.css";

const MAPBOX_TOKEN = "pk.eyJ1IjoiYW1pcmhhc3NhbiIsImEiOiJjbTdiczg4OTUwaGxwMmpzZzZ4azZ0dXk2In0.LFXEgHBqbGgCsr_PDhpRew"; // Replace with your API key

const MapboxLocationPicker = ({ onLocationSelect }) => {
    const [viewport, setViewport] = useState({
        latitude: 51.4416, // Default: Eindhoven
        longitude: 5.4697,
        zoom: 12
    });

    const [marker, setMarker] = useState(null);

    const handleMapClick = (event) => {
        const { lng, lat } = event.lngLat;
        setMarker({ longitude: lng, latitude: lat });
        onLocationSelect(lng, lat); // Send the location to the parent component
    };

    return (
        <Map
            initialViewState={viewport}
            style={{ width: "100%", height: "400px" }}
            mapStyle="mapbox://styles/mapbox/streets-v11"
            mapboxAccessToken={MAPBOX_TOKEN}
            onClick={handleMapClick}
        >
            {marker && (
                <Marker longitude={marker.longitude} latitude={marker.latitude} color="red" />
            )}
        </Map>
    );
};

export default MapboxLocationPicker;
