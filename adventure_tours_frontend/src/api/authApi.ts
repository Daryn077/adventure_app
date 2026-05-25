import api from "./axios";

export const register = (data: {
  full_name: string;
  email: string;
  password: string;
}) => api.post("/auth/register", data);

export const login = (data: {
  email: string;
  password: string;
}) => api.post("/auth/login", data);

export const getMe = () => {
  return api.get("/auth/me");
};