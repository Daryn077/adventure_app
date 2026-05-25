import { Link } from "react-router-dom";

export default function NotFoundPage() {
  return (
    <div className="flex min-h-[70vh] items-center justify-center bg-[linear-gradient(180deg,#eff9ff_0%,#ffffff_100%)] px-4">
      <div className="max-w-xl text-center">
        <p className="text-8xl font-black text-sky-500">404</p>

        <h1 className="mt-4 text-4xl font-black text-slate-950">
          Page not found
        </h1>

        <p className="mt-4 text-lg leading-8 text-slate-600">
          This route does not exist. Go back and continue exploring tours.
        </p>

        <Link
          to="/"
          className="mt-8 inline-flex rounded-full bg-slate-950 px-8 py-4 text-sm font-black uppercase tracking-wide text-white transition hover:bg-sky-600"
        >
          Back to home
        </Link>
      </div>
    </div>
  );
}