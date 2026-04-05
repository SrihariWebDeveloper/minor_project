import { useState } from "react";
import { signupUser } from "../services/api.js";

export default function Signup({ setPage }) {
  const [form, setForm] = useState({
    username: "",
    email: "",
    mobile: "",
    password: "",
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await signupUser(form);
    setPage("login");
  };

  return (
    <div className="flex items-center justify-center h-screen bg-blue-100">
      <form
        onSubmit={handleSubmit}
        className="bg-white p-8 rounded-xl shadow-lg w-96"
      >
        <h2 className="text-2xl font-bold mb-4">Signup</h2>

        <input
          name="username"
          placeholder="Username"
          className="border border-gray-300 p-2 rounded mb-4 w-full"
          onChange={handleChange}
        />

        <input
          name="email"
          placeholder="Email"
          className="border border-gray-300 p-2 rounded mb-4 w-full"
          onChange={handleChange}
        />

        <input
          name="mobile"
          placeholder="Mobile"
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

        <button className=" bg-blue-400 text-white w-full p-2 ">Signup</button>

        <p className="mt-3 text-sm">
          Already have account?
          <button onClick={() => setPage("login")} className="text-blue-500">
            Login
          </button>
        </p>
      </form>
    </div>
  );
}
