import { useEffect, useState } from "react";
import { getPartners } from "../api/partnersApi";
import type { Partner } from "../types/partner";

export default function PartnersPage() {
  const [partners, setPartners] = useState<Partner[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    getPartners()
      .then((res) => setPartners(res.data))
      .catch((e) => console.log("Error loading partners", e))
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="bg-[linear-gradient(180deg,#f8fafc_0%,#e0f7ff_100%)] px-4 py-20 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-7xl">
        <p className="text-sm font-black uppercase tracking-[0.35em] text-sky-600">
          Partners
        </p>

        <h1 className="mt-4 text-5xl font-black text-slate-950">
          Trusted travel partners
        </h1>

        <p className="mt-5 max-w-2xl text-lg leading-8 text-slate-600">
          View companies and contacts that support adventure tours.
        </p>

        {loading ? (
          <div className="mt-12 grid gap-7 md:grid-cols-3">
            {[1, 2, 3].map((item) => (
              <div
                key={item}
                className="h-[330px] animate-pulse rounded-[2rem] bg-white shadow-xl"
              />
            ))}
          </div>
        ) : partners.length === 0 ? (
          <div className="mt-12 rounded-[2rem] bg-white p-10 text-center shadow-xl">
            <h2 className="text-2xl font-black text-slate-950">
              No partners found
            </h2>
          </div>
        ) : (
          <div className="mt-12 grid gap-7 md:grid-cols-3">
            {partners.map((partner) => (
              <div
                key={partner.id}
                className="rounded-[2rem] bg-white p-7 shadow-xl shadow-sky-900/10 transition hover:-translate-y-2"
              >
                <div className="mb-6 flex h-16 w-16 items-center justify-center rounded-3xl bg-sky-100 text-3xl">
                  🤝
                </div>

                <h2 className="text-2xl font-black text-slate-950">
                  {partner.name}
                </h2>

                <div className="mt-6 space-y-3 text-sm font-semibold text-slate-500">
                  <p>✉️ {partner.contact_email}</p>
                  {partner.phone && <p>📞 {partner.phone}</p>}
                  {partner.website && <p>🌐 {partner.website}</p>}
                </div>

                {partner.website ? (
                  <a
                    href={partner.website}
                    target="_blank"
                    className="mt-7 block rounded-full bg-slate-950 px-5 py-3 text-center text-sm font-black uppercase text-white hover:bg-sky-600"
                  >
                    Open website
                  </a>
                ) : (
                  <button className="mt-7 w-full rounded-full bg-slate-950 px-5 py-3 text-sm font-black uppercase text-white hover:bg-sky-600">
                    View partner
                  </button>
                )}
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}