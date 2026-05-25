import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { register } from "../api/authApi";

export default function RegisterPage() {
  const navigate = useNavigate();

  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    await register({
  full_name: fullName,
  email,
  password,
});

    navigate("/login");
  };

  return (
    <section className="relative min-h-[calc(100vh-96px)] overflow-hidden bg-[url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1800&q=80')] bg-cover bg-center px-4 py-16">
      <div className="absolute inset-0 bg-slate-950/35" />

      <div className="relative mx-auto grid min-h-[calc(100vh-220px)] max-w-6xl items-center gap-10 lg:grid-cols-2">
        <div className="hidden text-white lg:block">
          <p className="text-sm font-black uppercase tracking-[0.35em] text-sky-200">
            Start Exploring
          </p>

          <h1 className="mt-5 text-6xl font-black leading-tight">
            Create your adventure planner.
          </h1>

          <p className="mt-6 max-w-xl text-lg leading-8 text-white/80">
            Join the platform to plan routes, save tours and prepare safe group
            adventures.
          </p>
        </div>

        <form
          onSubmit={handleSubmit}
          className="mx-auto w-full max-w-md rounded-[2rem] bg-white/90 p-8 shadow-2xl backdrop-blur-xl"
        >
          <p className="text-sm font-black uppercase tracking-[0.3em] text-sky-600">
            Register
          </p>

          <h2 className="mt-3 text-4xl font-black text-slate-950">
            New account
          </h2>

          <p className="mt-3 text-slate-500">
            Create an account to start planning your tours.
          </p>

          <div className="mt-8 space-y-4">
            <input
              type="text"
              placeholder="Full name"
              value={fullName}
              onChange={(e) => setFullName(e.target.value)}
              className="h-14 w-full rounded-2xl border border-slate-200 bg-slate-50 px-5 font-semibold outline-none transition focus:border-sky-400 focus:bg-white"
            />

            <input
              type="email"
              placeholder="Email address"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="h-14 w-full rounded-2xl border border-slate-200 bg-slate-50 px-5 font-semibold outline-none transition focus:border-sky-400 focus:bg-white"
            />

            <input
              type="password"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="h-14 w-full rounded-2xl border border-slate-200 bg-slate-50 px-5 font-semibold outline-none transition focus:border-sky-400 focus:bg-white"
            />
          </div>

          <button
            type="submit"
            className="mt-6 h-14 w-full rounded-2xl bg-slate-950 font-black uppercase tracking-wide text-white shadow-xl transition hover:-translate-y-1 hover:bg-sky-600"
          >
            Register
          </button>

          <p className="mt-6 text-center text-sm font-semibold text-slate-500">
            Already have an account?{" "}
            <Link to="/login" className="font-black text-sky-600">
              Login
            </Link>
          </p>
        </form>
      </div>
    </section>
  );
}