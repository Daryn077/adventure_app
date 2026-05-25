import { useEffect, useState } from "react";
import { getEquipment } from "../api/equipmentApi";
import type { Equipment } from "../types/equipment";

export default function EquipmentPage() {
  const [equipment, setEquipment] = useState<Equipment[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getEquipment()
      .then((res) => setEquipment(res.data))
      .catch((e) => console.log("Error loading equipment", e))
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="bg-white px-4 py-20 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-7xl">
        <p className="text-sm font-black uppercase tracking-[0.35em] text-emerald-600">
          Equipment
        </p>

        <h1 className="mt-4 text-5xl font-black text-slate-950">
          Travel equipment
        </h1>

        <p className="mt-5 max-w-2xl text-lg leading-8 text-slate-600">
          Check available equipment for safe and comfortable adventure trips.
        </p>

        {loading ? (
          <div className="mt-12 grid gap-7 md:grid-cols-3">
            {[1, 2, 3].map((item) => (
              <div
                key={item}
                className="h-[330px] animate-pulse rounded-[2rem] bg-slate-100"
              />
            ))}
          </div>
        ) : equipment.length === 0 ? (
          <div className="mt-12 rounded-[2rem] bg-slate-50 p-10 text-center">
            <h2 className="text-2xl font-black text-slate-950">
              No equipment found
            </h2>
          </div>
        ) : (
          <div className="mt-12 grid gap-7 md:grid-cols-3">
            {equipment.map((item) => (
              <div
                key={item.id}
                className="rounded-[2rem] border border-slate-100 bg-slate-50 p-7 transition hover:-translate-y-2 hover:bg-white hover:shadow-xl"
              >
                <div className="mb-6 flex h-16 w-16 items-center justify-center rounded-3xl bg-emerald-100 text-3xl">
                  🎒
                </div>

                <h2 className="text-2xl font-black text-slate-950">
                  {item.name}
                </h2>

                <p className="mt-3 line-clamp-4 text-sm leading-6 text-slate-500">
                  {item.description}
                </p>

                <div className="mt-6 flex items-center justify-between">
                  <span
                    className={[
                      "rounded-full px-4 py-2 text-sm font-black",
                      item.quantity > 0
                        ? "bg-white text-emerald-600"
                        : "bg-red-50 text-red-600",
                    ].join(" ")}
                  >
                    {item.quantity > 0 ? "Available" : "Out of stock"}
                  </span>

                  <span className="text-xl font-black text-slate-950">
                    {item.quantity} pcs
                  </span>
                </div>

                <button className="mt-7 w-full rounded-full bg-slate-950 px-5 py-3 text-sm font-black uppercase text-white hover:bg-emerald-600">
                  View equipment
                </button>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}