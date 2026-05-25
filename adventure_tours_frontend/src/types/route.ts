export interface Route {
  id: number;
  name: string;
  description: string;
  distance_km: number;
  duration_hours: number;
  start_point: string;
  end_point: string;
  map_url?: string | null;
}