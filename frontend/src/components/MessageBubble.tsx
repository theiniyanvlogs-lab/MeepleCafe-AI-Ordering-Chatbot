"use client";

import { Bot, User } from "lucide-react";

interface MessageBubbleProps {
  sender: "user" | "bot";
  text: string;
  timestamp?: string;
}

export default function MessageBubble({
  sender,
  text,
  timestamp,
}: MessageBubbleProps) {
  const isUser = sender === "user";

  return (
    <div
      className={`flex ${
        isUser ? "justify-end" : "justify-start"
      } animate-in fade-in duration-300`}
    >
      <div
        className={`flex max-w-[75%] items-end gap-3 ${
          isUser ? "flex-row-reverse" : ""
        }`}
      >
        {/* Avatar */}
        <div
          className={`flex h-10 w-10 items-center justify-center rounded-full ${
            isUser
              ? "bg-green-600 text-white"
              : "bg-gray-200 text-gray-700"
          }`}
        >
          {isUser ? <User size={20} /> : <Bot size={20} />}
        </div>

        {/* Message */}
        <div
          className={`rounded-2xl px-4 py-3 shadow-md ${
            isUser
              ? "bg-green-600 text-white rounded-br-md"
              : "bg-white text-gray-800 rounded-bl-md border"
          }`}
        >
          <p className="whitespace-pre-wrap text-sm leading-6">
            {text}
          </p>

          <div
            className={`mt-2 text-xs ${
              isUser ? "text-green-100" : "text-gray-400"
            }`}
          >
            {timestamp ??
              new Date().toLocaleTimeString([], {
                hour: "2-digit",
                minute: "2-digit",
              })}
          </div>
        </div>
      </div>
    </div>
  );
}
