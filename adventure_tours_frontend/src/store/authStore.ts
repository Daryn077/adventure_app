import { create } from "zustand";
import { getMe, login } from "../api/authApi";

type User = {
  id: number;
  email: string;
  full_name?: string;
  role_name?: string;
  role?: string;
};

interface AuthState {
  token: string | null;
  user: User | null;
  loginUser: (email: string, password: string) => Promise<void>;
  loadMe: () => Promise<void>;
  logout: () => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  token: localStorage.getItem("token"),
  user: null,

  loginUser: async (email, password) => {
    const res = await login({ email, password });
    const token = res.data.access_token;

    localStorage.setItem("token", token);
    set({ token });

    const me = await getMe();
    set({ user: me.data });
  },

  loadMe: async () => {
    const token = localStorage.getItem("token");

    if (!token) {
      set({ token: null, user: null });
      return;
    }

    try {
      const me = await getMe();
      set({ token, user: me.data });
    } catch {
      localStorage.removeItem("token");
      set({ token: null, user: null });
    }
  },

  logout: () => {
    localStorage.removeItem("token");
    set({ token: null, user: null });
  },
}));