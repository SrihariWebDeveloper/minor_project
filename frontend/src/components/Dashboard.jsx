import { useEffect, useState } from "react";
import { getWeather } from "../services/api.js";

export default function Dashboard({setPage}) {
  const [weather, setWeather] = useState(null);

  useEffect(() => {
    fetchWeather();
  }, []);

  const logout = () => {
    localStorage.removeItem("token");

    setPage("login");
  };

  const fetchWeather = async () => {
    const data = await getWeather();
    setWeather(data);
  };

  if (!weather) return <div className="p-10">Loading...</div>;

  return (
    <div className="min-h-screen bg-gray-100 p-10">
      <button
        onClick={logout}
        className="bg-red-500 text-white px-4 cursor-pointer py-2 rounded mb-6"
      >
        Logout
      </button>
      <h1 className="text-3xl font-bold mb-6">Weather Dashboard</h1>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-6">
        <div className="card">
          🌡 Temp
          <h2>{weather.temperature} °C</h2>
        </div>

        <div className="card">
          💧 Humidity
          <h2>{weather.humidity} %</h2>
        </div>

        <div className="card">
          🧭 Pressure
          <h2>{weather.pressure} hPa</h2>
        </div>

        <div className="card">
          🌪 Wind
          <h2>{weather.wind_speed} km/h</h2>
        </div>
      </div>

      <div className="mt-8 bg-red-100 p-4 rounded">
        <h2 className="font-bold text-red-600">⚠ Weather Alerts</h2>

        {weather.alert.map((i, index) => (
          <p key={index} className="text-red-500 pl-4">
            {i}
          </p>
        ))}
      </div>
    </div>
  );
}
