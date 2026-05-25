import { useEffect, useState } from "react";
import {
  createTour,
  deleteTour,
  getTours,
  updateTour,
  type TourPayload,
} from "../api/toursApi";
import type { Tour } from "../types/tour";

const initialForm: TourPayload = {
  title: "",
  description: "",
  country: "",
  city: "",
  difficulty: "easy",
  start_date: "",
  end_date: "",
  price: 0,
  max_people: 1,
  image_url: "",
};

export default function AdminToursPage() {
  const [tours, setTours] = useState<Tour[]>([]);
  const [form, setForm] = useState<TourPayload>(initialForm);
  const [editingId, setEditingId] = useState<number | null>(null);
  const [loading, setLoading] = useState(true);

  const loadTours = async () => {
    setLoading(true);
    const res = await getTours();
    setTours(res.data);
    setLoading(false);
  };

  useEffect(() => {
    loadTours();
  }, []);

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>
  ) => {
    const { name, value } = e.target;

    setForm((prev) => ({
      ...prev,
      [name]:
        name === "price" || name === "max_people" ? Number(value) : value,
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (editingId) {
      await updateTour(editingId, form);
    } else {
      await createTour(form);
    }

    setForm(initialForm);
    setEditingId(null);
    await loadTours();
  };

  const handleEdit = (tour: Tour) => {
    setEditingId(tour.id);

    setForm({
      title: tour.title,
      description: tour.description,
      country: tour.country,
      city: tour.city,
      difficulty: tour.difficulty,
      start_date: tour.start_date,
      end_date: tour.end_date,
      price: Number(tour.price),
      max_people: tour.max_people,
      image_url: tour.image_url || "",
    });

    window.scrollTo({ top: 0, behavior: "smooth" });
  };

  const handleDelete = async (id: number) => {
    const ok = confirm("Delete this tour?");
    if (!ok) return;

    await deleteTour(id);
    await loadTours();
  };

  return (
    <div className="bg-[linear-gradient(180deg,#eff9ff_0%,#ffffff_100%)] px-4 py-20 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-7xl">
        <p className="text-sm font-black uppercase tracking-[0.35em] text-sky-600">
          Admin panel
        </p>

        <h1 className="mt-4 text-5xl font-black text-slate-950">
          Manage tours
        </h1>

        <p className="mt-5 max-w-2xl text-lg leading-8 text-slate-600">
          Add, edit and delete adventure tours. This page is available only for admin.
        </p>

        <form
          onSubmit={handleSubmit}
          className="mt-12 rounded-[2.5rem] bg-white p-8 shadow-2xl shadow-sky-900/10"
        >
          <h2 className="text-3xl font-black text-slate-950">
            {editingId ? "Edit tour" : "Create new tour"}
          </h2>

          <div className="mt-8 grid gap-5 md:grid-cols-2">
            <input name="title" value={form.title} onChange={handleChange} placeholder="Title" className="h-14 rounded-2xl border border-slate-200 bg-slate-50 px-5 font-semibold outline-none" />
            <input name="country" value={form.country} onChange={handleChange} placeholder="Country" className="h-14 rounded-2xl border border-slate-200 bg-slate-50 px-5 font-semibold outline-none" />
            <input name="city" value={form.city} onChange={handleChange} placeholder="City" className="h-14 rounded-2xl border border-slate-200 bg-slate-50 px-5 font-semibold outline-none" />

            <select name="difficulty" value={form.difficulty} onChange={handleChange} className="h-14 rounded-2xl border border-slate-200 bg-slate-50 px-5 font-semibold outline-none">
              <option value="easy">easy</option>
              <option value="medium">medium</option>
              <option value="hard">hard</option>
            </select>

            <input type="date" name="start_date" value={form.start_date} onChange={handleChange} className="h-14 rounded-2xl border border-slate-200 bg-slate-50 px-5 font-semibold outline-none" />
            <input type="date" name="end_date" value={form.end_date} onChange={handleChange} className="h-14 rounded-2xl border border-slate-200 bg-slate-50 px-5 font-semibold outline-none" />
            <input type="number" name="price" value={form.price} onChange={handleChange} placeholder="Price" className="h-14 rounded-2xl border border-slate-200 bg-slate-50 px-5 font-semibold outline-none" />
            <input type="number" name="max_people" value={form.max_people} onChange={handleChange} placeholder="Max people" className="h-14 rounded-2xl border border-slate-200 bg-slate-50 px-5 font-semibold outline-none" />

            <input name="image_url" value={form.image_url || ""} onChange={handleChange} placeholder="Image URL" className="md:col-span-2 h-14 rounded-2xl border border-slate-200 bg-slate-50 px-5 font-semibold outline-none" />

            <textarea name="description" value={form.description} onChange={handleChange} placeholder="Description" rows={5} className="md:col-span-2 rounded-2xl border border-slate-200 bg-slate-50 px-5 py-4 font-semibold outline-none" />
          </div>

          <div className="mt-8 flex gap-4">
            <button className="rounded-full bg-slate-950 px-8 py-4 text-sm font-black uppercase text-white hover:bg-sky-600">
              {editingId ? "Save changes" : "Create tour"}
            </button>

            {editingId && (
              <button
                type="button"
                onClick={() => {
                  setEditingId(null);
                  setForm(initialForm);
                }}
                className="rounded-full bg-slate-100 px-8 py-4 text-sm font-black uppercase text-slate-700"
              >
                Cancel
              </button>
            )}
          </div>
        </form>

        <div className="mt-12">
          <h2 className="text-3xl font-black text-slate-950">Tours list</h2>

          {loading ? (
            <p className="mt-6 font-bold text-slate-500">Loading...</p>
          ) : (
            <div className="mt-6 grid gap-5">
              {tours.map((tour) => (
                <div
                  key={tour.id}
                  className="grid gap-5 rounded-[2rem] bg-white p-5 shadow-xl shadow-sky-900/10 lg:grid-cols-[160px_1fr_auto]"
                >
                  <img
                    src={
                      tour.image_url ||
                      "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=800&q=80"
                    }
                    alt={tour.title}
                    className="h-32 w-full rounded-3xl object-cover"
                  />

                  <div>
                    <h3 className="text-2xl font-black text-slate-950">
                      {tour.title}
                    </h3>
                    <p className="mt-2 text-sm font-semibold text-slate-500">
                      📍 {tour.city}, {tour.country}
                    </p>
                    <p className="mt-2 line-clamp-2 text-sm text-slate-500">
                      {tour.description}
                    </p>
                    <p className="mt-3 font-black text-emerald-600">
                      {Number(tour.price).toLocaleString()} ₸
                    </p>
                  </div>

                  <div className="flex gap-3 lg:flex-col">
                    <button
                      onClick={() => handleEdit(tour)}
                      className="rounded-full bg-sky-500 px-6 py-3 text-sm font-black text-white"
                    >
                      Edit
                    </button>

                    <button
                      onClick={() => handleDelete(tour.id)}
                      className="rounded-full bg-red-500 px-6 py-3 text-sm font-black text-white"
                    >
                      Delete
                    </button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}