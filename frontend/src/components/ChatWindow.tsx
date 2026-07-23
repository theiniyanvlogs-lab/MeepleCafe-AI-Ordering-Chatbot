"use client";

import { useState } from "react";
import MessageBubble from "./MessageBubble";
import ChatInput from "./ChatInput";

interface Message {
  id: number;
  sender: "user" | "bot";
  text: string;
}

export default function ChatWindow() {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: 1,
      sender: "bot",
      text: "👋 Welcome to Meeple Cafe! How can I help you today?",
    },
  ]);

  const handleSend = (text: string) => {
    // Add user message
    setMessages((prev) => [
      ...prev,
      {
        id: Date.now(),
        sender: "user",
        text,
      },
      {
        id: Date.now() + 1,
        sender: "bot",
        text: "🤖 AI response will come from FastAPI backend.",
      },
    ]);
  };

  return (
    <div className="flex h-full flex-col bg-gray-50">

      <div className="border-b bg-white px-6 py-4 shadow-sm">
        <h2 className="text-lg font-semibold">
          🤖 Meeple AI Assistant
        </h2>

        <p className="text-sm text-gray-500">
          Ask about our menu or place an order.
        </p>
      </div>

      <div className="flex-1 space-y-4 overflow-y-auto p-6">
        {messages.map((message) => (
          <MessageBubble
            key={message.id}
            sender={message.sender}
            text={message.text}
          />
        ))}
      </div>

      <ChatInput onSend={handleSend} />

    </div>
  );
}
