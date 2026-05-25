import { useEffect, useMemo, useState } from "react";
import { Link } from "react-router-dom";
import { getTours } from "../api/toursApi";
import type { Tour } from "../types/tour";
import { useAuthStore } from "../store/authStore";

const images = [
  "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=80",
  "https://images.unsplash.com/photo-1509316785289-025f5b846b35?auto=format&fit=crop&w=1200&q=80",
  "https://images.unsplash.com/photo-1478131143081-80f7f84ca84d?auto=format&fit=crop&w=1200&q=80",
];

export default function ToursPage() {
  const [tours, setTours] = useState<Tour[]>([]);
  const [search, setSearch] = useState("");
  const [difficulty, setDifficulty] = useState("all");
  const [loading, setLoading] = useState(true);

  const { user } = useAuthStore();

  const role = user?.role || user?.role_name;
  const isAdmin = role === "admin";

  useEffect(() => {
    getTours()
      .then((res) => setTours(res.data))
      .catch((e) => console.log("Error loading tours", e))
      .finally(() => setLoading(false));
  }, []);

  const filteredTours = useMemo(() => {
    return tours.filter((tour) => {
      const text = `${tour.title} ${tour.city} ${tour.country}`.toLowerCase();
      const matchesSearch = text.includes(search.toLowerCase());
      const matchesDifficulty =
        difficulty === "all" || tour.difficulty === difficulty;

      return matchesSearch && matchesDifficulty;
    });
  }, [tours, search, difficulty]);

  return (
    <div className="bg-[linear-gradient(180deg,#eff9ff_0%,#ffffff_100%)]">
      <section className="px-4 py-24 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <p className="text-sm font-black uppercase tracking-[0.35em] text-sky-600">
            Adventure Tours
          </p>

          <div className="mt-4 flex flex-col gap-6 lg:flex-row lg:items-end lg:justify-between">
            <div>
              <h1 className="text-5xl font-black text-slate-950 sm:text-6xl">
                Explore tours
              </h1>

              <p className="mt-5 max-w-2xl text-lg leading-8 text-slate-600">
                Choose a tour, check difficulty, location, price and available
                participants.
              </p>
            </div>

            {isAdmin && (
              <Link
                to="/admin/tours"
                className="rounded-full bg-slate-950 px-7 py-4 text-sm font-black uppercase text-white transition hover:bg-sky-600"
              >
                + Create Tour
              </Link>
            )}
          </div>

          <div className="mt-12 rounded-[2rem] bg-white/80 p-5 shadow-xl backdrop-blur">
            <div className="grid gap-4 lg:grid-cols-[1fr_220px]">
              <input
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                placeholder="Search tour, city or country..."
                className="h-16 rounded-2xl border border-slate-200 bg-slate-50 px-5 font-semibold outline-none"
              />

              <select
                value={difficulty}
                onChange={(e) => setDifficulty(e.target.value)}
                className="h-16 rounded-2xl border border-slate-200 bg-slate-50 px-5 font-bold outline-none"
              >
                <option value="all">All difficulty</option>
                <option value="easy">easy</option>
                <option value="medium">medium</option>
                <option value="hard">hard</option>
              </select>
            </div>
          </div>
        </div>
      </section>

      <section className="px-4 pb-24 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          {loading ? (
            <p className="font-bold text-slate-500">Loading...</p>
          ) : (
            <div className="grid gap-8 md:grid-cols-2 xl:grid-cols-3">
              {filteredTours.map((tour, index) => (
                <div
                  key={tour.id}
                  className="group overflow-hidden rounded-[2rem] bg-white shadow-xl shadow-sky-900/10 transition hover:-translate-y-2"
                >
                  <Link to={`/tours/${tour.id}`}>
                    <div className="relative overflow-hidden">
                      <img
                        src={tour.image_url || images[index % images.length]}
                        alt={tour.title}
                        className="h-72 w-full object-cover transition duration-500 group-hover:scale-110"
                      />

                      <div className="absolute left-5 top-5 rounded-full bg-white/90 px-4 py-2 text-xs font-black uppercase text-slate-950">
                        {tour.difficulty}
                      </div>

                      <div className="absolute right-5 top-5 rounded-full bg-slate-950/80 px-4 py-2 text-sm font-black text-white">
                        ★ {tour.average_rating ?? 0}
                      </div>
                    </div>

                    <div className="p-7">
                      <h2 className="text-2xl font-black text-slate-950">
                        {tour.title}
                      </h2>

                      <p className="mt-3 text-sm font-semibold text-slate-500">
                        📍 {tour.city}, {tour.country}
                      </p>

                      <p className="mt-4 line-clamp-3 text-sm leading-6 text-slate-600">
                        {tour.description}
                      </p>

                      <div className="mt-6 flex items-center justify-between border-t border-slate-100 pt-5">
                        <span className="text-xl font-black text-emerald-600">
                          {Number(tour.price).toLocaleString()} ₸
                        </span>

                        <span className="rounded-full bg-slate-950 px-5 py-3 text-sm font-black uppercase text-white">
                          View Tour
                        </span>
                      </div>
                    </div>
                  </Link>

                  {isAdmin && (
                    <div className="flex gap-3 border-t border-slate-100 p-5">
                      <Link
                        to="/admin/tours"
                        className="flex-1 rounded-full bg-sky-500 px-5 py-3 text-center text-sm font-black text-white"
                      >
                        Edit
                      </Link>

                      <Link
                        to="/admin/tours"
                        className="flex-1 rounded-full bg-red-500 px-5 py-3 text-center text-sm font-black text-white"
                      >
                        Delete
                      </Link>
                    </div>
                  )}
                </div>
              ))}
            </div>
          )}
        </div>
      </section>
    </div>
  );
}