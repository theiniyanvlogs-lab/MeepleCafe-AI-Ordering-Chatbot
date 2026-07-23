"use client";

import { ShoppingCart } from "lucide-react";

import type { MenuItem } from "@/types/chat";

interface MenuCardProps {
  item: MenuItem;
  onAddToCart?: (item: MenuItem) => void;
}

export default function MenuCard({
  item,
  onAddToCart,
}: MenuCardProps) {
  return (
    <div className="overflow-hidden rounded-2xl border bg-white shadow-sm transition-all hover:shadow-lg">

      {/* Food Image */}
      <div className="h-48 bg-gray-100">
        <img
          src={
            item.image ||
            "https://placehold.co/600x400?text=Meeple+Cafe"
          }
          alt={item.name}
          className="h-full w-full object-cover"
        />
      </div>

      {/* Content */}
      <div className="p-5">

        <span className="rounded-full bg-green-100 px-3 py-1 text-xs font-semibold text-green-700">
          {item.category}
        </span>

        <h3 className="mt-3 text-xl font-bold text-gray-800">
          {item.name}
        </h3>

        <p className="mt-2 text-sm text-gray-600">
          {item.description}
        </p>

        <div className="mt-5 flex items-center justify-between">

          <span className="text-2xl font-bold text-green-700">
            ₹{item.price}
          </span>

          <button
            onClick={() => onAddToCart?.(item)}
            className="flex items-center gap-2 rounded-xl bg-green-600 px-4 py-2 text-white transition hover:bg-green-700"
          >
            <ShoppingCart size={18} />
            Add
          </button>

        </div>

      </div>

    </div>
  );
}
