import { createBrowserRouter } from "react-router-dom";
import Layout from "../components/Layout";
import AdminRoute from "../components/AdminRoute";
import HomePage from "../pages/HomePage";
import LoginPage from "../pages/LoginPage";
import RegisterPage from "../pages/RegisterPage";
import ToursPage from "../pages/ToursPage";
import TourDetailPage from "../pages/TourDetailPage";
import RoutesPage from "../pages/RoutesPage";
import EquipmentPage from "../pages/EquipmentPage";
import PartnersPage from "../pages/PartnersPage";
import AnalyticsPage from "../pages/AnalyticsPage";
import AdminToursPage from "../pages/AdminToursPage";
import NotFoundPage from "../pages/NotFoundPage";
import AdminUsersPage from "../pages/AdminUsersPage";
import NotificationsPage from "../pages/NotificationsPage";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    children: [
      { path: "/", element: <HomePage /> },
      { path: "/login", element: <LoginPage /> },
      { path: "/register", element: <RegisterPage /> },
      { path: "/tours", element: <ToursPage /> },
      { path: "/tours/:id", element: <TourDetailPage /> },
      { path: "/routes", element: <RoutesPage /> },
      { path: "/equipment", element: <EquipmentPage /> },
      { path: "/partners", element: <PartnersPage /> },
      { path: "/analytics", element: <AnalyticsPage /> },
      {
        path: "/admin/tours",
        element: (
          <AdminRoute>
            <AdminToursPage />
          </AdminRoute>
        ),
      },
      { path: "*", element: <NotFoundPage /> },
      {
      path: "/admin/users", 
      element: (
        <AdminRoute>
          <AdminUsersPage />
        </AdminRoute>
  ),
},
      {
  path: "/notifications",
  element: <NotificationsPage />,
},
    ],
  },
]);

export default router;