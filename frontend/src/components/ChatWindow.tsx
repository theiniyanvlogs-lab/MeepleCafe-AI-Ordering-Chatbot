"use client";

import { useState, useRef, useEffect } from "react";

import MessageBubble from "./MessageBubble";
import ChatInput from "./ChatInput";
import LoadingDots from "./LoadingDots";

interface Message {
  id: number;
  sender: "user" | "bot";
  text: string;
  timestamp?: string;
}

export default function ChatWindow() {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: 1,
      sender: "bot",
      text:
        "👋 Welcome to Meeple Cafe!\n\nI'm your AI Restaurant Ordering Assistant.\n\nYou can ask me about:\n\n🍔 Menu\n🍕 Pizza\n🥤 Drinks\n🎁 Offers\n🛒 Place Order\n📍 Restaurant Information",
    },
  ]);

  const [loading, setLoading] = useState(false);

  const messagesEndRef = useRef<HTMLDivElement | null>(null);

  // Auto Scroll
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages, loading]);

  const handleSend = async (text: string) => {
    // User Message
    const userMessage: Message = {
      id: Date.now(),
      sender: "user",
      text,
      timestamp: new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit",
      }),
    };

    setMessages((prev) => [...prev, userMessage]);

    setLoading(true);

    try {
      /*
      -----------------------------------------
      FastAPI Integration

      Replace this section later.

      Example:

      const response = await fetch("http://127.0.0.1:8000/chat", {
          method:"POST",
          headers:{
              "Content-Type":"application/json"
          },
          body: JSON.stringify({
              message:text
          })
      });

      const data = await response.json();

      botText = data.answer;
      -----------------------------------------
      */

      await new Promise((resolve) => setTimeout(resolve, 1500));

      const botText =
        "🤖 This is a sample AI response.\n\nLater this message will come from your FastAPI + RAG backend.";

      const botMessage: Message = {
        id: Date.now() + 1,
        sender: "bot",
        text: botText,
        timestamp: new Date().toLocaleTimeString([], {
          hour: "2-digit",
          minute: "2-digit",
        }),
      };

      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      const errorMessage: Message = {
        id: Date.now() + 2,
        sender: "bot",
        text:
          "❌ Sorry! Unable to connect to the AI server.\nPlease try again.",
      };

      setMessages((prev) => [...prev, errorMessage]);

      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex h-full flex-col bg-gray-50">
      {/* Header */}
      <div className="border-b bg-white px-6 py-4 shadow-sm">
        <h2 className="text-xl font-bold text-green-700">
          🤖 Meeple AI Assistant
        </h2>

        <p className="text-sm text-gray-500">
          Ask about menu, food recommendations, pricing, offers, or place your
          order.
        </p>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-6">
        <div className="space-y-5">
          {messages.map((message) => (
            <MessageBubble
              key={message.id}
              sender={message.sender}
              text={message.text}
              timestamp={message.timestamp}
            />
          ))}

          {loading && <LoadingDots />}

          <div ref={messagesEndRef} />
        </div>
      </div>

      {/* Input */}
      <ChatInput
        onSend={handleSend}
        disabled={loading}
      />
    </div>
  );
}
