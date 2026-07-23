"use client";

import { Bot } from "lucide-react";

export default function LoadingDots() {
  return (
    <div className="flex justify-start animate-pulse">
      <div className="flex items-end gap-3">

        {/* Bot Avatar */}
        <div className="flex h-10 w-10 items-center justify-center rounded-full bg-gray-200 text-gray-700">
          <Bot size={20} />
        </div>

        {/* Typing Bubble */}
        <div className="rounded-2xl rounded-bl-md border bg-white px-4 py-3 shadow-md">

          <div className="flex items-center gap-2">
            <span className="h-2 w-2 rounded-full bg-gray-400 animate-bounce"></span>

            <span
              className="h-2 w-2 rounded-full bg-gray-400 animate-bounce"
              style={{ animationDelay: "0.15s" }}
            ></span>

            <span
              className="h-2 w-2 rounded-full bg-gray-400 animate-bounce"
              style={{ animationDelay: "0.3s" }}
            ></span>
          </div>

          <p className="mt-2 text-xs text-gray-400">
            Meeple AI is typing...
          </p>

        </div>

      </div>
    </div>
  );
}
