import { useEffect, useState } from "react";

export default function NotificationToast() {
  const [message, setMessage] = useState("");
  const [permission, setPermission] = useState<NotificationPermission>(
    "Notification" in window ? Notification.permission : "denied"
  );

  const enableNotifications = async () => {
    if (!("Notification" in window)) {
      alert("Браузер не поддерживает уведомления");
      return;
    }

    const result = await Notification.requestPermission();
    setPermission(result);

    if (result === "granted") {
      new Notification("Adventure Tours", {
        body: "Уведомления включены",
        icon: "/vite.svg",
      });
    }

    if (result === "denied") {
      alert("Уведомления заблокированы. Разреши их в настройках сайта.");
    }
  };

  const showDesktopNotification = (text: string) => {
    if (!("Notification" in window)) return;

    if (Notification.permission === "granted") {
      new Notification("Adventure Tours", {
        body: text,
        icon: "/vite.svg",
      });
    }
  };

  useEffect(() => {
    const socket = new WebSocket("ws://127.0.0.1:8000/notifications/ws");

    socket.onopen = () => {
      console.log("WebSocket connected");
    };

    socket.onmessage = (event) => {
      console.log("Notification received:", event.data);

      setMessage(event.data);
      showDesktopNotification(event.data);

      setTimeout(() => {
        setMessage("");
      }, 5000);
    };

    socket.onerror = (error) => {
      console.log("WebSocket error:", error);
    };

    socket.onclose = () => {
      console.log("WebSocket closed");
    };

    return () => {
      socket.close();
    };
  }, []);

  return (
    <>
      {permission !== "granted" && (
        <button
          onClick={enableNotifications}
          className="fixed bottom-6 right-6 z-[9999] rounded-full bg-sky-600 px-6 py-3 text-sm font-black text-white shadow-2xl"
        >
          Enable notifications
        </button>
      )}

      {message && (
        <div className="fixed right-6 top-24 z-[9999] w-[360px] rounded-3xl border border-sky-100 bg-white p-5 shadow-2xl">
          <p className="text-sm font-black uppercase text-sky-600">
            🔔 Notification
          </p>

          <p className="mt-2 text-sm font-bold text-slate-900">
            {message}
          </p>
        </div>
      )}
    </>
  );
}