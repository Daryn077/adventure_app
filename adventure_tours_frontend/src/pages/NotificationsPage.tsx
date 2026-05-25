import { useEffect, useState } from "react";
import { getNotifications } from "../api/notificationsApi";

export default function NotificationsPage() {
  const [notifications, setNotifications] = useState<string[]>([]);

  const loadNotifications = () => {
    getNotifications()
      .then((res) => setNotifications(res.data))
      .catch((err) => console.log("Notifications error:", err));
  };

  useEffect(() => {
    loadNotifications();

    const interval = setInterval(loadNotifications, 5000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="min-h-screen bg-sky-50 px-6 py-16">
      <div className="mx-auto max-w-5xl">
        <h1 className="text-4xl font-black text-slate-950">
          Notifications
        </h1>

        <p className="mt-3 text-slate-600">
          Redis notifications about tour changes.
        </p>

        <div className="mt-10 space-y-4">
          {notifications.length === 0 ? (
            <div className="rounded-3xl bg-white p-8 text-center font-bold shadow-xl">
              No notifications yet
            </div>
          ) : (
            notifications.map((item, index) => (
              <div
                key={index}
                className="rounded-3xl bg-white p-6 shadow-xl"
              >
                <p className="text-lg font-bold text-slate-900">
                  🔔 {item}
                </p>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}