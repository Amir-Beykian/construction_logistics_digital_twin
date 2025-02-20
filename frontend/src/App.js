import React, { useContext, useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import { AuthContext } from "./context/AuthContext";
import Login from "./pages/Login";
import Register from "./pages/Register";
import ProjectDashboard from "./pages/ProjectDashboard";
import SupplierDashboard from "./pages/SupplierDashboard";
import BouwhubDashboard from "./pages/BouwhubDashboard";
import AdminDashboard from "./pages/AdminDashboard";

function App() {
    const { user } = useContext(AuthContext);
    const [role, setRole] = useState(localStorage.getItem("role") || "");

    useEffect(() => {
        setRole(localStorage.getItem("role"));
    }, [user]);

    return (
        <Router>
            <Routes>
                <Route path="/login" element={<Login />} />
                <Route path="/register" element={<Register />} />

                {/* Role-Based Dashboards */}
                {role === "project" && <Route path="/dashboard" element={<ProjectDashboard />} />}
                {role === "supplier" && <Route path="/dashboard" element={<SupplierDashboard />} />}
                {role === "bouwhub" && <Route path="/dashboard" element={<BouwhubDashboard />} />}
                {role === "admin" && <Route path="/dashboard" element={<AdminDashboard />} />}

                {/* Redirect if no role is found */}
                <Route path="*" element={<Navigate to="/login" />} />
            </Routes>
        </Router>
    );
}

export default App;