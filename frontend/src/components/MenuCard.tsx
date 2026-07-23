"use client";

import Image from "next/image";
import { ShoppingCart } from "lucide-react";

import { useCart } from "@/context/CartContext";
import type { MenuItem } from "@/types/chat";

interface MenuCardProps {
  item: MenuItem;
}

export default function MenuCard({ item }: MenuCardProps) {
  const { addToCart } = useCart();

  const handleAddToCart = () => {
    addToCart(item);
  };

  return (
    <div className="overflow-hidden rounded-2xl border border-gray-200 bg-white shadow-sm transition-all duration-300 hover:-translate-y-1 hover:shadow-lg">
      {/* Food Image */}
      <div className="relative h-52 w-full bg-gray-100">
        <Image
          src={
            item.image ||
            "https://placehold.co/600x400?text=Meeple+Cafe"
          }
          alt={item.name}
          fill
          className="object-cover"
          sizes="(max-width:768px) 100vw, 33vw"
        />
      </div>

      {/* Content */}
      <div className="p-5">
        {/* Category */}
        <span className="inline-block rounded-full bg-green-100 px-3 py-1 text-xs font-semibold text-green-700">
          {item.category}
        </span>

        {/* Food Name */}
        <h3 className="mt-3 text-xl font-bold text-gray-800">
          {item.name}
        </h3>

        {/* Description */}
        <p className="mt-2 min-h-[48px] text-sm leading-6 text-gray-600">
          {item.description}
        </p>

        {/* Price + Button */}
        <div className="mt-6 flex items-center justify-between">
          <span className="text-2xl font-bold text-green-600">
            ₹{item.price}
          </span>

          <button
            onClick={handleAddToCart}
            className="flex items-center gap-2 rounded-xl bg-green-600 px-4 py-2 font-medium text-white transition hover:bg-green-700 active:scale-95"
          >
            <ShoppingCart size={18} />
            Add to Cart
          </button>
        </div>
      </div>
    </div>
  );
}
