"use client";

import { Bot } from "lucide-react";

export default function Navbar() {
  return (
    <header className="h-16 bg-white border-b flex items-center justify-between px-6 shadow-sm">
      <div className="flex items-center gap-3">
        <div className="bg-green-600 p-2 rounded-lg">
          <Bot className="text-white w-6 h-6" />
        </div>

        <div>
          <h1 className="text-xl font-bold text-gray-800">
            Meeple Cafe AI
          </h1>

          <p className="text-sm text-gray-500">
            Restaurant Ordering Assistant
          </p>
        </div>
      </div>

      <div className="text-sm text-green-600 font-semibold">
        ● Online
      </div>
    </header>
  );
}
