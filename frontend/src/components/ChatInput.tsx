"use client";

import { useState, KeyboardEvent } from "react";
import { SendHorizontal } from "lucide-react";

interface ChatInputProps {
  onSend: (message: string) => void;
  disabled?: boolean;
}

export default function ChatInput({
  onSend,
  disabled = false,
}: ChatInputProps) {
  const [message, setMessage] = useState("");

  const sendMessage = () => {
    const text = message.trim();

    if (!text || disabled) return;

    onSend(text);
    setMessage("");
  };

  const handleKeyDown = (e: KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className="border-t bg-white p-4">
      <div className="flex items-center gap-3 rounded-2xl border bg-gray-50 p-2 shadow-sm">

        <input
          type="text"
          placeholder="Ask about menu, offers or place an order..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={handleKeyDown}
          disabled={disabled}
          className="flex-1 bg-transparent px-3 py-2 text-sm outline-none"
        />

        <button
          onClick={sendMessage}
          disabled={disabled || !message.trim()}
          className="rounded-xl bg-green-600 p-3 text-white transition hover:bg-green-700 disabled:cursor-not-allowed disabled:bg-gray-300"
        >
          <SendHorizontal size={20} />
        </button>

      </div>
    </div>
  );
}
