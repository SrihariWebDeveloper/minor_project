import { useState } from "react";
import { loginUser } from "../services/api.js";

export default function Login({ setPage }) {
  const [form, setForm] = useState({
    email: "",
    password: "",
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const res = await loginUser(form);

    if (res.success) {
      localStorage.setItem("token", res.token);
      setPage("dashboard");
    } else {
      alert("Invalid login");
    }
  };

  return (
    <div className="flex items-center justify-center h-screen bg-blue-100">
      <form
        onSubmit={handleSubmit}
        className="bg-white p-8 rounded-xl shadow-lg w-96"
      >
        <h2 className="text-2xl font-bold mb-4">Login</h2>

        <input
          name="email"
          placeholder="Email"
          className="border border-gray-300 p-2 rounded mb-4 w-full"
          onChange={handleChange}
        />

        <input
          type="password"
          name="password"
          placeholder="Password"
          className="border border-gray-300 p-2 rounded mb-4 w-full"
          onChange={handleChange}
        />

        <button className=" bg-blue-400 text-white w-full p-2 ">Login</button>
        <p className="mt-3 text-sm">
          Don't have an account?
          <button onClick={() => setPage("signup")} className="text-blue-500">
            Signup
          </button>
        </p>
      </form>
    </div>
  );
}
