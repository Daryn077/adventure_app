import { Outlet } from "react-router-dom";
import Header from "./Header";
import Footer from "./Footer";
import NotificationToast from "./NotificationToast";

export default function Layout() {
  return (
    <div className="min-h-screen bg-white text-slate-900">
      <Header />

      <NotificationToast />

      <main className="w-full">
        <Outlet />
      </main>

      <Footer />
    </div>
  );
}