import api from "./axios";
import type { Route } from "../types/route";

export const getRoutes = () => {
  return api.get<Route[]>("/routes/");
};

export const getRouteById = (id: number | string) => {
  return api.get<Route>(`/routes/${id}`);
};