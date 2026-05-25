import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

import { getTours } from "../api/toursApi";
import type { Tour } from "../types/tour";

const benefits = [
  "Safe routes",
  "Verified guides",
  "Group planning",
  "Equipment support",
];

const images = [
  "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=80",
  "https://images.unsplash.com/photo-1509316785289-025f5b846b35?auto=format&fit=crop&w=1200&q=80",
  "https://images.unsplash.com/photo-1478131143081-80f7f84ca84d?auto=format&fit=crop&w=1200&q=80",
];

export default function HomePage() {
  const [tours, setTours] = useState<Tour[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getTours()
      .then((res) => setTours(res.data))
      .catch((e) => console.log("Error loading tours", e))
      .finally(() => setLoading(false));
  }, []);

  const topTours = tours.slice(0, 3);

  return (
    <div className="w-full overflow-hidden">
      {/* HERO */}
      <section className="relative min-h-[820px] overflow-hidden">
        {/* 🎥 ВИДЕО */}
        <video
          autoPlay
          muted
          loop
          playsInline
          className="absolute inset-0 h-full w-full object-cover"
        >
          <source src="/video/hero.mp4" type="video/mp4" />
        </video>

        {/* overlay */}
        <div className="absolute inset-0 bg-gradient-to-r from-white/95 via-white/75 to-white/30" />

        {/* контент */}
        <div className="relative z-10 mx-auto flex min-h-[820px] max-w-7xl items-center px-4 py-24 sm:px-6 lg:px-8">
          <div className="max-w-2xl">
            <p className="mb-4 text-sm font-black uppercase tracking-[0.35em] text-sky-700">
              Adventure Travel
            </p>

            <h1 className="text-5xl font-black leading-tight text-slate-950 sm:text-6xl lg:text-7xl">
              Wander Without Limits
            </h1>

            <p className="mt-5 max-w-xl text-lg leading-8 text-slate-700">
              Discover beautiful routes around the world, choose your tour,
              plan your group and enjoy safe adventure travel.
            </p>

            <div className="mt-8 flex flex-wrap gap-3">
              {benefits.map((item) => (
                <span
                  key={item}
                  className="rounded-full bg-white/85 px-5 py-3 text-sm font-bold text-slate-800 shadow-sm backdrop-blur"
                >
                  {item}
                </span>
              ))}
            </div>

            <div className="mt-9 flex flex-col gap-4 sm:flex-row">
              <Link
                to="/tours"
                className="rounded-full bg-slate-950 px-8 py-4 text-center text-sm font-black uppercase tracking-wide text-white shadow-xl transition hover:-translate-y-1 hover:bg-sky-600"
              >
                Explore Tours
              </Link>

              <Link
                to="/routes"
                className="rounded-full bg-white/85 px-8 py-4 text-center text-sm font-black uppercase tracking-wide text-slate-950 shadow-lg backdrop-blur transition hover:-translate-y-1"
              >
                View Routes
              </Link>
            </div>

            {/* 🔍 ПОИСК (теперь НЕ absolute) */}
            <div className="mt-12 w-full max-w-5xl rounded-[2rem] bg-white/90 p-4 shadow-2xl backdrop-blur-xl">
              <div className="grid gap-3 md:grid-cols-[1fr_1fr_1fr_auto]">
                <div className="rounded-3xl bg-slate-100 px-5 py-4">
                  <p className="text-xs font-bold uppercase text-slate-400">
                    Location
                  </p>
                  <p className="font-black text-slate-900">Worldwide</p>
                </div>

                <div className="rounded-3xl bg-slate-100 px-5 py-4">
                  <p className="text-xs font-bold uppercase text-slate-400">
                    Tour type
                  </p>
                  <p className="font-black text-slate-900">Adventure trip</p>
                </div>

                <div className="rounded-3xl bg-slate-100 px-5 py-4">
                  <p className="text-xs font-bold uppercase text-slate-400">
                    Budget
                  </p>
                  <p className="font-black text-slate-900">from 45 000 ₸</p>
                </div>

                <Link
                  to="/tours"
                  className="rounded-3xl bg-sky-500 px-8 py-4 text-center font-black text-white transition hover:bg-sky-600"
                >
                  Search
                </Link>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* ТОП ТУРЫ */}
      <section className="bg-[linear-gradient(180deg,#dff9ff_0%,#ffffff_100%)] px-4 py-20 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <div className="mb-10 flex items-end justify-between gap-6">
            <div>
              <p className="text-sm font-black uppercase tracking-[0.3em] text-sky-600">
                Top tours
              </p>

              <h2 className="mt-3 text-4xl font-black text-slate-950">
                Choose your next adventure
              </h2>
            </div>

            <Link
              to="/tours"
              className="hidden rounded-full bg-slate-950 px-6 py-3 text-sm font-bold text-white md:block"
            >
              View all tours
            </Link>
          </div>

          {loading ? (
            <div className="grid gap-7 md:grid-cols-3">
              {[1, 2, 3].map((item) => (
                <div
                  key={item}
                  className="h-[410px] animate-pulse rounded-[2rem] bg-white shadow-xl"
                />
              ))}
            </div>
          ) : topTours.length === 0 ? (
            <div className="rounded-[2rem] bg-white p-10 text-center shadow-xl">
              <h3 className="text-2xl font-black text-slate-950">
                No tours yet
              </h3>
            </div>
          ) : (
            <div className="grid gap-7 md:grid-cols-3">
              {topTours.map((tour, index) => (
                <Link
                  to={`/tours/${tour.id}`}
                  key={tour.id}
                  className="overflow-hidden rounded-[2rem] bg-white shadow-xl transition hover:-translate-y-2"
                >
                  <img
                    src={tour.image_url || images[index % images.length]}
                    alt={tour.title}
                    className="h-56 w-full object-cover"
                  />

                  <div className="p-6">
                    <div className="mb-3 flex items-center justify-between">
                      <span className="rounded-full bg-sky-50 px-3 py-1 text-xs font-black text-sky-700">
                        ★ {tour.average_rating ?? 0}
                      </span>

                      <span className="font-black text-emerald-600">
                        {tour.price.toLocaleString()} ₸
                      </span>
                    </div>

                    <h3 className="text-2xl font-black text-slate-950">
                      {tour.title}
                    </h3>

                    <p className="mt-2 text-sm font-semibold text-slate-500">
                      📍 {tour.city}, {tour.country}
                    </p>

                    <span className="mt-6 block rounded-full bg-slate-950 px-5 py-3 text-center text-sm font-bold text-white hover:bg-sky-600">
                      View details
                    </span>
                  </div>
                </Link>
              ))}
            </div>
          )}
        </div>
      </section>
    </div>
  );
}