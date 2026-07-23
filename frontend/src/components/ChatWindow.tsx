"use client";

import { useState, useRef, useEffect } from "react";

import MessageBubble from "./MessageBubble";
import ChatInput from "./ChatInput";
import LoadingDots from "./LoadingDots";

import type { Message } from "@/types/chat";

export default function ChatWindow() {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: 1,
      sender: "bot",
      text:
        "👋 Welcome to Meeple Cafe!\n\nI'm your AI Restaurant Ordering Assistant.\n\nYou can ask me about:\n\n🍔 Menu\n🍕 Pizza\n🥤 Drinks\n🍰 Desserts\n🎁 Offers\n🛒 Place Order\n📍 Restaurant Information",
      timestamp: new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit",
      }),
    },
  ]);

  const [loading, setLoading] = useState(false);

  const messagesEndRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages, loading]);

  function getBotReply(query: string): string {
    const q = query.toLowerCase();

    // Greetings
    if (
      q.includes("hi") ||
      q.includes("hello") ||
      q.includes("hey")
    ) {
      return `👋 Hello!

Welcome to Meeple Cafe.

How can I help you today?

🍔 Menu
🍕 Pizza
🥤 Drinks
🛒 Place Order`;
    }

    // Menu
    if (q.includes("menu")) {
      return `📋 Today's Menu

🍔 Burgers

• Classic Veg Burger - ₹179
• Crispy Chicken Burger - ₹229
• Nashville Chicken Burger - ₹249

🍕

• Margherita Pizza - ₹299
• Farmhouse Pizza - ₹349
• Chicken Supreme Pizza - ₹399

🥤 Drinks

• Coke - ₹60
• Lemon Mint Cooler - ₹90
• Cold Coffee - ₹120

🍰 Desserts

• Brownie - ₹150
• Ice Cream - ₹120`;
    }

    // Burger
    if (q.includes("burger")) {
      return `🍔 Our Burgers

1. Classic Veg Burger
₹179

2. Crispy Chicken Burger
₹229

3. Nashville Chicken Burger
₹249

Would you like to add one to your cart?`;
    }

    // Pizza
    if (q.includes("pizza")) {
      return `🍕

Available Pizzas

🍕 Margherita
₹299

🍕 Farmhouse
₹349

🍕 Chicken Supreme
₹399`;
    }

    // Drinks
    if (
      q.includes("drink") ||
      q.includes("juice") ||
      q.includes("coffee")
    ) {
      return `🥤 Available Drinks

🥤 Coke
₹60

🍹 Lemon Mint Cooler
₹90

☕ Cold Coffee
₹120`;
    }

    // Dessert
    if (
      q.includes("dessert") ||
      q.includes("cake") ||
      q.includes("ice cream")
    ) {
      return `🍰 Desserts

🍫 Brownie
₹150

🍨 Vanilla Ice Cream
₹120

🍮 Chocolate Lava Cake
₹180`;
    }

    // Offer
    if (
      q.includes("offer") ||
      q.includes("discount")
    ) {
      return `🎁 Current Offers

✅ Flat 10% OFF above ₹500

✅ Free Coke on Burger Combo

✅ Buy 2 Pizza Get Garlic Bread FREE`;
    }

    // Timing
    if (
      q.includes("time") ||
      q.includes("open") ||
      q.includes("close")
    ) {
      return `🕒 Restaurant Timing

Monday - Sunday

10:00 AM

to

10:30 PM`;
    }

    // Location
    if (
      q.includes("location") ||
      q.includes("address") ||
      q.includes("where")
    ) {
      return `📍 Meeple Cafe

Anna Nagar

Chennai

Tamil Nadu`;
    }

    // Contact
    if (
      q.includes("phone") ||
      q.includes("contact")
    ) {
      return `☎ Contact Us

+91 98765 43210

support@meeplecafe.com`;
    }

    // Order
    if (
      q.includes("order") ||
      q.includes("buy")
    ) {
      return `🛒 Great!

Please tell me

• Food Name

• Quantity

Example

2 Chicken Burgers

or

1 Farmhouse Pizza`;
    }

    return `🤖 Sorry, I couldn't understand your request.

You can ask me about:

🍔 Menu

🍕

Pizza

🥤 Drinks

🎁 Offers

📍 Restaurant Information

🛒 Place Order`;
  }

  const handleSend = async (text: string) => {
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
      // Simulate API delay
      await new Promise((resolve) =>
        setTimeout(resolve, 1200)
      );

      const botMessage: Message = {
        id: Date.now() + 1,
        sender: "bot",
        text: getBotReply(text),
        timestamp: new Date().toLocaleTimeString([], {
          hour: "2-digit",
          minute: "2-digit",
        }),
      };

      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          id: Date.now() + 2,
          sender: "bot",
          text: "❌ Unable to connect to the AI server.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex h-full flex-col bg-gray-50">
      {/* Header */}
      <div className="border-b bg-white px-6 py-4 shadow-sm">
        <h2 className="text-xl font-bold text-green-700">
          🤖 Meeple Cafe AI
        </h2>

        <p className="text-sm text-gray-500">
          AI Restaurant Ordering Assistant
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
