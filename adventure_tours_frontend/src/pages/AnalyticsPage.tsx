const cards = [
  { title: "Active tours", value: "12", text: "Tours available this month" },
  { title: "Participants", value: "148", text: "People joined adventure trips" },
  { title: "Routes", value: "24", text: "Prepared travel routes" },
  { title: "Safety checks", value: "98%", text: "Routes checked before trips" },
];

export default function AnalyticsPage() {
  return (
    <div className="bg-[linear-gradient(180deg,#eff9ff_0%,#ffffff_100%)] px-4 py-20 sm:px-6 lg:px-8">
      <div className="mx-auto max-w-7xl">
        <p className="text-sm font-black uppercase tracking-[0.35em] text-sky-600">
          Analytics
        </p>

        <h1 className="mt-4 text-5xl font-black text-slate-950">
          Travel statistics
        </h1>

        <p className="mt-5 max-w-2xl text-lg leading-8 text-slate-600">
          Track tours, participants, routes and safety indicators in one place.
        </p>

        <div className="mt-12 grid gap-6 md:grid-cols-4">
          {cards.map((card) => (
            <div
              key={card.title}
              className="rounded-[2rem] bg-white p-7 shadow-xl shadow-sky-900/10"
            >
              <p className="text-sm font-bold uppercase tracking-wide text-slate-400">
                {card.title}
              </p>

              <p className="mt-4 text-5xl font-black text-slate-950">
                {card.value}
              </p>

              <p className="mt-3 text-sm leading-6 text-slate-500">
                {card.text}
              </p>
            </div>
          ))}
        </div>

        <div className="mt-10 grid gap-8 lg:grid-cols-[1.2fr_0.8fr]">
          <div className="rounded-[2rem] bg-slate-950 p-8 text-white shadow-2xl">
            <h2 className="text-2xl font-black">Monthly activity</h2>

            <div className="mt-8 flex h-72 items-end gap-4">
              {[45, 70, 55, 90, 65, 85, 75].map((height, index) => (
                <div key={index} className="flex flex-1 flex-col items-center gap-3">
                  <div
                    className="w-full rounded-t-2xl bg-sky-400"
                    style={{ height: `${height}%` }}
                  />
                  <span className="text-xs font-bold text-white/50">
                    W{index + 1}
                  </span>
                </div>
              ))}
            </div>
          </div>

          <div className="rounded-[2rem] bg-white p-8 shadow-xl shadow-sky-900/10">
            <h2 className="text-2xl font-black text-slate-950">
              Popular categories
            </h2>

            <div className="mt-8 space-y-5">
              {[
                ["Mountain tours", "82%"],
                ["Camping", "64%"],
                ["Desert trips", "48%"],
                ["Forest routes", "71%"],
              ].map(([name, percent]) => (
                <div key={name}>
                  <div className="mb-2 flex justify-between text-sm font-bold">
                    <span>{name}</span>
                    <span>{percent}</span>
                  </div>

                  <div className="h-3 overflow-hidden rounded-full bg-slate-100">
                    <div
                      className="h-full rounded-full bg-sky-500"
                      style={{ width: percent }}
                    />
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}