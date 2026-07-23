"use client";

import MessageBubble from "./MessageBubble";

const messages = [
  {
    id: 1,
    sender: "bot",
    text: "👋 Welcome to Meeple Cafe! How can I help you today?",
  },
  {
    id: 2,
    sender: "user",
    text: "Show me your burger menu.",
  },
  {
    id: 3,
    sender: "bot",
    text: "We have Classic Veg Burger (₹179), Crispy Chicken Burger (₹229), and Nashville Chicken Burger (₹249).",
  },
];

export default function ChatWindow() {
  return (
    <div className="flex h-full flex-col bg-gray-50">

      {/* Chat Header */}
      <div className="border-b bg-white px-6 py-4 shadow-sm">
        <h2 className="text-lg font-semibold text-gray-800">
          🤖 Meeple AI Assistant
        </h2>
        <p className="text-sm text-gray-500">
          Ask about our menu, offers, or place an order.
        </p>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-6 space-y-4">
        {messages.map((message) => (
          <MessageBubble
            key={message.id}
            sender={message.sender}
            text={message.text}
          />
        ))}
      </div>
    </div>
  );
}
