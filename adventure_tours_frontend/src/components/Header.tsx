import { useState } from "react";
import { Link, NavLink, useNavigate } from "react-router-dom";
import { useAuthStore } from "../store/authStore";

const navItems = [
  { to: "/", label: "Home" },
  { to: "/tours", label: "Tours" },
  { to: "/routes", label: "Routes" },
  { to: "/equipment", label: "Equipment" },
  { to: "/partners", label: "Partners" },
  { to: "/notifications", label: "Notifications" },
];

export default function Header() {
  const [open, setOpen] = useState(false);

  const { token, user, logout } = useAuthStore();

  const navigate = useNavigate();

  const role = user?.role || user?.role_name;

  const isAdmin = role === "admin";

  const linkClass = ({ isActive }: { isActive: boolean }) =>
    [
      "rounded-full px-4 py-2 text-sm font-semibold transition",
      isActive
        ? "bg-sky-100 text-sky-700"
        : "text-slate-600 hover:bg-slate-100 hover:text-slate-900",
    ].join(" ");

  const handleLogout = () => {
    logout();

    setOpen(false);

    navigate("/login");
  };

  return (
    <header className="sticky top-0 z-50 border-b border-white/60 bg-white/80 backdrop-blur-xl">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-4 py-4 sm:px-6 lg:px-8">
        <Link to="/" className="flex items-center gap-3">
          <div className="grid h-11 w-11 place-items-center rounded-2xl bg-sky-500 text-xl font-black text-white">
            A
          </div>

          <div>
            <p className="text-lg font-black text-slate-950">
              Adventure Tours
            </p>

            <p className="text-xs font-semibold uppercase tracking-widest text-sky-600">
              Worldwide travel
            </p>
          </div>
        </Link>

        <nav className="hidden items-center gap-1 lg:flex">
          {navItems.map((item) => (
            <NavLink
              key={item.to}
              to={item.to}
              className={linkClass}
            >
              {item.label}
            </NavLink>
          ))}

          {isAdmin && (
            <>
              <NavLink
                to="/admin/tours"
                className={linkClass}
              >
                Admin Tours
              </NavLink>

              <NavLink
                to="/admin/users"
                className={linkClass}
              >
                Users
              </NavLink>
            </>
          )}
        </nav>

        <div className="hidden items-center gap-3 lg:flex">
          {!token ? (
            <>
              <Link
                to="/login"
                className="rounded-full px-5 py-2 text-sm font-bold"
              >
                Login
              </Link>

              <Link
                to="/register"
                className="rounded-full bg-slate-950 px-5 py-2 text-sm font-bold text-white"
              >
                Register
              </Link>
            </>
          ) : (
            <button
              onClick={handleLogout}
              className="rounded-full bg-red-600 px-5 py-2 text-sm font-bold text-white"
            >
              Logout
            </button>
          )}
        </div>

        <button
          onClick={() => setOpen((prev) => !prev)}
          className="grid h-11 w-11 place-items-center rounded-2xl border border-slate-200 bg-white text-xl lg:hidden"
        >
          ☰
        </button>
      </div>

      {open && (
        <div className="border-t border-slate-100 bg-white px-4 py-4 lg:hidden">
          <div className="flex flex-col gap-2">
            {navItems.map((item) => (
              <NavLink
                key={item.to}
                to={item.to}
                onClick={() => setOpen(false)}
                className={linkClass}
              >
                {item.label}
              </NavLink>
            ))}

            {isAdmin && (
              <>
                <NavLink
                  to="/admin/tours"
                  onClick={() => setOpen(false)}
                  className={linkClass}
                >
                  Admin Tours
                </NavLink>

                <NavLink
                  to="/admin/users"
                  onClick={() => setOpen(false)}
                  className={linkClass}
                >
                  Users
                </NavLink>
              </>
            )}

            {token && (
              <button
                onClick={handleLogout}
                className="mt-3 rounded-2xl bg-red-600 px-4 py-3 font-bold text-white"
              >
                Logout
              </button>
            )}
          </div>
        </div>
      )}
    </header>
  );
}