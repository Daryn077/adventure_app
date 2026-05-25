export type Tour = {
  id: number;
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
  average_rating?: number;
  participants_count?: number;
};