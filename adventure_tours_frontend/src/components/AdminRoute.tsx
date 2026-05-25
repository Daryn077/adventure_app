import { Navigate } from "react-router-dom";
import { useAuthStore } from "../store/authStore";

export default function AdminRoute({ children }: { children: React.ReactNode }) {
  const { token, user } = useAuthStore();

  if (!token) {
    return <Navigate to="/login" replace />;
  }

  const role = user?.role_name || user?.role;

  if (role !== "admin") {
    return <Navigate to="/" replace />;
  }

  return children;
}