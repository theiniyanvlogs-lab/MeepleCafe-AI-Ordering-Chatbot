"use client";

import { useState } from "react";
import MessageBubble from "./MessageBubble";
import ChatInput from "./ChatInput";
import LoadingDots from "./LoadingDots";

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

  const [loading, setLoading] = useState(false);

  const handleSend = (text: string) => {
    setMessages((prev) => [
      ...prev,
      {
        id: Date.now(),
        sender: "user",
        text,
      },
    ]);

    setLoading(true);

    // Simulate backend response
    setTimeout(() => {
      setMessages((prev) => [
        ...prev,
        {
          id: Date.now() + 1,
          sender: "bot",
          text: "🤖 This response will come from your FastAPI + RAG backend.",
        },
      ]);

      setLoading(false);
    }, 1500);
  };

  return (
    <div className="flex h-full flex-col bg-gray-50">

      {/* Header */}
      <div className="border-b bg-white px-6 py-4 shadow-sm">
        <h2 className="text-lg font-semibold">
          🤖 Meeple AI Assistant
        </h2>

        <p className="text-sm text-gray-500">
          Ask about menu, offers, or place an order.
        </p>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto space-y-4 p-6">
        {messages.map((message) => (
          <MessageBubble
            key={message.id}
            sender={message.sender}
            text={message.text}
          />
        ))}

        {loading && <LoadingDots />}
      </div>

      {/* Input */}
      <ChatInput
        onSend={handleSend}
        disabled={loading}
      />

    </div>
  );
}
