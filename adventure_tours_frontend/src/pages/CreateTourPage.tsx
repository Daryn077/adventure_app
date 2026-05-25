import { useState } from "react";

export default function CreateTourPage() {
  const [form, setForm] = useState({
    title: "",
    location: "",
    duration: "",
    difficulty: "Easy",
    price: "",
    description: "",
  });

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>
  ) => {
    setForm((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    console.log(form);
  };

  return (
    <div className="bg-[linear-gradient(180deg,#eff9ff_0%,#ffffff_100%)] px-4 py-20 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-5xl">
        <div className="mb-12">
          <p className="text-sm font-black uppercase tracking-[0.35em] text-sky-600">
            Create tour
          </p>

          <h1 className="mt-4 text-5xl font-black text-slate-950">
            New adventure tour
          </h1>

          <p className="mt-5 max-w-2xl text-lg leading-8 text-slate-600">
            Create a new travel experience with route details, difficulty,
            pricing and description.
          </p>
        </div>

        <form
          onSubmit={handleSubmit}
          className="rounded-[2.5rem] bg-white p-8 shadow-2xl shadow-sky-900/10 sm:p-12"
        >
          <div className="grid gap-8 md:grid-cols-2">
            <div>
              <label className="mb-3 block text-sm font-black uppercase tracking-wide text-slate-500">
                Tour title
              </label>

              <input
                type="text"
                name="title"
                value={form.title}
                onChange={handleChange}
                placeholder="Mountain Adventure"
                className="h-16 w-full rounded-2xl border border-slate-200 bg-slate-50 px-5 font-semibold outline-none transition focus:border-sky-400 focus:bg-white"
              />
            </div>

            <div>
              <label className="mb-3 block text-sm font-black uppercase tracking-wide text-slate-500">
                Location
              </label>

              <input
                type="text"
                name="location"
                value={form.location}
                onChange={handleChange}
                placeholder="Almaty, Kazakhstan"
                className="h-16 w-full rounded-2xl border border-slate-200 bg-slate-50 px-5 font-semibold outline-none transition focus:border-sky-400 focus:bg-white"
              />
            </div>

            <div>
              <label className="mb-3 block text-sm font-black uppercase tracking-wide text-slate-500">
                Duration
              </label>

              <input
                type="text"
                name="duration"
                value={form.duration}
                onChange={handleChange}
                placeholder="7 days"
                className="h-16 w-full rounded-2xl border border-slate-200 bg-slate-50 px-5 font-semibold outline-none transition focus:border-sky-400 focus:bg-white"
              />
            </div>

            <div>
              <label className="mb-3 block text-sm font-black uppercase tracking-wide text-slate-500">
                Difficulty
              </label>

              <select
                name="difficulty"
                value={form.difficulty}
                onChange={handleChange}
                className="h-16 w-full rounded-2xl border border-slate-200 bg-slate-50 px-5 font-semibold outline-none transition focus:border-sky-400 focus:bg-white"
              >
                <option>Easy</option>
                <option>Medium</option>
                <option>Hard</option>
              </select>
            </div>

            <div className="md:col-span-2">
              <label className="mb-3 block text-sm font-black uppercase tracking-wide text-slate-500">
                Price
              </label>

              <input
                type="number"
                name="price"
                value={form.price}
                onChange={handleChange}
                placeholder="50000"
                className="h-16 w-full rounded-2xl border border-slate-200 bg-slate-50 px-5 font-semibold outline-none transition focus:border-sky-400 focus:bg-white"
              />
            </div>

            <div className="md:col-span-2">
              <label className="mb-3 block text-sm font-black uppercase tracking-wide text-slate-500">
                Description
              </label>

              <textarea
                name="description"
                value={form.description}
                onChange={handleChange}
                placeholder="Describe the route, safety information and travel experience..."
                rows={7}
                className="w-full rounded-3xl border border-slate-200 bg-slate-50 px-5 py-5 font-semibold outline-none transition focus:border-sky-400 focus:bg-white"
              />
            </div>
          </div>

          <div className="mt-10 flex flex-col gap-4 sm:flex-row">
            <button
              type="submit"
              className="h-16 rounded-2xl bg-slate-950 px-8 text-sm font-black uppercase tracking-wide text-white shadow-xl transition hover:-translate-y-1 hover:bg-sky-600"
            >
              Create tour
            </button>

            <button
              type="button"
              className="h-16 rounded-2xl border border-slate-200 bg-slate-50 px-8 text-sm font-black uppercase tracking-wide text-slate-700 transition hover:bg-slate-100"
            >
              Save draft
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}