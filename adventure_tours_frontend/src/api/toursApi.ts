import api from "./axios";
import type { Tour } from "../types/tour";

export type TourPayload = {
  title: string;
  description: string;
  country: string;
  city: string;
  difficulty: string;
  start_date: string;
  end_date: string;
  price: number;
  max_people: number;
  image_url?: string | null;
};

export const getTours = () => {
  return api.get<Tour[]>("/tours/");
};

export const getTourById = (id: number | string) => {
  return api.get<Tour>(`/tours/${id}`);
};

export const createTour = (data: TourPayload) => {
  return api.post<Tour>("/tours/", data);
};

export const updateTour = (id: number | string, data: Partial<TourPayload>) => {
  return api.put<Tour>(`/tours/${id}`, data);
};

export const deleteTour = (id: number | string) => {
  return api.delete(`/tours/${id}`);
};