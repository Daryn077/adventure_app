import { useEffect, useState } from "react";
import { getRoutes } from "../api/routesApi";
import type { Route } from "../types/route";

export default function RoutesPage() {
  const [routes, setRoutes] = useState<Route[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getRoutes()
      .then((res) => setRoutes(res.data))
      .catch((e) => console.log("Error loading routes", e))
      .finally(() => setLoading(false));
  }, []);

  const getEmbedMap = (route: Route) => {
    const location =
      route.end_point ||
      `${route.start_point} ${route.end_point}`;

    return `https://maps.google.com/maps?q=${encodeURIComponent(
      location
    )}&t=&z=11&ie=UTF8&iwloc=&output=embed`;
  };

  return (
    <div className="bg-[linear-gradient(180deg,#eff9ff_0%,#ffffff_100%)] px-4 py-20 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-7xl">
        <p className="text-sm font-black uppercase tracking-[0.35em] text-sky-600">
          Travel routes
        </p>

        <h1 className="mt-4 text-5xl font-black text-slate-950">
          Adventure routes
        </h1>

        <p className="mt-5 max-w-3xl text-lg leading-8 text-slate-600">
          This page displays detailed travel routes with start point,
          destination, distance, duration and integrated Google Maps.
        </p>

        {loading ? (
          <div className="mt-12 grid gap-7 md:grid-cols-2 xl:grid-cols-3">
            {[1, 2, 3].map((item) => (
              <div
                key={item}
                className="h-[700px] animate-pulse rounded-[2rem] bg-white shadow-xl"
              />
            ))}
          </div>
        ) : routes.length === 0 ? (
          <div className="mt-12 rounded-[2rem] bg-white p-10 text-center shadow-xl">
            <h2 className="text-2xl font-black text-slate-950">
              No routes found
            </h2>
          </div>
        ) : (
          <div className="mt-12 grid gap-7 md:grid-cols-2 xl:grid-cols-3">
            {routes.map((route) => (
              <div
                key={route.id}
                className="overflow-hidden rounded-[2rem] bg-white shadow-xl shadow-sky-900/10 transition hover:-translate-y-2"
              >
                <div className="p-7">
                  <div className="mb-6 flex items-center justify-between">
                    <div className="flex h-16 w-16 items-center justify-center rounded-3xl bg-sky-100 text-3xl">
                      🧭
                    </div>

                    <span className="rounded-full bg-emerald-100 px-4 py-2 text-xs font-black uppercase text-emerald-700">
                      Active Route
                    </span>
                  </div>

                  <h2 className="text-2xl font-black text-slate-950">
                    {route.name}
                  </h2>

                  <p className="mt-3 text-sm leading-6 text-slate-500">
                    {route.description}
                  </p>

                  <div className="mt-6 grid grid-cols-2 gap-3">
                    <div className="rounded-2xl bg-slate-50 p-4">
                      <p className="text-xs font-bold text-slate-400">
                        Distance
                      </p>

                      <p className="mt-1 text-lg font-black text-slate-950">
                        {route.distance_km} km
                      </p>
                    </div>

                    <div className="rounded-2xl bg-slate-50 p-4">
                      <p className="text-xs font-bold text-slate-400">
                        Duration
                      </p>

                      <p className="mt-1 text-lg font-black text-slate-950">
                        {route.duration_hours} h
                      </p>
                    </div>
                  </div>

                  <div className="mt-5 rounded-2xl bg-slate-50 p-5">
                    <p className="text-sm font-bold text-slate-400">
                      Start point
                    </p>

                    <p className="mt-1 font-black text-slate-900">
                      {route.start_point}
                    </p>
                  </div>

                  <div className="mt-3 rounded-2xl bg-slate-50 p-5">
                    <p className="text-sm font-bold text-slate-400">
                      Destination
                    </p>

                    <p className="mt-1 font-black text-slate-900">
                      {route.end_point}
                    </p>
                  </div>
                </div>

                <div className="h-[300px] w-full overflow-hidden border-t border-slate-100">
                  <iframe
                    title={route.name}
                    src={getEmbedMap(route)}
                    width="100%"
                    height="100%"
                    loading="lazy"
                    referrerPolicy="no-referrer-when-downgrade"
                    className="border-0"
                  />
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}