import React, { createContext, useState, useEffect } from "react";
import axios from "axios";

export const AuthContext = createContext();

const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [token, setToken] = useState(localStorage.getItem("token") || null);

    useEffect(() => {
        if (token) {
            axios.get("http://127.0.0.1:8000/api/users/me/", {
                headers: { Authorization: `Bearer ${token}` },
            })
            .then(response => setUser(response.data))
            .catch(() => logout());
        }
    }, [token]);

    const login = async (credentials) => {
    try {
        const response = await axios.post("http://127.0.0.1:8000/api/users/login/", credentials);
        localStorage.setItem("token", response.data.access);
        localStorage.setItem("role", response.data.role); // Store role
        setToken(response.data.access);
        setUser(response.data);
        return response.data;
    } catch (error) {
        console.error("Login failed", error);
        throw error;
    }
    };


    const logout = () => {
    localStorage.removeItem("token");
    localStorage.removeItem("role");
    setUser(null);
    setToken(null);
    };


    return (
        <AuthContext.Provider value={{ user, token, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
};

export default AuthProvider;
