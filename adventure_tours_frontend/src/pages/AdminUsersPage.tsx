import { useEffect, useState } from "react";
import api from "../api/axios";

type User = {
  id: number;
  full_name: string;
  email: string;
  role?: string | null;
  role_name?: string | null;
};

export default function AdminUsersPage() {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api
      .get("/users/")
      .then((res) => setUsers(res.data))
      .catch((err) => console.log("Users loading error:", err))
      .finally(() => setLoading(false));
  }, []);

  return (
    <div className="min-h-screen bg-sky-50 px-6 py-16">
      <div className="mx-auto max-w-6xl">
        <h1 className="text-4xl font-black text-slate-950">
          Users Management
        </h1>

        <p className="mt-3 text-slate-600">
          Admin can view all registered users.
        </p>

        <div className="mt-10 overflow-hidden rounded-3xl bg-white shadow-xl">
          <table className="w-full text-left">
            <thead className="bg-slate-950 text-white">
              <tr>
                <th className="px-6 py-4">ID</th>
                <th className="px-6 py-4">Full name</th>
                <th className="px-6 py-4">Email</th>
                <th className="px-6 py-4">Role</th>
              </tr>
            </thead>

            <tbody>
              {loading ? (
                <tr>
                  <td colSpan={4} className="px-6 py-8 text-center font-bold">
                    Loading...
                  </td>
                </tr>
              ) : (
                users.map((user) => (
                  <tr key={user.id} className="border-b border-slate-100">
                    <td className="px-6 py-4 font-bold">{user.id}</td>
                    <td className="px-6 py-4">{user.full_name}</td>
                    <td className="px-6 py-4">{user.email}</td>
                    <td className="px-6 py-4">
                        <span
                            className={
                                (user.role || user.role_name) === "admin"
                                    ? "rounded-full bg-red-100 px-4 py-2 text-sm font-bold text-red-700"
                                    : "rounded-full bg-emerald-100 px-4 py-2 text-sm font-bold text-emerald-700"
                            }
                        >
                            {user.role || user.role_name || "user"}
                        </span>
                        </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}