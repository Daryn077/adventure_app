import api from "./axios";
import type { Equipment } from "../types/equipment";

export const getEquipment = () => {
  return api.get<Equipment[]>("/equipment/");
};

export const getEquipmentById = (id: number | string) => {
  return api.get<Equipment>(`/equipment/${id}`);
};