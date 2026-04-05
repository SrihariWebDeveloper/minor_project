import { useState, useEffect } from "react";
import Login from "./components/Login.jsx";
import Signup from "./components/SignUP.jsx";
import Dashboard from "./components/Dashboard.jsx";

function App() {
  const [page, setPage] = useState("signup");

  useEffect(() => {
    const token = localStorage.getItem("token");

    if (token) {
      setPage("dashboard");
    }
  }, []);
  return (
    <div className="min-h-screen bg-gray-100">
      {/* Application Title */}
      <header className="bg-blue-600 text-white py-4 shadow">
        <h1 className="text-3xl font-bold text-center">
          Weather Alert Monitoring System
        </h1>
      </header>

      {/* Page Content */}
      <div>
        {page === "login" && <Login setPage={setPage} />}

        {page === "signup" && <Signup setPage={setPage} />}

        {page === "dashboard" && <Dashboard setPage={setPage} />}
      </div>
    </div>
  );
}

export default App;