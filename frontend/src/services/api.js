const API_URL = "http://localhost:5000";

export const signupUser = async (data) => {
  const res = await fetch(`${API_URL}/signup`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });
  return res.json();
};

export const loginUser = async (data) => {
  const res = await fetch(`${API_URL}/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });
  return res.json();
};

export const getWeather = async () => {

const token = localStorage.getItem("token")

const res = await fetch("http://localhost:5000/weather",{
headers:{
Authorization:`Bearer ${token}`
}
})

return res.json()

}