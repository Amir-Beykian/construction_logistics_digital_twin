import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import Projects from "./Projects";
import Suppliers from "./Suppliers";
import Bouwhubs from "./Bouwhubs";
import Map from "./components/Map"; // Import Map component

function App() {
    return (
        <Router>
            <nav>
                <Link to="/">Home</Link> |
                <Link to="/projects">Projects</Link> |
                <Link to="/suppliers">Suppliers</Link> |
                <Link to="/bouwhubs">Bouwhubs</Link>
            </nav>
            <Routes>
                <Route path="/" element={<Map />} /> {/* Show map on home page */}
                <Route path="/projects" element={<Projects />} />
                <Route path="/suppliers" element={<Suppliers />} />
                <Route path="/bouwhubs" element={<Bouwhubs />} />
            </Routes>
        </Router>
    );
}

export default App;
