import { Link } from "react-router-dom";

export default function Footer() {
  return (
    <footer className="bg-slate-950 px-4 py-14 text-white sm:px-6 lg:px-8">
      <div className="mx-auto grid max-w-7xl gap-10 md:grid-cols-4">
        <div>
          <h2 className="text-2xl font-black">Adventure Tours</h2>
          <p className="mt-4 text-sm leading-7 text-slate-400">
            Plan routes, choose tours and prepare safe adventure trips across
            Kazakhstan.
          </p>
        </div>

        <div>
          <h3 className="font-black">Menu</h3>
          <div className="mt-4 flex flex-col gap-3 text-sm text-slate-400">
            <Link to="/">Home</Link>
            <Link to="/tours">Tours</Link>
            <Link to="/routes">Routes</Link>
          </div>
        </div>

        <div>
          <h3 className="font-black">Services</h3>
          <div className="mt-4 flex flex-col gap-3 text-sm text-slate-400">
            <Link to="/equipment">Equipment</Link>
            <Link to="/partners">Partners</Link>
            <Link to="/analytics">Analytics</Link>
          </div>
        </div>

        <div>
          <h3 className="font-black">Contact</h3>
          <p className="mt-4 text-sm leading-7 text-slate-400">
            Kazakhstan, Karaganda <br />
            adventure.tours@mail.com
          </p>
        </div>
      </div>

      <div className="mx-auto mt-10 max-w-7xl border-t border-white/10 pt-6 text-center text-sm text-slate-500">
        © 2026 Adventure Tours. All rights reserved.
      </div>
    </footer>
  );
}