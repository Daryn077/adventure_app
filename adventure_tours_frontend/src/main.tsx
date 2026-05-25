import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";

import { RouterProvider } from "react-router-dom";
import router from "./providers/router";

import { useAuthStore } from "./store/authStore";
import { useEffect } from "react";

function AppWrapper() {
  const { loadMe } = useAuthStore();

  useEffect(() => {
    loadMe();
  }, [loadMe]);

  return <RouterProvider router={router} />;
}

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <AppWrapper />
  </React.StrictMode>
);