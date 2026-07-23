"use client";

import {
  House,
  UtensilsCrossed,
  Bot,
  ShoppingCart,
  ClipboardList,
  Info,
} from "lucide-react";

const menuItems = [
  {
    name: "Home",
    icon: House,
  },
  {
    name: "Menu",
    icon: UtensilsCrossed,
  },
  {
    name: "AI Chat",
    icon: Bot,
  },
  {
    name: "Cart",
    icon: ShoppingCart,
  },
  {
    name: "Orders",
    icon: ClipboardList,
  },
  {
    name: "About",
    icon: Info,
  },
];

export default function Sidebar() {
  return (
    <aside className="hidden md:flex w-64 flex-col border-r bg-white shadow-sm">

      {/* Logo */}
      <div className="flex h-20 items-center justify-center border-b">
        <div className="text-center">
          <h2 className="text-2xl font-bold text-green-700">
            🍽️ Meeple Cafe
          </h2>
          <p className="text-xs text-gray-500">
            AI Ordering Assistant
          </p>
        </div>
      </div>

      {/* Navigation */}
      <nav className="flex-1 px-4 py-6">
        <ul className="space-y-2">
          {menuItems.map((item) => {
            const Icon = item.icon;

            return (
              <li key={item.name}>
                <button
                  className="flex w-full items-center gap-3 rounded-xl px-4 py-3 text-gray-700 transition hover:bg-green-100 hover:text-green-700"
                >
                  <Icon size={20} />
                  <span className="font-medium">
                    {item.name}
                  </span>
                </button>
              </li>
            );
          })}
        </ul>
      </nav>

      {/* Footer */}
      <div className="border-t p-4 text-center">
        <p className="text-xs text-gray-500">
          Powered by
        </p>

        <p className="font-semibold text-green-700">
          FastAPI + RAG + FAISS
        </p>
      </div>

    </aside>
  );
}
