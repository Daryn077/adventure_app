import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { getTourById } from "../api/toursApi";
import type { Tour } from "../types/tour";

const images = [
  "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1600&q=80",
  "https://images.unsplash.com/photo-1509316785289-025f5b846b35?auto=format&fit=crop&w=1600&q=80",
  "https://images.unsplash.com/photo-1478131143081-80f7f84ca84d?auto=format&fit=crop&w=1600&q=80",
];

export default function TourDetailPage() {
  const { id } = useParams();
  const [tour, setTour] = useState<Tour | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!id) return;

    getTourById(id)
      .then((res) => setTour(res.data))
      .catch((e) => console.log("Error loading tour", e))
      .finally(() => setLoading(false));
  }, [id]);

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-50 px-4 py-20">
        <div className="mx-auto max-w-7xl">
          <div className="h-[520px] animate-pulse rounded-[2.5rem] bg-white shadow-xl" />
        </div>
      </div>
    );
  }

  if (!tour) {
    return (
      <div className="flex min-h-[70vh] items-center justify-center px-4 text-center">
        <div>
          <h1 className="text-4xl font-black text-slate-950">
            Tour not found
          </h1>
          <Link
            to="/tours"
            className="mt-6 inline-flex rounded-full bg-slate-950 px-7 py-4 font-black text-white"
          >
            Back to tours
          </Link>
        </div>
      </div>
    );
  }

  const image = tour.image_url || images[tour.id % images.length];

  return (
    <div className="bg-white">
      <section
        className="relative min-h-[620px] bg-cover bg-center"
        style={{ backgroundImage: `url(${image})` }}
      >
        <div className="absolute inset-0 bg-gradient-to-r from-slate-950/85 via-slate-950/45 to-transparent" />

        <div className="relative mx-auto flex min-h-[620px] max-w-7xl items-center px-4 py-20 sm:px-6 lg:px-8">
          <div className="max-w-3xl text-white">
            <Link
              to="/tours"
              className="mb-8 inline-flex rounded-full bg-white/15 px-5 py-3 text-sm font-bold backdrop-blur transition hover:bg-white/25"
            >
              ← Back to tours
            </Link>

            <p className="text-sm font-black uppercase tracking-[0.35em] text-sky-200">
              {tour.city}, {tour.country}
            </p>

            <h1 className="mt-4 text-5xl font-black leading-tight sm:text-7xl">
              {tour.title}
            </h1>

            <p className="mt-6 max-w-2xl text-lg leading-8 text-white/85">
              {tour.description}
            </p>

            <div className="mt-8 flex flex-wrap gap-3">
              <span className="rounded-full bg-white/15 px-5 py-3 font-bold backdrop-blur">
                ★ {tour.average_rating ?? 0}
              </span>

              <span className="rounded-full bg-white/15 px-5 py-3 font-bold capitalize backdrop-blur">
                {tour.difficulty}
              </span>

              <span className="rounded-full bg-white/15 px-5 py-3 font-bold backdrop-blur">
                Max {tour.max_people ?? "-"} people
              </span>
            </div>
          </div>
        </div>
      </section>

      <section className="px-4 py-16 sm:px-6 lg:px-8">
        <div className="mx-auto grid max-w-7xl gap-8 lg:grid-cols-[1fr_380px]">
          <div className="rounded-[2rem] bg-slate-50 p-8">
            <h2 className="text-3xl font-black text-slate-950">
              Tour information
            </h2>

            <div className="mt-8 grid gap-4 sm:grid-cols-2">
              <div className="rounded-3xl bg-white p-6">
                <p className="text-sm font-bold text-slate-400">Location</p>
                <p className="mt-2 text-xl font-black">
                  {tour.city}, {tour.country}
                </p>
              </div>

              <div className="rounded-3xl bg-white p-6">
                <p className="text-sm font-bold text-slate-400">Difficulty</p>
                <p className="mt-2 text-xl font-black capitalize">
                  {tour.difficulty}
                </p>
              </div>

              <div className="rounded-3xl bg-white p-6">
                <p className="text-sm font-bold text-slate-400">Start date</p>
                <p className="mt-2 text-xl font-black">
                  {tour.start_date ?? "Not specified"}
                </p>
              </div>

              <div className="rounded-3xl bg-white p-6">
                <p className="text-sm font-bold text-slate-400">End date</p>
                <p className="mt-2 text-xl font-black">
                  {tour.end_date ?? "Not specified"}
                </p>
              </div>

              <div className="rounded-3xl bg-white p-6">
                <p className="text-sm font-bold text-slate-400">
                  Participants
                </p>
                <p className="mt-2 text-xl font-black">
                  {tour.participants_count ?? 0} / {tour.max_people ?? "-"}
                </p>
              </div>

              <div className="rounded-3xl bg-white p-6">
                <p className="text-sm font-bold text-slate-400">Safety</p>
                <p className="mt-2 text-xl font-black">Route checked</p>
              </div>
            </div>
          </div>

          <aside className="rounded-[2rem] bg-slate-950 p-8 text-white shadow-2xl">
            <p className="text-sm font-bold uppercase tracking-[0.3em] text-sky-300">
              Price
            </p>

            <p className="mt-4 text-5xl font-black">
              {tour.price.toLocaleString()} ₸
            </p>

            <p className="mt-3 text-white/60">per participant</p>

            <button className="mt-8 h-14 w-full rounded-2xl bg-sky-500 font-black uppercase tracking-wide text-white transition hover:bg-sky-600">
              Book tour
            </button>

            <button className="mt-3 h-14 w-full rounded-2xl bg-white/10 font-black uppercase tracking-wide text-white transition hover:bg-white/20">
              Add to favorites
            </button>
          </aside>
        </div>
      </section>
    </div>
  );
}